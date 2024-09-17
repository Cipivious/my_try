#include <iostream>
#include <string>

template<typename NameType, typename AgeType>
class Student{
    public:
    NameType name;
    AgeType age;
    Student(NameType& name, AgeType& age){
        this->name = name;
        this->age = age;
    }

    void show(){
        std::cout << "name: " << name << std::endl;
        std::cout << "age: " << age << std::endl;
    }

};

void test01(){
    Student<std::string, int> stu("zhangsan", 18);
    stu.show();
}

int main(){
    test01();
    return 0;
}