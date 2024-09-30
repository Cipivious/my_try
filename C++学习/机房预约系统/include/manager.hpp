#pragma once
#include "new_module.hpp"
#include <string>

template <typename T>
class Manager
{
public:
    std::vector<T *> modules;
    std::string num, name, password;
    Manager() = default;
    // void set_user_information(std::string num, std::string name, std::string password);
    void show_menu();
    virtual void work(std::string choice) = 0;
    void start();
};

template <typename T>
void Manager<T>::show_menu()
{
    std::cout << "\n\n----------------------------------------" << std::endl;
    std::cout << "Welcome to the person Management System" << std::endl;
    for (int i = 0; i < modules.size(); i++)
    {
        std::cout << modules[i]->info << std::endl;
    }
}

template <typename T>
void Manager<T>::start()
{
    while (true)
    {
        show_menu();
        std::string choice = AbstractModule<int>::read_from_command_line("your choice");
        if (choice == "exit")
        {
            break;
        }
        work(choice);
        system("pause");
        system("cls");
    }
}