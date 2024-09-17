#include <iostream>
// 支付接口，定义支付行为
class PaymentMethod
{
public:
    virtual void pay(double amount) = 0; // 纯虚函数，表示每个支付方式必须实现这个方法
    virtual ~PaymentMethod() = default;  // 虚析构函数，确保派生类可以正确销毁
};
// 信用卡支付实现
class CreditCardPayment : public PaymentMethod
{
public:
    void pay(double amount) override
    {
        std::cout << "使用信用卡支付了 " << amount << " 元。" << std::endl;
    }
};

// PayPal支付实现
class PayPalPayment : public PaymentMethod
{
public:
    void pay(double amount) override
    {
        std::cout << "使用PayPal支付了 " << amount << " 元。" << std::endl;
    }
};
// 在线商店类，依赖支付接口
class OnlineStore
{
private:
    PaymentMethod *paymentMethod; // 使用支付接口
public:
    OnlineStore(PaymentMethod *method) : paymentMethod(method) {}

    void purchase(double amount)
    {
        std::cout << "在线商店购买商品，总金额：" << amount << " 元。" << std::endl;
        paymentMethod->pay(amount); // 通过支付接口进行支付
    }
};

// 订阅服务类，依赖支付接口
class SubscriptionService
{
private:
    PaymentMethod *paymentMethod; // 使用支付接口
public:
    SubscriptionService(PaymentMethod *method) : paymentMethod(method) {}

    void subscribe(double amount)
    {
        std::cout << "订阅服务，总金额：" << amount << " 元。" << std::endl;
        paymentMethod->pay(amount); // 通过支付接口进行支付
    }
};
int main()
{
    // 创建支付方式
    CreditCardPayment creditCardPayment;
    PayPalPayment payPalPayment;

    // 在线商店使用信用卡支付
    OnlineStore store(&creditCardPayment);
    store.purchase(500);
    std::cout << "-------------------------------------------------" << std::endl;
    // 订阅服务使用PayPal支付
    SubscriptionService subscription(&payPalPayment);
    subscription.subscribe(100);

    return 0;
}
