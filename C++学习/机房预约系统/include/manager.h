#pragma once
#include "module.h"
#include <string>
class Manager
{
public:
    std::vector<AbstractModule *> modules;
    std::string num, name, password;
    Manager(std::vector<AbstractModule *> modules);
    ~Manager();
    virtual void read_from_file() = 0;
    virtual void write_into_file() = 0;
    void set_user_information(std::string num, std::string name, std::string password);
    void show_menu();
    virtual void work(std::string choice) = 0;
    void start();
};