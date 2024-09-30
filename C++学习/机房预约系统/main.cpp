#include "CSVHandler.h"
#include "new_module.hpp"
#include "manager.hpp"
#include "administrator_page.h"
#include <iostream>
#include "main_page.h"
#include "student_page.h"

int main()
{
    std::cout << "this is main program" << std::endl;
    std::vector<MainAbstractModule *> modules = {
        new WentToStudentPage,
        new WentToAdministratorPage,
    };
    MainManager manager(modules);
    manager.start();
    return 0;
}