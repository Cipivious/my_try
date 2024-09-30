#include "new_module.hpp"
#include <vector>
#include <string>
#include "main_page.h"
#include "administrator_page.h"
#include "student_page.h"

MainManager::MainManager(std::vector<MainAbstractModule *> modules)
{
    this->modules = modules;
    this->tag = 1;
}
MainManager::~MainManager()
{
}

void MainManager::work(std::string choice)
{
    for (int i = 0; i < modules.size(); i++)
    {
        if (modules[i]->worker(choice, tag))
        {
            break;
        }
    }
}

WentToStudentPage::WentToStudentPage()
{
    info = "enter to student's page(enter: student)";
    tag = "student";
}

std::vector<std::string> WentToStudentPage::menu_function()
{
    std::string name = "";
    return {name};
}

void WentToStudentPage::realize(std::vector<std::string> &args, int &tag)
{
    // std::cout << "hello welcome to add a person" << std::endl;
    std::cout << "this is main program" << std::endl;
    std::vector<StudentAbstractModule *> modules = {
        new ViewAllReservations,
        new AddReservation,
        new RemoveReservation,
        new ModifyReservation,
    };
    StudentManager manager(modules);
    manager.start();
}

WentToAdministratorPage::WentToAdministratorPage()
{
    info = "enter to adminstrator's page(enter: admin)";
    tag = "admin";
}

std::vector<std::string> WentToAdministratorPage::menu_function()
{
    std::string name = "";
    return {name};
}

void WentToAdministratorPage::realize(std::vector<std::string> &args, int &tag)
{
    // std::cout << "hello welcome to add a person" << std::endl;
    std::cout << "this is main program" << std::endl;
    std::vector<AdministratorAbstractModule *> modules = {
        new ViewAllPersons,
        new AddPerson,
        new RemovePerson,
        new ModifyPerson,
    };
    AdministratorManager manager(modules);
    manager.start();
}
