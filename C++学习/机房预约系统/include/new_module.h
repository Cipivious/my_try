#pragma once
#include <string>
#include <vector>
#include <iostream>
// 定义 AbstractModule 类模板
template <typename... Args>
class AbstractModule
{
public:
    std::string info;
    std::string tag;

    // 纯虚函数，子类必须实现
    virtual std::vector<std::string> menu_function() = 0;

    // realize 函数模板：用于接收不定数量的左值引用
    virtual void realize(std::vector<std::string> &args, Args &...custom_classes) = 0;

    // worker 函数模板：接收不定数量的左值引用
    bool worker(const std::string &choice, Args &...custom_classes);

    static std::string read_from_command_line(const std::string &prompt);
};

// worker 函数的实现
template <typename... Args>
bool AbstractModule<Args...>::worker(const std::string &choice, Args &...custom_classes)
{
    if (choice != tag)
    {
        return false;
    }

    // 调用 menu_function 生成参数 args
    std::vector<std::string> args = menu_function();

    // 将不定数量的左值引用参数传递给 realize
    realize(args, custom_classes...);

    return true;
}

template <typename... Args>
std::string AbstractModule<Args...>::read_from_command_line(const std::string &prompt)
{
    std::cout << "Please enter " << prompt << ": ";
    std::string result;
    std::getline(std::cin, result);
    std::cout << "OK, your entered \"" << result << "\" has been recorded." << std::endl;
    return result;
}