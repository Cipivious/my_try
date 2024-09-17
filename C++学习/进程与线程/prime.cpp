#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
#include <queue>
#include <condition_variable>
#include <cmath>

int gap = 1000;
int thread_num = 8;
std::mutex mtx;
std::vector<int> prime_numbers;

bool is_prime(int num)
{
    if (num % 2 == 0)
        return false;
    for (int i = 3; i < std::sqrt(num); i += 2)
    {
        if (num % i == 0)
        {
            return false;
        }
    }
    return true;
}

void worker(int start)
{
    for (int i = start; i < start + gap; i++)
    {
        if (is_prime(i))
        {
            std::unique_lock<std::mutex> lock(mtx);
            prime_numbers.push_back(i);
        }
    }
}

void test01()
{
    std::cout << "is_prime(5) = " << is_prime(5) << std::endl;
}

int main()
{
    int pre_num = 10000;
    while (1)
    {
        int num = 5;
        std::vector<std::thread> threads;
        for (int i = 0; i < thread_num; i++)
        {
            threads.push_back(std::thread(worker, num)); // 使用线程直接创建
            num += gap;                                  // 每个线程处理 gap 范围内的数字
        }
        for (int i = 0; i < thread_num; i++)
        {
            threads[i].join();
        }
        if (prime_numbers.size() > pre_num)
        {
            for (int i = 0; i < prime_numbers.size(); i++)
            {
                std::cout << prime_numbers[i] << " ";
            }
            std::cout << std::endl;
            break;
        }
    }
    return 0;
}