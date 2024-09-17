#include <iostream>
#include <string>

class Person{
    public:
    friend std::ostream& operator<<(std::ostream& os, const Person& p);
    int m_age;
    int* m_height;
    static double PI;   
    std::string m_name;
    mutable int m_width;
    void show_width() const{
        m_width = 10;
        std::cout << "m_width is: " << m_width << std::endl;
    }
    static void init(){
        PI = 3.1415;
    }
    Person& add_from_other_person(Person& p){
        m_age += p.m_age;
        return *this;
    }
    Person(std::string name, int age, int height){
        std::cout << "Person's Person(std::string name, int age, int height) " << std::endl;
        init();
        m_name = name;
        m_age = age;
        m_height = new int(height);
    }
    Person(const Person& p){
        std::cout << "Person's Person(const Person& p) " << std::endl;
        m_name = p.m_name;
        m_age = p.m_age;
        m_height = new int(*p.m_height);
    }
    ~Person(){
        std::cout << "Person's ~Person() " << std::endl;
        if(m_height != NULL){
            delete m_height;
            m_height = NULL;
        }
    }
};
double Person::PI;
// Correct operator overload function
std::ostream& operator<<(std::ostream& os, const Person& p) {
    os << "p's name is: " << p.m_name << ", p's age is: " << p.m_age;
    return os;
}


int main(){
    Person p[2] = {
        {"zhangsan", 10, 160},
        {"sili", 12, 170}
    };
    Person p2 = p[1];
    p2.show_width();
    std::cout << "first person's age is: " << p[0].m_age << std::endl;
    std::cout << "secend person's age is: " << p[1].m_age << std::endl;
    std::cout << "secend person's age is: " << *p2.m_height << std::endl;
    std::cout << "the sizeof person is: " << sizeof(p2) << std::endl;
    std::cout << "the sizeof person is: " << sizeof(p) << std::endl;
    std::cout << "the PI value of person is: " << Person::PI << std::endl;
    p2.add_from_other_person(p2).add_from_other_person(p2);//12*2*2 = 48
    std::cout << "secend person's age is: " << p2.m_age << std::endl;
    std::cout << p2 << std::endl;
    return 0;
}