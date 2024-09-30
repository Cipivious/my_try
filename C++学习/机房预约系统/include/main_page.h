#pragma once
#include "new_module.hpp"
#include <vector>
#include <string>
#include "manager.hpp"
#include "new_module.hpp"
#include "CSVHandler.h"

// #include "any"

// 定义管理员抽象模块，存储人员信息
class MainAbstractModule : public AbstractModule<int>
{
};

class MainManager : public Manager<MainAbstractModule>
{
public:
    int tag;
    MainManager(std::vector<MainAbstractModule *> modules);
    ~MainManager();
    void read_from_file();
    void write_into_file();
    void work(std::string choice);
};

// 定义 AddPerson 类，添加成员功能
class WentToStudentPage : public MainAbstractModule
{
public:
    WentToStudentPage();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    void realize(std::vector<std::string> &args, int &tag) override;
};

// 定义 RemovePerson 类，删除成员功能
class WentToAdministratorPage : public MainAbstractModule
{
public:
    WentToAdministratorPage();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的删除成员逻辑
    void realize(std::vector<std::string> &args, int &tag);
};
