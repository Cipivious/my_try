#include <vector>
#include <string>

class Person
{
public:
    enum class Role
    {
        Admin = 0,
        Teacher = 1,
        Student = 2
    };
    Role role;
    int serial_number;
    std::string name;
    std::string password;
};

class Administrator : public Person
{
public:
    std::vector<std::vector<std::string>> personnel_information;
    Administrator(int serial, const std::string &admin_name, const std::string &admin_password);
    std::vector<std::vector<std::string>> get_personnel_information(std::string file_name = "personnel_information.txt");
    void write_personnel_information();
};