#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <sstream>

// 基类
class Operator {
public:
    virtual double calculate(double a, double b) = 0;
    virtual ~Operator() {}
};

// 加法类
class Add : public Operator {
public:
    double calculate(double a, double b) override {
        return a + b;
    }
};

// 减法类
class Subtract : public Operator {
public:
    double calculate(double a, double b) override {
        return a - b;
    }
};

// 乘法类
class Multiply : public Operator {
public:
    double calculate(double a, double b) override {
        return a * b;
    }
};

// 除法类
class Divide : public Operator {
public:
    double calculate(double a, double b) override {
        if (b == 0) {
            throw std::runtime_error("Division by zero!");
        }
        return a / b;
    }
};

// 工厂方法，用于创建不同的运算对象
std::unique_ptr<Operator> getOperator(const std::string& op) {
    if (op == "+") return std::make_unique<Add>();
    if (op == "-") return std::make_unique<Subtract>();
    if (op == "*") return std::make_unique<Multiply>();
    if (op == "/") return std::make_unique<Divide>();

    throw std::invalid_argument("Unsupported operator");
}

int main() {
    std::string line;
    std::cout << "Enter expression (e.g., 12 + 3): ";
    std::getline(std::cin, line);

    std::istringstream iss(line);
    double a, b;
    std::string op;

    iss >> a >> op >> b;

    try {
        auto oper = getOperator(op);
        double result = oper->calculate(a, b);
        std::cout << "Result: " << result << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    return 0;
}
