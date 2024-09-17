#include <iostream>

class animals
{
public:
    int age;
};

class Sheep : virtual public animals
{
};
class Tuo : virtual public animals
{
};
class SheepTuo : public Sheep, public Tuo
{
};

int main()
{
    SheepTuo sheep_tuo;
    sheep_tuo.age = 10;
    std::cout << "sheep_tuo.Sheep::age " << sheep_tuo.Sheep::age << std::endl;
    std::cout << "sheep_tuo.Tuo::age " << sheep_tuo.Tuo::age << std::endl;
    std::cout << "sheep_tuo.age " << sheep_tuo.age << std::endl;
    return 0;
}