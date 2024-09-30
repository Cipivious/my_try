#pragma once
#include "new_module.hpp"
#include <vector>
#include <string>
#include "manager.hpp"
#include "new_module.hpp"
#include "CSVHandler.h"

// #include "any"

// 定义管理员抽象模块，存储人员信息
class StudentAbstractModule : public AbstractModule<std::vector<std::vector<std::string>>>
{
};

class StudentManager : public Manager<StudentAbstractModule>
{
public:
    std::vector<std::vector<std::string>> Reservations;
    StudentManager(std::vector<StudentAbstractModule *> modules);
    ~StudentManager();
    void read_from_file();
    void write_into_file();
    void work(std::string choice);
};

// 定义 AddReservation 类，添加成员功能
class AddReservation : public StudentAbstractModule
{
public:
    AddReservation();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations) override;
};

// 定义 RemoveReservation 类，删除成员功能
class RemoveReservation : public StudentAbstractModule
{
public:
    RemoveReservation();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的删除成员逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations);
};

// 定义 ModifyReservation 类，修改成员信息功能
class ModifyReservation : public StudentAbstractModule
{
public:
    ModifyReservation();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的修改成员信息逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations);
};

// 定义 ViewAllReservations 类，查看所有成员信息功能
class ViewAllReservations : public StudentAbstractModule
{
public:
    ViewAllReservations();

    // 实现菜单功能
    std::vector<std::string> menu_function() override;

    // 实现具体的查看所有成员信息逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations);
};

// 定义 FindReservation 类，查找某个成员的信息功能
class FindReservation : public StudentAbstractModule
{
public:
    FindReservation();

    // 实现菜单功能
    std::vector<std::string> menu_function();

    // 实现具体的查找某个成员信息逻辑
    void realize(std::vector<std::string> &args, std::vector<std::vector<std::string>> &Reservations);
};
