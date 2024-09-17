#include <iostream>
#include <vector>
#include <thread>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <functional>
#include <future>
#include <atomic>

class ThreadPool
{
public:
    // 构造函数：启动 thread_count 个线程
    ThreadPool(size_t thread_count);

    // 向线程池提交一个任务，并返回 std::future 对象以获取结果
    template <class F, class... Args>
    auto enqueue(F &&f, Args &&...args) -> std::future<typename std::result_of<F(Args...)>::type>;

    // 析构函数：关闭线程池并等待所有线程完成
    ~ThreadPool();

private:
    // 线程池中的工作线程函数
    void worker_thread();

    std::vector<std::thread> workers;        // 存储工作线程
    std::queue<std::function<void()>> tasks; // 任务队列

    std::mutex queue_mutex;            // 任务队列互斥锁
    std::condition_variable condition; // 条件变量用于线程同步
    std::atomic<bool> stop;            // 线程池是否停止的标志
};

// 构造函数，创建 thread_count 个工作线程
ThreadPool::ThreadPool(size_t thread_count) : stop(false)
{
    for (size_t i = 0; i < thread_count; ++i)
    {
        workers.emplace_back(&ThreadPool::worker_thread, this);
    }
}

// 提交一个任务到线程池，返回 future 用于获取结果
template <class F, class... Args>
auto ThreadPool::enqueue(F &&f, Args &&...args) -> std::future<typename std::result_of<F(Args...)>::type>
{
    using return_type = typename std::result_of<F(Args...)>::type;

    // 创建一个包装任务的 shared pointer，支持异步操作
    auto task = std::make_shared<std::packaged_task<return_type()>>(
        std::bind(std::forward<F>(f), std::forward<Args>(args)...));

    // 获取 future 以便返回
    std::future<return_type> res = task->get_future();

    {
        std::unique_lock<std::mutex> lock(queue_mutex);

        // 在停止时不能提交新任务
        if (stop)
        {
            throw std::runtime_error("enqueue on stopped ThreadPool");
        }

        // 将任务加入任务队列
        tasks.emplace([task]()
                      { (*task)(); });
    }

    // 唤醒一个等待中的线程去执行任务
    condition.notify_one();

    return res;
}

// 工作线程函数，从任务队列中提取任务并执行
void ThreadPool::worker_thread()
{
    while (true)
    {
        std::function<void()> task;

        {
            std::unique_lock<std::mutex> lock(queue_mutex);

            // 等待直到有任务或者线程池关闭
            condition.wait(lock, [this]
                           { return stop || !tasks.empty(); });

            if (stop && tasks.empty())
            {
                return; // 线程池停止且没有任务时退出
            }

            // 从任务队列中获取任务
            task = std::move(tasks.front());
            tasks.pop();
        }

        // 执行任务
        task();
    }
}

// 析构函数，等待所有线程完成并销毁线程池
ThreadPool::~ThreadPool()
{
    {
        std::unique_lock<std::mutex> lock(queue_mutex);
        stop = true;
    }

    // 唤醒所有线程
    condition.notify_all();

    // 等待所有线程完成工作
    for (std::thread &worker : workers)
    {
        worker.join();
    }
}

int main()
{
    // 创建包含 4 个线程的线程池
    ThreadPool pool(4);

    // 提交任务并获取结果
    std::vector<std::future<int>> results;

    for (int i = 0; i < 8; ++i)
    {
        results.emplace_back(
            pool.enqueue([i]
                         {
                std::cout << "Thread " << std::this_thread::get_id() << " working on task " << i << std::endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                return i * i; }));
    }

    // 获取并输出任务结果
    for (auto &&result : results)
    {
        std::cout << "Result: " << result.get() << std::endl;
    }

    return 0;
}
