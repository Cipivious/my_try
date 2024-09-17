#include <iostream>
#include <string>
#include <vector>
#include "new_module.h"
// 定义 ConcreteModule 类，继承 AbstractModule 并实现具体逻辑
class ConcreteModule : public AbstractModule<std::string, int, double>
{
public:
    ConcreteModule()
    {
        tag = "ModuleTag";
    }

    // 实现 menu_function
    std::vector<std::string> menu_function() override
    {
        return {"Option1", "Option2"};
    }

    // 实现 realize 函数，处理传入的左值引用参数
    void realize(const std::vector<std::string> &args, std::string &str_arg, int &int_arg, double &double_arg) override
    {
        std::cout << "Realize called with args:" << std::endl;
        for (const auto &arg : args)
        {
            std::cout << "  Arg: " << arg << std::endl;
        }

        std::cout << "Processing custom classes:" << std::endl;
        std::cout << "  String arg: " << str_arg << std::endl;
        std::cout << "  Int arg: " << int_arg << std::endl;
        std::cout << "  Double arg: " << double_arg << std::endl;
    }
};

int main()
{
    // 创建 ConcreteModule 实例
    ConcreteModule module;

    // 定义自定义参数
    std::string param1 = "CustomParam1";
    int param2 = 42;
    double param3 = 3.14;

    // 调用 worker 函数，将左值引用传递给 realize
    if (module.worker("ModuleTag", param1, param2, param3))
    {
        std::cout << "Worker executed successfully!" << std::endl;
    }
    else
    {
        std::cout << "Worker execution failed!" << std::endl;
    }

    return 0;
}
