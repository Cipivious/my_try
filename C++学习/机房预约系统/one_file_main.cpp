#include <string>
#include <vector>
#include <iostream>
#include <fstream> // 包含 ifstream 的头文件
#include <sstream> // 包含 std::stringstream 的头文件
// 定义 AbstractModule 类模板
template <typename... Args>
class AbstractModule
{
public:
    std::string info;
    std::string tag;

    // 纯虚函数，子类必须实现
    virtual std::vector<std::string> menu_function() = 0;

    // realize 函数模板：用于接收不定数量的左值引用
    virtual void realize(std::vector<std::string> &args, Args &...custom_classes) = 0;

    // worker 函数模板：接收不定数量的左值引用
    bool worker(const std::string &choice, Args &...custom_classes);

    static std::string read_from_command_line(const std::string &prompt);
};

// worker 函数的实现
template <typename... Args>
bool AbstractModule<Args...>::worker(const std::string &choice, Args &...custom_classes)
{
    if (choice != tag)
    {
        return false;
    }

    // 调用 menu_function 生成参数 args
    std::vector<std::string> args = menu_function();

    // 将不定数量的左值引用参数传递给 realize
    realize(args, custom_classes...);

    return true;
}

template <typename... Args>
std::string AbstractModule<Args...>::read_from_command_line(const std::string &prompt)
{
    std::cout << "Please enter " << prompt << ": ";
    std::string result;
    std::getline(std::cin, result);
    std::cout << "OK, your entered \"" << result << "\" has been recorded." << std::endl;
    return result;
}

template <typename T>
class Manager
{
public:
    std::vector<T *> modules;
    std::string num, name, password;
    Manager() {};
    Manager(std::vector<T *> modules);
    ~Manager();
    virtual void read_from_file() = 0;
    virtual void write_into_file() {};
    void set_user_information(std::string num, std::string name, std::string password);
    void show_menu();
    virtual void work(std::string choice) = 0;
    void start();
};

class CSVHandler
{
public:
    // 读取 CSV 文件，返回一个二维字符串向量
    static std::vector<std::vector<std::string>> readCSV(const std::string &filename);

    // 写入数据到 CSV 文件，接收一个二维字符串向量
    static void writeCSV(const std::string &filename, const std::vector<std::vector<std::string>> &data);
};
class AdministratorAbstractModule : public AbstractModule<std::vector<std::vector<std::string>>>
{
};

// 定义 AddPerson 类，添加成员功能
class AddPerson : public AdministratorAbstractModule
{
public:
    AddPerson();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons) override;
};

class AdministratorManager : public Manager<AdministratorAbstractModule>
{
public:
    std::vector<std::vector<std::string>> persons;
    AdministratorManager(std::vector<AdministratorAbstractModule *> modules)
    {
        this->modules = modules;
        read_from_file();
    }
    ~AdministratorManager()
    {
        write_into_file();
    }
    void read_from_file();
    void write_into_file();
    void work(std::string choice);
};

AddPerson::AddPerson()
{
    info = "add a person(enter: add)";
    tag = "add";
}

std::vector<std::string> AddPerson::menu_function()
{
    std::string name = read_from_command_line("please enter person's name: ");
    std::string password = read_from_command_line("please enter person's password: ");
    std::string number = read_from_command_line("please enter person's number: ");
    return {name, password, number};
}

void AddPerson::realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons)
{
    persons.push_back(args);
}

// 读取 CSV 文件的实现
std::vector<std::vector<std::string>> CSVHandler::readCSV(const std::string &filename)
{
    std::ifstream file(filename);
    if (!file.is_open())
    {
        throw std::runtime_error("Could not open file");
    }

    std::vector<std::vector<std::string>> data;
    std::string line, cell;

    while (std::getline(file, line))
    {
        std::stringstream lineStream(line);
        std::vector<std::string> row;

        while (std::getline(lineStream, cell, ','))
        {
            row.push_back(cell);
        }

        data.push_back(row);
    }

    file.close();
    return data;
}

// 写入 CSV 文件的实现
void CSVHandler::writeCSV(const std::string &filename, const std::vector<std::vector<std::string>> &data)
{
    std::ofstream file(filename);
    if (!file.is_open())
    {
        throw std::runtime_error("Could not open file");
    }

    for (const auto &row : data)
    {
        for (size_t i = 0; i < row.size(); ++i)
        {
            file << row[i];
            if (i != row.size() - 1)
            {
                file << ",";
            }
        }
        file << "\n";
    }

    file.close();
}

void AdministratorManager::read_from_file()
{
    try
    {
        std::vector<std::vector<std::string>> persons = CSVHandler::readCSV("person_information.csv");
        std::cout << "Data read from CSV file:" << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error reading CSV: " << e.what() << std::endl;
    }
}

void AdministratorManager::write_into_file()
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
template <typename T>
Manager<T>::Manager(std::vector<T *> modules)
{
    this->modules = modules;
    read_from_file();
}

template <typename T>
Manager<T>::~Manager()
{
    std::cout << "Welcome to ~Manager()" << std::endl;
    write_into_file();
}

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
int main()
{
    std::cout << "this is main program" << std::endl;
    std::vector<AdministratorAbstractModule *> modules = {
        new AddPerson,
    };
    AdministratorManager manager(modules);
    manager.start();
    return 0;
}