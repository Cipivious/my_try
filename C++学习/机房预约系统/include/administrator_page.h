#pragma once
#include "new_module.hpp"
#include <vector>
#include <string>
#include "manager.hpp"
#include "new_module.hpp"
#include "CSVHandler.h"

// #include "any"

// 定义管理员抽象模块，存储人员信息
class AdministratorAbstractModule : public AbstractModule<std::vector<std::vector<std::string>>>
{
};

class AdministratorManager : public Manager<AdministratorAbstractModule>
{
public:
    std::vector<std::vector<std::string>> persons;
    AdministratorManager(std::vector<AdministratorAbstractModule *> modules);
    ~AdministratorManager();
    void read_from_file();
    void write_into_file();
    void work(std::string choice);
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

// 定义 RemovePerson 类，删除成员功能
class RemovePerson : public AdministratorAbstractModule
{
public:
    RemovePerson();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的删除成员逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons);
};

// 定义 ModifyPerson 类，修改成员信息功能
class ModifyPerson : public AdministratorAbstractModule
{
public:
    ModifyPerson();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的修改成员信息逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons);
};

// 定义 ViewAllPersons 类，查看所有成员信息功能
class ViewAllPersons : public AdministratorAbstractModule
{
public:
    ViewAllPersons();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的查看所有成员信息逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons);
};

// 定义 FindPerson 类，查找某个成员的信息功能
class FindPerson : public AdministratorAbstractModule
{
public:
    FindPerson();

    // 实现菜单功能
    std::vector<std::string> menu_function();

    // 实现具体的查找某个成员信息逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons);
};
