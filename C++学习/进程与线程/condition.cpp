#include <iostream>
#include <string>
#include <condition_variable>
#include <mutex>
#include <queue>
#include <thread>

std::mutex mtx;
std::condition_variable g_cv;
std::queue<int> queue;
bool finished = false;

void Producer()
{
    for (int i = 0; i < 10000; i++)
    {
        std::unique_lock<std::mutex> lock(mtx);
        queue.push(i);
        std::cout << "Producer: " << i << std::endl;
        g_cv.notify_one();
    }

    // After producing, signal the consumer that we're done
    std::unique_lock<std::mutex> lock(mtx);
    finished = true;
    g_cv.notify_one();
}

void Consumer()
{
    while (true)
    {
        std::unique_lock<std::mutex> lock(mtx);
        g_cv.wait(lock, []()
                  { return !queue.empty() || finished; });

        // If the queue is empty and finished is true, exit the loop
        if (queue.empty() && finished)
            break;

        int value = queue.front();
        queue.pop();
        std::cout << "Consumer: " << value << std::endl;
    }
}

int main()
{
    std::thread t1(Producer);
    std::thread t2(Consumer);
    t1.join();
    t2.join();
    return 0;
}
