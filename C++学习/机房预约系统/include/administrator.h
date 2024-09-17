#pragma once
#include "new_module.h"
#include <vector>
#include <string>

// 定义管理员抽象模块，存储人员信息
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

    // 实现具体的添加成员逻辑
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
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons) override;
};

// 定义 ModifyPerson 类，修改成员信息功能
class ModifyPerson : public AdministratorAbstractModule
{
public:
    ModifyPerson();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的修改成员信息逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons) override;
};

// 定义 ViewAllPersons 类，查看所有成员信息功能
class ViewAllPersons : public AdministratorAbstractModule
{
public:
    ViewAllPersons();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的查看所有成员信息逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons) override;
};

// 定义 FindPerson 类，查找某个成员的信息功能
class FindPerson : public AdministratorAbstractModule
{
public:
    FindPerson();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的查找某个成员信息逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &persons) override;
};
