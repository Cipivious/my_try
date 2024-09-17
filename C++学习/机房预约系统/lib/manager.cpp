#include "manager.h"

Manager::Manager(std::vector<AbstractModule *> modules)
{
    this->modules = modules;
    read_from_file();
}
Manager::~Manager()
{
    std::cout << "Welcome to ~Manager()" << std::endl;
    write_into_file();
}

void Manager::show_menu()
{
    std::cout << "\n\n----------------------------------------" << std::endl;
    std::cout << "Welcome to the person Management System" << std::endl;
    for (int i = 0; i < modules.size(); i++)
    {
        std::cout << modules[i]->info << std::endl;
    }
}

void Manager::set_user_information(std::string num, std::string name, std::string password)
{
    this->num = num;
    this->name = name;
    this->password = password;
}
void Manager::start()
{
    while (true)
    {
        show_menu();
        std::string choice = AbstractModule::read_from_command_line("your choice");
        if (choice == "exit")
        {
            break;
        }
        work(choice);
        system("pause");
        system("cls");
    }
}
