#include <iostream>
#include <fstream>
#include <string>
#include <locale>
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
void test01(){
    std::ofstream ofs;
    ofs.open("test.txt", std::ios::out);
    ofs << "姓名：张三" << std::endl;
    ofs << "姓名：李四" << std::endl;
    ofs << "姓名：王五" << std::endl;
    ofs.close();
}

void test02(){
    std::ifstream ifs;
    std::string info;
    ifs.open("test.txt", std::ios::in);
    int i = 0;
    while(std::getline(ifs, info)){
        i++;
        std::cout << "第" << i << "行: " << info << std::endl;
    }
    std::cout << "第" << i + 1 << "行: " << info << std::endl;
    ifs.close();
}

void test03(){
    Person p[2] = {
        {"zhangsan", 10, 160},
        {"sili", 12, 170}
    };
    std::ofstream ofs("person.txt", std::ios::out | std::ios::binary);
    ofs.write((const char *)&p, sizeof(p));
    ofs.close();
}

// void test04(){
//     std::ifstream ifs("person.txt", std::ios::in | std::ios::binary);
//     Person p[2];
//     ifs((char *)&p, sizeof(p));
//     std::cout << p[0]->m_age << " " << p[0]->m_height << std::endl;

// }
int main(){
    test03();
    return 0;
}