#include <iostream>

class Operation
{
public:
    virtual ~Operation() {}
    virtual double execute(double a, double b) = 0;
};

class Add : public Operation
{
public:
    double execute(double a, double b) override
    {
        return a + b;
    }
};

class Subtract : public Operation
{
public:
    double execute(double a, double b) override
    {
        return a - b;
    }
};

class Multiply : public Operation
{
public:
    double execute(double a, double b) override
    {
        return a * b;
    }
};

class Divide : public Operation
{
public:
    double execute(double a, double b) override
    {
        if (b == 0)
        {
            throw std::runtime_error("Division by zero");
        }
        return a / b;
    }
};

class Calculator
{
public:
    double calculate(double a, double b, Operation *op)
    {
        return op->execute(a, b);
    }
};

int main()
{
    Calculator calc;
    Operation *op = new Add();
    std::cout << "5 + 3 = " << calc.calculate(5, 3, op) << std::endl;
    delete op;

    op = new Subtract();
    std::cout << "5 - 3 = " << calc.calculate(5, 3, op) << std::endl;
    delete op;

    op = new Multiply();
    std::cout << "5 * 3 = " << calc.calculate(5, 3, op) << std::endl;
    delete op;

    op = new Divide();
    std::cout << "5 / 3 = " << calc.calculate(5, 3, op) << std::endl;
    delete op;

    return 0;
}
