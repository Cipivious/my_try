#include "new_module.hpp"
#include <vector>
#include <string>
#include "Student_page.h"

StudentManager::StudentManager(std::vector<StudentAbstractModule *> modules)
{
    this->modules = modules;
    try
    {
        this->Reservations = CSVHandler::readCSV("computer_information.csv");
        std::cout << "read Data from CSV file" << std::endl;
        std::cout << "Reservation's size is " << Reservations.size() << std::endl;
        for (auto Reservation = Reservations.begin(); Reservation != Reservations.end(); Reservation++)
        {
            std::cout << "name: " << (*Reservation)[0] << " password: " << (*Reservation)[1] << " number: " << (*Reservation)[2] << " identity: " << (*Reservation)[3] << std::endl;
        }
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error reading CSV: " << e.what() << std::endl;
    }
}
StudentManager::~StudentManager()
{
    try
    {
        CSVHandler::writeCSV("computer_information.csv", Reservations);
        std::cout << "Data written to CSV file successfully!" << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error writing CSV: " << e.what() << std::endl;
    }
}

void StudentManager::work(std::string choice)
{
    for (int i = 0; i < modules.size(); i++)
    {
        if (modules[i]->worker(choice, Reservations))
        {
            break;
        }
    }
}

AddReservation::AddReservation()
{
    info = "add a Reservation(enter: add)";
    tag = "add";
}

std::vector<std::string> AddReservation::menu_function()
{
    std::string name = read_from_command_line("Reservation's name");
    std::string password = read_from_command_line("Reservation's password");
    std::string number = read_from_command_line("Reservation's number");
    std::string identity = read_from_command_line("Reservation's identity");
    return {name, password, number, identity};
}

void AddReservation::realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations)
{
    // std::cout << "hello welcome to add a Reservation" << std::endl;
    Reservations.push_back(args);
}

RemoveReservation::RemoveReservation()
{
    info = "remove a Reservation(enter: remove)";
    tag = "remove";
}

std::vector<std::string> RemoveReservation::menu_function()
{
    std::string name = read_from_command_line("the Reservation's name your want to remove");
    return {name};
}

void RemoveReservation::realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations)
{
    for (auto Reservation = Reservations.begin(); Reservation != Reservations.end(); Reservation++)
    {
        if ((*Reservation)[0] == args[0])
        {
            Reservations.erase(Reservation);
            break;
        }
    }
}

ModifyReservation::ModifyReservation()
{
    info = "modify a Reservation(enter: modify)";
    tag = "modify";
}

std::vector<std::string> ModifyReservation::menu_function()
{
    std::string old_name = read_from_command_line("the Reservation's name your want to modify");
    std::string new_name = read_from_command_line("Reservation's new name");
    std::string password = read_from_command_line("Reservation's new password");
    std::string number = read_from_command_line("Reservation's new number");
    std::string identity = read_from_command_line("Reservation's new identity");
    return {new_name, password, number, identity, old_name};
}

void ModifyReservation::realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations)
{
    for (auto Reservation = Reservations.begin(); Reservation != Reservations.end(); Reservation++)
    {
        if ((*Reservation)[0] == args[4])
        {
            for (int i = 0; i < 4; i++)
            {
                (*Reservation)[i] = args[i];
            }
        }
    }
}

ViewAllReservations::ViewAllReservations()
{
    info = "view all Reservation(enter: view)";
    tag = "view";
}

std::vector<std::string> ViewAllReservations::menu_function()
{
    // std::string name = read_from_command_line("the Reservation's name your want to modify");
    std::string name = "view";
    return {name};
}

void ViewAllReservations::realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations)
{
    // std::cout << "name: " << Reservations[0][0] << std::endl;
    for (auto Reservation = Reservations.begin(); Reservation != Reservations.end(); Reservation++)
    {
        std::cout << "name: " << (*Reservation)[0] << " password: " << (*Reservation)[1] << " number: " << (*Reservation)[2] << " identity: " << (*Reservation)[3] << std::endl;
    }
}
// // 定义 FindReservation 类，查找某个成员的信息功能
// class FindReservation : public StudentAbstractModule
// {
// public:
//     FindReservation();

//     // 实现菜单功能
//     std::vector<std::string> menu_function() override;

//     // 实现具体的查找某个成员信息逻辑
//     void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations);
// };
