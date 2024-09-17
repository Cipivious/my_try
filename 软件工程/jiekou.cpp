#include <iostream>
// ֧���ӿڣ�����֧����Ϊ
class PaymentMethod
{
public:
    virtual void pay(double amount) = 0; // ���麯������ʾÿ��֧����ʽ����ʵ���������
    virtual ~PaymentMethod() = default;  // ������������ȷ�������������ȷ����
};
// ���ÿ�֧��ʵ��
class CreditCardPayment : public PaymentMethod
{
public:
    void pay(double amount) override
    {
        std::cout << "ʹ�����ÿ�֧���� " << amount << " Ԫ��" << std::endl;
    }
};

// PayPal֧��ʵ��
class PayPalPayment : public PaymentMethod
{
public:
    void pay(double amount) override
    {
        std::cout << "ʹ��PayPal֧���� " << amount << " Ԫ��" << std::endl;
    }
};
// �����̵��࣬����֧���ӿ�
class OnlineStore
{
private:
    PaymentMethod *paymentMethod; // ʹ��֧���ӿ�
public:
    OnlineStore(PaymentMethod *method) : paymentMethod(method) {}

    void purchase(double amount)
    {
        std::cout << "�����̵깺����Ʒ���ܽ�" << amount << " Ԫ��" << std::endl;
        paymentMethod->pay(amount); // ͨ��֧���ӿڽ���֧��
    }
};

// ���ķ����࣬����֧���ӿ�
class SubscriptionService
{
private:
    PaymentMethod *paymentMethod; // ʹ��֧���ӿ�
public:
    SubscriptionService(PaymentMethod *method) : paymentMethod(method) {}

    void subscribe(double amount)
    {
        std::cout << "���ķ����ܽ�" << amount << " Ԫ��" << std::endl;
        paymentMethod->pay(amount); // ͨ��֧���ӿڽ���֧��
    }
};
int main()
{
    // ����֧����ʽ
    CreditCardPayment creditCardPayment;
    PayPalPayment payPalPayment;

    // �����̵�ʹ�����ÿ�֧��
    OnlineStore store(&creditCardPayment);
    store.purchase(500);
    std::cout << "-------------------------------------------------" << std::endl;
    // ���ķ���ʹ��PayPal֧��
    SubscriptionService subscription(&payPalPayment);
    subscription.subscribe(100);

    return 0;
}
