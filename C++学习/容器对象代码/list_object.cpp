#include <iostream>
#include <list>
#include <algorithm>

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

bool compare(Person* person1, Person* person2) {
    if (person1->age == person2->age) {
        return person1->height < person2->height; // Ascending order of height
    }
    return person1->age > person2->age; // Descending order of age
}
void test02(){
    std::list<Person*> persons;
    std::string names = "ABCDEFGHIJKL";
    std::string xuanshou = "xuanshou";
    Person* person;
    std::string full_name;
    for(int i = 0; i < names.size(); i++){
        full_name = xuanshou + names[i];
        person = new Person(full_name, rand() % 21 + 10, rand() % 151 + 50);
        persons.push_back(person);
    }

    persons.sort(compare);
    std::for_each(persons.begin(), persons.end(), [](Person* person){std::cout << "person's name is: " << person->name << " person's age is: " << person->age << " person's height is: " << person->height << std::endl;});

    std::for_each(persons.begin(), persons.end(), [](Person* person){delete person;});
}

void test01(){
    std::list<int> list1;
    for(int i = 0; i < 8; i++){
        list1.push_back(i);
    }
    std::for_each(list1.begin(), list1.end(), [](int &num){std::cout << num << " ";});
    list1.remove(3);
    std::cout << std::endl;
    list1.reverse();
    std::for_each(list1.begin(), list1.end(), [](int &num){std::cout << num << " ";});
}

int main(){
    test02();
    return 0; 
}