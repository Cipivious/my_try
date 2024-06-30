# Windows环境配置

## [mingw](https://blog.csdn.net/qq_40410597/article/details/122474487)

在下载过程出现很多问题，主要是不了解，下载exe文件结果执行不了，源文件找不到bin，最后只好下载7z文件。

## [miniconda](https://docs.anaconda.com/miniconda/)

### 下载

在这个界面下载miniconda

### 添加环境变量

[anaconda安装目录下的Scripts文件夹中有conda等程序](https://www.py.cn/tools/anaconda/19876.html)

## 管理员权限

我想要给所有的应用管理员权限，但是用Windows11组策略打不开，于是放弃

## 删除软件

[找到所有的软件](https://jingyan.baidu.com/article/c33e3f48f38c2dea14cbb57f.html)

到设置里面删除

## [cmd.exe 的命令行启动参数](https://blog.csdn.net/WPwalter/article/details/94128623)

有一些程序不支持被直接启动，而要求通过命令行启动。这个时候，你就需要使用 cmd.exe 来启动这样的程序。我们都知道如何在 cmd.exe 中启动一个程序，但是当你需要自动启动这个程序的时候，你就需要知道如何通过 cmd.exe 来启动一个程序，而不是手工输入然后回车运行了。

## [注册表](https://blog.csdn.net/weixin_45300266/article/details/122359920)

注册表是一个强大的工具，可以用来自动执行一些任务

注册表是Windows操作系统中的一个重要组成部分，用于存储和管理系统和应用程序的配置信息、用户设置、硬件配置等数据。它以一种层次化的树状结构组织数据，类似于文件系统中的文件夹和文件，但它不是一个真正的文件系统，而是一个数据库。

### 结构和组织

注册表分为几个主要的顶级键（Hives），每个顶级键包含特定类型的配置信息：

1. **HKEY_CLASSES_ROOT (HKCR)**：包含文件扩展名与文件类型关联的信息，以及COM组件的注册信息。

2. **HKEY_CURRENT_USER (HKCU)**：包含当前用户的配置信息，包括桌面、环境变量、网络连接等。

3. **HKEY_LOCAL_MACHINE (HKLM)**：包含计算机的全局配置信息，包括硬件配置、安装的软件信息等。

4. **HKEY_USERS (HKU)**：包含所有用户的配置信息，每个用户有一个对应的子键。

5. **HKEY_CURRENT_CONFIG (HKCC)**：包含计算机的当前硬件配置信息，通常是动态生成的。

### 数据单元

注册表中的数据单元主要有三种类型：

- **键 (Key)**：类似于文件夹，用于组织和存储数据。键可以包含子键和值。
  
- **值 (Value)**：类似于文件，存储具体的数据。每个键可以包含多个值。

- **数据类型**：值可以有不同的数据类型，如字符串、整数、二进制数据等，这取决于存储的数据内容。

### 原理和作用

注册表的主要作用包括但不限于以下几个方面：

1. **配置管理**：存储和管理系统和应用程序的配置信息，包括用户界面设置、安全选项、网络配置等。

2. **软件安装**：在安装软件时，注册表被用来记录安装的路径、版本信息、文件关联等。

3. **系统状态维护**：记录系统的硬件配置、设备驱动、系统服务等。

4. **用户配置**：每个用户的个性化设置、环境变量、桌面背景等都可以在注册表中找到。

### 访问和修改

访问注册表可以通过注册表编辑器（如 `regedit.exe`）进行，也可以通过编程接口（如 Windows API 或 PowerShell）来实现。修改注册表需要管理员权限，并且需要小心操作，因为错误的修改可能导致系统不稳定或不可预测的行为。

### 总结

注册表是Windows操作系统中的核心配置存储机制，它以层次化、键值对的方式组织和存储各种系统和应用程序的配置信息。正确理解和管理注册表对于系统稳定性和应用程序正常运行至关重要，因此在修改注册表时务必小心谨慎，最好提前备份以防万一。

## 自动执行任务

在注册表中实现自动执行任务通常涉及到创建一个特定类型的注册表项或值，使得系统在某些事件发生时能够自动执行相关的任务或命令。这些任务可以是启动应用程序、运行脚本、设置环境变量等。以下是几种常见的在注册表中实现自动执行任务的方法：

###  启动项（AutoStart）

通过在注册表中设置启动项，可以让系统在用户登录时或计算机启动时自动执行相关的任务或程序。这通常用于设置自动启动的应用程序。

- **当前用户启动项**：
  - 路径：`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
  - 在这个位置下创建一个字符串值，命名为你想要启动的程序或任务，值设置为程序的路径或命令。

- **所有用户启动项**：
  - 路径：`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
  - 同样，在这个位置下创建一个字符串值，指定要自动启动的程序或任务。

例如，在 `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` 中创建一个名为 `MyApp` 的字符串值，其值设置为 `C:\Path\To\MyApp.exe`，这样每次用户登录时 `MyApp` 就会自动启动。

###  注册表中的计划任务

可以通过注册表设置来创建和管理 Windows 的计划任务，让系统在特定时间或事件发生时执行任务。

- **计划任务路径**：
  - `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree`

- 在这个路径下创建子键和值来定义计划任务的详细信息，例如任务名称、触发器、执行路径等。这种方式比较复杂，推荐使用 Windows 提供的任务计划程序界面（Task Scheduler）来创建和管理计划任务，它提供了更直观的界面和更多的配置选项。

### 注册表中的服务

服务是在系统后台运行的应用程序，可以通过注册表中的相关项来配置服务的启动和执行。

- **服务路径**：
  - `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services`

- 在这个路径下创建或修改相关的子键和值来配置服务的启动类型、依赖项等。这需要特别的权限和对服务的深入了解，不推荐直接修改注册表来配置服务，建议使用服务管理器（services.msc）或 PowerShell 等工具。

### 注意事项

- **备份注册表**：在修改注册表之前，务必备份当前的注册表状态，以防操作失误导致系统问题。
- **权限**：修改注册表需要管理员权限。
- **谨慎操作**：注册表是系统关键的配置存储机制，不正确的修改可能导致系统不稳定甚至无法启动。

总之，虽然可以通过注册表来实现自动执行任务，但对于大部分任务，Windows 提供了更安全和方便的界面和工具（如任务计划程序），推荐优先使用这些工具来管理任务和自动化操作。

## [git](https://git-scm.com/download/win)

git是一个强大的版本控制系统，可以借助它同步内容，下载东西。

## mysql

[mysql在安装时遇到的问题，电脑名称为中文字符或者含有空格，要把之前的删除掉然后重命名电脑，再重新安装。](https://blog.csdn.net/weixin_61635597/article/details/124332866)

```bash
gcc -o library Book.cpp BorrowRecord.cpp DBUtil.cpp main.cpp Manager.cpp Student.cpp TimeUtil.cpp User.cpp -IC:/Program\ Files/MySQL/MySQL\ Server\ 8.0/include -LC:/Program\ Files/MySQL/MySQL\ Server\ 8.0/lib -lmysqlclient
```

## windows管理员账户

Windows设置管理员账户启动的时候，有诸多的方便，可以从网上搜索具体的方法。

管理员账户启动，安装之类的操作不需要再经过确认操作，比较简便。

在安装应用的时候要注意是给一个用户安装，还是给所有的用户安装。

## 修改键盘映射

Windows修改键盘映射本质是修改注册表来实现的，[也可以通过安装sharpkey软件来简化这个过程](https://github.com/randyrants/sharpkeys?tab=readme-ov-file)。

## vscode

### 安装

vscode在安装的时候区分普通用户和系统用户，分别是两个不同的版本，[参见该网页](https://code.visualstudio.com/Download)

