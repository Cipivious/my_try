#include <iostream>
// #include <string>

class BasePage
{
    public:
    void header(){
        std::cout << "this is header information" << std::endl;
    }
    void footer(){
        std::cout << "this is footer information" << std::endl;
    }
    void left(){
        std::cout << "this is left information" << std::endl;
    }
};

class Java: public BasePage
{
    public:
    void content(){
        std::cout << "this is Java content information" << std::endl;
    }
};

class Python: public BasePage
{
    public:
    void content(){
        std::cout << "this is Python content information" << std::endl;
    }
};

int main(){
    Java java;
    java.header();
    java.footer();
    java.left();
    java.content();
    std::cout << "--------------------------------------------" << std::endl;
    Python py;
    py.header();
    py.footer();
    py.left();
    py.content();
    return 0;
}