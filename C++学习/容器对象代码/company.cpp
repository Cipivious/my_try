#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

class Person{
    public:
    std::string name;
    double salary;
    Person(std::string name, double salary){
        this->name = name;
        this->salary = salary;
    }
};

int main(){
    std::vector<std::string> company_part = {"cehua", "meigong", "yanfa"};
    std::multimap<std::string, Person*> person_table;
    std::string names = "ABCDEFGHIJ";
    std::string base_name = "yuangong ";
    std::string full_name;
    for(int i = 0; i < names.size(); i++){
        full_name = base_name + names[i];
        std::pair<std::string, Person*> pair = {company_part[rand() % company_part.size()],  new Person(full_name, rand() % 10000)};
        person_table.insert(pair);
    }

    std::for_each(person_table.begin(), person_table.end(), [](std::pair<std::string, Person*> pair){std::cout << pair.first << ":\t" << pair.second->name << ",\t$" << pair.second->salary << std::endl;});

    std::for_each(person_table.begin(), person_table.end(), [](auto p){delete p.second;});
}