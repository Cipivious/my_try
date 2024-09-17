#include <iostream>
#include <set>
#include <algorithm>

class MyCompare{
    public:
    bool operator()(int a, int b){
        return a < b;
    }
};

class Person{
    public:
    std::string name;
    int age;
    int height;
    Person(std::string name, int age, int height){
        this->name = name;
        this->age = age;
        this->height = height;
    }
};
class MyCompare2{
    public:
    bool operator()(Person* person1, Person* person2) {
    if (person1->age == person2->age) {
        return person1->height < person2->height; // Ascending order of height
    }
    return person1->age > person2->age; // Descending order of age
}
};
void test01(){
    std::set<int, MyCompare> set;
    for(int i = 0; i < 10; i++){
        set.insert(rand() % 100);
    }
    std::for_each(set.begin(), set.end(), [](const int& num){std::cout << num << " " << std::endl;});

}
void test02(){
    std::set<Person*, MyCompare2> persons;
    std::string names = "ABCDEFGHIJKL";
    std::string xuanshou = "xuanshou";
    Person* person;
    std::string full_name;
    for(int i = 0; i < names.size(); i++){
        full_name = xuanshou + names[i];
        person = new Person(full_name, rand() % 21 + 10, rand() % 151 + 50);
        persons.insert(person);
    }
    std::for_each(persons.begin(), persons.end(), [](Person* person){std::cout << "person's fullname is: " << person->name << std::endl;});
}
int main(){
    test02();
    return 0;
}