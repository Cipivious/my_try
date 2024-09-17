#include <iostream>
#include <thread>
#include <atomic>
#include <mutex>

std::atomic<int> shared_data(0);
void func()
{
    for (int i = 0; i < 1000; i++)
    {
        shared_data += 1;
    }
}
void PrintHelloWorld(std::string msg)
{
    std::cout << msg << std::endl;
    return;
}

int main()
{
    std::thread t1(func);
    std::thread t2(func);

    t1.join();
    t2.join();

    std::cout << "a's value is: " << shared_data << std::endl;
    return 0;
}