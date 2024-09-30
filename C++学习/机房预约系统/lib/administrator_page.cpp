#include "new_module.hpp"
#include <vector>
#include <string>
#include "administrator_page.h"

AdministratorManager::AdministratorManager(std::vector<AdministratorAbstractModule *> modules)
{
    this->modules = modules;
    try
    {
        this->persons = CSVHandler::readCSV("person_information.csv");
        std::cout << "read Data from CSV file" << std::endl;
        std::cout << "person's size is " << persons.size() << std::endl;
        for (auto person = persons.begin(); person != persons.end(); person++)
        {
            std::cout << "name: " << (*person)[0] << " password: " << (*person)[1] << " number: " << (*person)[2] << " identity: " << (*person)[3] << std::endl;
        }
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error reading CSV: " << e.what() << std::endl;
    }
}
AdministratorManager::~AdministratorManager()
{
    try
    {
        CSVHandler::writeCSV("person_information.csv", persons);
        std::cout << "Data written to CSV file successfully!" << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error writing CSV: " << e.what() << std::endl;
    }
}

void AdministratorManager::work(std::string choice)
{
    for (int i = 0; i < modules.size(); i++)
    {
        if (modules[i]->worker(choice, persons))
        {
            break;
        }
    }
}

AddPerson::AddPerson()
{
    info = "add a person(enter: add)";
    tag = "add";
}

std::vector<std::string> AddPerson::menu_function()
{
    std::string name = read_from_command_line("person's name");
    std::string password = read_from_command_line("person's password");
    std::string number = read_from_command_line("person's number");
    std::string identity = read_from_command_line("person's identity");
    return {name, password, number, identity};
}

void AddPerson::realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons)
{
    // std::cout << "hello welcome to add a person" << std::endl;
    persons.push_back(args);
}

RemovePerson::RemovePerson()
{
    info = "remove a person(enter: remove)";
    tag = "remove";
}

std::vector<std::string> RemovePerson::menu_function()
{
    std::string name = read_from_command_line("the person's name your want to remove");
    return {name};
}

void RemovePerson::realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons)
{
    for (auto person = persons.begin(); person != persons.end(); person++)
    {
        if ((*person)[0] == args[0])
        {
            persons.erase(person);
            break;
        }
    }
}

ModifyPerson::ModifyPerson()
{
    info = "modify a person(enter: modify)";
    tag = "modify";
}

std::vector<std::string> ModifyPerson::menu_function()
{
    std::string old_name = read_from_command_line("the person's name your want to modify");
    std::string new_name = read_from_command_line("person's new name");
    std::string password = read_from_command_line("person's new password");
    std::string number = read_from_command_line("person's new number");
    std::string identity = read_from_command_line("person's new identity");
    return {new_name, password, number, identity, old_name};
}

void ModifyPerson::realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons)
{
    for (auto person = persons.begin(); person != persons.end(); person++)
    {
        if ((*person)[0] == args[4])
        {
            for (int i = 0; i < 4; i++)
            {
                (*person)[i] = args[i];
            }
        }
    }
}

ViewAllPersons::ViewAllPersons()
{
    info = "view all person(enter: view)";
    tag = "view";
}

std::vector<std::string> ViewAllPersons::menu_function()
{
    // std::string name = read_from_command_line("the person's name your want to modify");
    std::string name = "view";
    return {name};
}

void ViewAllPersons::realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons)
{
    // std::cout << "name: " << persons[0][0] << std::endl;
    for (auto person = persons.begin(); person != persons.end(); person++)
    {
        std::cout << "name: " << (*person)[0] << " password: " << (*person)[1] << " number: " << (*person)[2] << " identity: " << (*person)[3] << std::endl;
    }
}
// // 定义 FindPerson 类，查找某个成员的信息功能
// class FindPerson : public AdministratorAbstractModule
// {
// public:
//     FindPerson();

//     // 实现菜单功能
//     std::vector<std::string> menu_function() override;

//     // 实现具体的查找某个成员信息逻辑
//     void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons);
// };
