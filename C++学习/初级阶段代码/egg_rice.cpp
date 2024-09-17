#include <iostream>

class Egg{
    public:
    void egg(){
        std::cout << "add egg" << std::endl;
    }
};

class Rice{
    public:
    void rice(){
        std::cout << "prepare rice" << std::endl;
    }
};

class EggRice: public Egg, public Rice
{
    public:
    EggRice(){
        rice();
        egg();
        std::cout << "it's ok!" << std::endl;
    }
};

int main(){
    EggRice eggrice;
    return 0;
}