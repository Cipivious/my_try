#include "administrator.h"
#include "manager.h"

class AdministratorManager : public Manager
{
public:
    std::vector<std::vector<std::string>> persons;
    void read_from_file() = 0;
    void write_into_file() = 0;
    void work(std::string choice) = 0;
};
