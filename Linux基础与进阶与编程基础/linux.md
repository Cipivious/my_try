# linux

## 解决问题的思路

1. 从笔记中查找有没有解决方法
   1. 方法类的内容 从日常笔记中查找
   2. 解释类的内容 从 recoll 中查找
   3. 文档类的内容 从 zeal 中查找
2. 寻找合适的工具（询问 ChatGPT）
3. 查找工具的用法（**tldr**，**man（--help）** ，**官方文档**）
4. 调试使用工具解决问题

## strace

要检测使用 `gsettings` 命令后哪些文件立刻发生了修改，可以使用以下方法来追踪文件系统中的变化：

### 使用 `strace` 工具

`strace` 是一个 Linux 下的系统调用跟踪工具，可以帮助捕获并分析进程的系统调用。你可以使用 `strace` 跟踪 `gsettings` 命令执行时所涉及到的文件操作。

1. **安装 `strace`**

   ```bash
   sudo apt install strace   # 如果你的系统是基于 Debian/Ubuntu 的
   ```

2. **跟踪 `gsettings` 命令**
   使用以下命令结构来跟踪 `gsettings` 命令的文件系统操作：

   ```bash
   strace -e trace=file gsettings set <schema> <key> <value>
   ```

   - `<schema>`：设置的 schema（如 `org.gnome.desktop.interface`）
   - `<key>`：具体的设置键（如 `gtk-theme`）
   - `<value>`：设置的值（如 `'Adwaita-dark'`）

   例如：

   ```bash
   strace -e trace=file gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
   ```

3. **分析输出**
   `strace` 会输出 `gsettings` 命令执行过程中涉及的文件操作。你可以检查输出来看哪些文件被修改或访问了。

### 示例输出

运行 `strace` 命令后，会看到类似以下的输出：

```
openat(AT_FDCWD, "/usr/share/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/usr/share/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/usr/share/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml", O_RDONLY|O_CLOEXEC) = 3
...
```

这些是 `gsettings` 命令执行时打开的文件。你可以分析这些输出来了解 `gsettings` 所影响的文件和目录。

### 注意事项

- `strace` 会捕获每个系统调用，输出可能会很多。你可以通过 `-e` 参数来限制捕获的系统调用类型，以便更精确地检查文件操作。
- 修改的文件可能包括配置文件、数据库文件、缓存文件等。对于 `gsettings` 而言，主要影响的是 `dconf` 数据库中的内容，而不是直接修改文件。
- 修改 `dconf` 数据库文件本身（`~/.config/dconf/user`）的变化不太容易通过 `strace` 观察到，因为这是一个二进制格式的文件。

通过使用 `strace` 工具，你可以比较准确地追踪到 `gsettings` 命令执行时所涉及的文件操作，从而了解 `gsettings` 设置的实际影响。

## dconf（gnome 桌面的配置文件）

在 GNOME 桌面环境中，用户配置的主题设置会保存到 `dconf` 数据库中，而 `dconf` 数据库会存储在用户的主目录下的特定文件中。直接编辑这些文件并不推荐，因为它们是二进制文件且由 GNOME 的设置守护进程（`dconf`）管理的。

### **dconf 配置存储位置**

用户的 dconf 数据库文件通常存储在以下目录：

```
~/.config/dconf/user
```

这个文件是二进制文件，不适合直接编辑。建议使用 `gsettings` 或 `dconf` 命令行工具来修改配置。

备份到文件：

```
dconf dump / > dconf-backup.txt
```

从文件恢复：

```
dconf load / < dconf-backup.txt
```

## gsettings

在 GNOME 桌面环境中，`gsettings` 提供了大量配置选项来设置桌面属性。以下是一些常见的设置桌面属性的 `gsettings` 配置：

可以从`/home/yang/.config/glib-2.0/settings/keyfile`中查看具体的配置的修改，文件类似下面这样：

```yaml
[system/proxy]
mode='manual'

[system/proxy/http]
host='127.0.0.1'
port=7890

[system/proxy/https]
host='127.0.0.1'
port=7890

[system/proxy/socks]
host='127.0.0.1'
port=7891
```

### **桌面背景**

- **设置桌面背景图片**：

  ```bash
  gsettings set org.gnome.desktop.background picture-uri 'file:///path/to/your/image.jpg'
  ```

- **设置背景图片的模式（缩放、平铺、拉伸等）**：

  ```bash
  gsettings set org.gnome.desktop.background picture-options 'stretched'
  ```

### **锁屏背景**

- **设置锁屏背景图片**：

  ```bash
  gsettings set org.gnome.desktop.screensaver picture-uri 'file:///path/to/your/image.jpg'
  ```

### **图标大小**

- **设置桌面图标大小**：

  ```bash
  gsettings set org.gnome.nautilus.icon-view default-zoom-level 'standard'
  ```

### **图标排列**

- **设置桌面图标排列方式（按网格、手动）**：

  ```bash
  gsettings set org.gnome.nautilus.icon-view default-layout 'manual'
  ```

### **主题**

- **设置 GTK 主题**：

  ```bash
  gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
  ```

- **设置图标主题**：

  ```bash
  gsettings set org.gnome.desktop.interface icon-theme 'Papirus'
  ```

- **设置 Shell 主题**：

  ```bash
  gsettings set org.gnome.shell.extensions.user-theme name 'Adwaita-dark'
  ```

### **字体**

- **设置界面字体**：

  ```bash
  gsettings set org.gnome.desktop.interface font-name 'Cantarell 11'
  ```

- **设置文档字体**：

  ```bash
  gsettings set org.gnome.desktop.interface document-font-name 'Sans 11'
  ```

- **设置等宽字体**：

  ```bash
  gsettings set org.gnome.desktop.interface monospace-font-name 'Monospace 11'
  ```

### **鼠标和触控板**

- **设置光标主题**：

  ```bash
  gsettings set org.gnome.desktop.interface cursor-theme 'Adwaita'
  ```

- **设置鼠标加速度**：

  ```bash
  gsettings set org.gnome.desktop.peripherals.mouse speed 0.5
  ```

### **键盘**

- **设置键盘重复延迟**：

  ```bash
  gsettings set org.gnome.desktop.peripherals.keyboard delay 250
  ```

- **设置键盘重复速度**：

  ```bash
  gsettings set org.gnome.desktop.peripherals.keyboard repeat-interval 30
  ```

### **电源管理**

- **设置显示器关闭时间**：

  ```bash
  gsettings set org.gnome.desktop.session idle-delay 300
  ```

### **通知**

- **启用或禁用通知**：

  ```bash
  gsettings set org.gnome.desktop.notifications show-banners true
  ```

### **时间和日期**

- **显示日期在顶栏**：

  ```bash
  gsettings set org.gnome.desktop.interface clock-show-date true
  ```

### **窗口管理**

- **启用窗口悬停焦点**：

  ```bash
  gsettings set org.gnome.desktop.wm.preferences focus-mode 'sloppy'
  ```

- **启用按键焦点模式**：

  ```bash
  gsettings set org.gnome.desktop.wm.preferences focus-mode 'click'
  ```

### **屏幕亮度**

- **设置屏幕亮度**：

  ```bash
  gsettings set org.gnome.settings-daemon.plugins.power ambient-enabled false
  gsettings set org.gnome.settings-daemon.plugins.power brightness 75
  ```

### **屏幕边缘触发（热区）**

- **启用屏幕左上角触发活动概览**：

  ```bash
  gsettings set org.gnome.desktop.interface enable-hot-corners true
  ```

### **扩展**

- **启用特定扩展**：

  ```bash
  gsettings set org.gnome.shell enabled-extensions "['extension-name@example.com']"
  ```

这些是一些常见的桌面属性配置，您可以根据需要进行修改。如果需要更详细的信息，您可以使用 `gsettings list-schemas` 和 `gsettings list-keys` 来查看可用的设置和对应的键。例如：

```bash
gsettings list-schemas | grep gnome
gsettings list-keys org.gnome.desktop.background
```

这样可以查看具体的可用配置项和对应的设置键。

## pkg-config

Provide the details of installed libraries for compiling applications.
More information: https://www.freedesktop.org/wiki/Software/pkg-config/.

- Get the list of libraries and their dependencies:
  pkg-config --libs library1 library2 ...

- Get the list of libraries, their dependencies, and proper cflags for gcc:
  pkg-config --cflags --libs library1 library2 ...

- Compile your code with libgtk-3, libwebkit2gtk-4.0 and all their dependencies:
  c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example

## 日志清理

定期清理日志文件以防止它们占用过多磁盘空间是一个良好的系统管理实践。可以使用 `logrotate` 工具来自动管理和轮换日志文件。以下是配置 `logrotate` 来定期清理 NGINX 日志的步骤：

### 安装 logrotate

大多数 Linux 发行版默认安装了 `logrotate`。如果你的系统上没有安装，可以使用包管理器来安装：

- 在 Debian/Ubuntu 系统上：

  ```bash
  sudo apt-get install logrotate
  ```

- 在 CentOS/RHEL 系统上：

  ```bash
  sudo yum install logrotate
  ```

### 配置 logrotate

1. **创建或编辑 logrotate 配置文件**:

   通常情况下，`logrotate` 的配置文件位于 `/etc/logrotate.d/` 目录下。你可以为 NGINX 创建一个单独的配置文件，例如 `/etc/logrotate.d/nginx`。

2. **添加 logrotate 配置**:

   下面是一个示例配置文件，它每天轮换 NGINX 的日志文件，并且保留最近的 7 个日志文件：

   ```text
   /var/log/nginx/*.log {
       daily                   # 每日轮换日志
       missingok               # 如果日志文件丢失，则忽略错误
       rotate 7                # 保留最近 7 个轮换的日志文件
       compress                # 压缩轮换后的日志文件
       delaycompress           # 延迟一个轮换周期再压缩
       notifempty              # 如果日志文件为空，不进行轮换
       create 0640 nginx adm   # 使用指定的权限创建新的日志文件
       sharedscripts           # 运行脚本时，仅执行一次

       postrotate
           # 在每次日志轮换后，重新加载 NGINX，以使其开始写入新的日志文件
           [ -f /run/nginx.pid ] && kill -USR1 `cat /run/nginx.pid`
       endscript
   }
   ```

### 解释配置选项

- `daily`: 每天轮换一次日志文件。
- `missingok`: 如果日志文件不存在，则不会报错。
- `rotate 7`: 保留最近的 7 个日志文件，超过这个数量的旧日志将被删除。
- `compress`: 压缩轮换后的日志文件以节省磁盘空间。
- `delaycompress`: 延迟一个轮换周期后再压缩日志文件，这样最近的一个日志文件不会被压缩，便于调试。
- `notifempty`: 如果日志文件为空，则不轮换。
- `create 0640 nginx adm`: 使用指定的权限创建新的日志文件，并设置所属用户和组。
- `sharedscripts`: 确保脚本（例如 postrotate）在所有日志文件轮换完毕后只运行一次。
- `postrotate ... endscript`: 在日志轮换后执行的脚本。在这里，它向 NGINX 主进程发送 `USR1` 信号，通知 NGINX 重新打开日志文件。

### 手动测试 logrotate 配置

在正式启用之前，可以手动测试 `logrotate` 配置，以确保它按预期工作：

```bash
sudo logrotate -d /etc/logrotate.d/nginx
```

此命令会显示 `logrotate` 将执行的操作，但不会实际执行轮换。确保没有错误后，可以运行以下命令实际执行轮换：

```bash
sudo logrotate -f /etc/logrotate.d/nginx
```

### 定期执行 logrotate

在大多数 Linux 系统中，`logrotate` 是通过 `cron` 自动定期运行的。`cron` 会定期检查并执行 `/etc/cron.daily/logrotate` 脚本，从而确保日志文件按计划轮换。

通过以上配置和步骤，你可以确保 NGINX 的日志文件被定期清理和管理，从而避免日志文件占用过多的磁盘空间。

## man

### 使用小技巧

先使用`man -k . | grep "word"`来匹配想搜索的命令或者定义的位置，然后再到对应的地方区查找。就大多数时候而言，很多都是可以找到的，对很多 C 语言的标准库的函数，是一查一个准。

![image-20240528192306010](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240528192306010.png)

### 介绍

在 Unix 和 Linux 系统中，`man` 命令用于显示各种文档页面（manual pages）。这些文档页面按章节（sections）组织，每个章节包含不同类型的信息。章节的数字指定了文档的类别。以下是各个章节的含义：

1. **User Commands**: 用户命令（可执行程序或 shell 命令）
2. **System Calls**: 系统调用（由内核提供的函数）
3. **Library Functions**: 库函数（通常是 C 标准库函数）
4. **Special Files**: 特殊文件（通常是/dev 下的设备文件）
5. **File Formats and Conventions**: 文件格式和约定（例如/etc/passwd）
6. **Games and Screensavers**: 游戏和屏保
7. **Miscellaneous**: 杂项（包括宏包、常见约定等）
8. **System Administration Commands**: 系统管理命令和守护进程
9. **Kernel Routines**: 内核例程（特定于内核的函数）

## 统计一个文件夹下的文件的总行数

```py
import os

def count_lines_in_folder(folder_path):
    total_lines = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    total_lines += len(lines)
    return total_lines

folder_path = '/home/yang/Downloads/nginx-1.0.15/src/'
total_lines = count_lines_in_folder(folder_path)
print("Total lines in folder:", total_lines)
```

## diff 工具

[用 MoonBit 实现 diff](https://zhuanlan.zhihu.com/p/699218281)

它是一个比对两个文本文件之间有什么不同之处的工具

## 文件的详细信息

(base) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:/var/www/html$ stat ch01/final/aliens/report.php
文件：ch01/final/aliens/report.php
大小：1662 块：8 IO 块大小：4096 普通文件
设备：259,5 Inode: 9967384 硬链接：1
权限：(0777/-rwxrwxrwx) Uid: ( 1000/ yang) Gid: ( 1000/ yang)
访问时间：2024-05-13 15:40:50.310284845 +0800
修改时间：2024-05-10 21:15:36.457368163 +0800
变更时间：2024-05-12 16:52:21.409318555 +0800
创建时间：2024-05-10 21:15:36.457368163 +0800

## find 的进阶用法

`find` 命令是一个非常强大的工具，用于在目录中搜索文件和目录。你可以结合 `-exec` 选项来对找到的每个文件或目录执行特定的命令。以下是 `find` 命令的一些常见用法以及如何使用 `-exec` 选项的更一般的方法：

### 一般用法

#### 查找特定名称的文件

```
find /path/to/search -name "filename"
```

例如，查找当前目录及其子目录中所有名为 `example.txt` 的文件：

```
find . -name "example.txt"
```

#### 查找特定模式的文件

```
find /path/to/search -name "*.txt"
```

例如，查找当前目录及其子目录中所有 `.txt` 文件：

```
find . -name "*.txt"
```

#### 查找特定大小的文件

```
find /path/to/search -size +10M
```

例如，查找当前目录及其子目录中所有大于 10MB 的文件：

```
find . -size +10M
```

#### 查找特定时间修改的文件

```
find /path/to/search -mtime -7
```

例如，查找当前目录及其子目录中所有 7 天内修改过的文件：

```
find . -mtime -7
```

### 使用 `-exec` 执行命令

#### 删除找到的文件

```
find /path/to/search -name "filename" -exec rm {} \;
```

例如，删除当前目录及其子目录中所有名为 `example.txt` 的文件：

```
find . -name "example.txt" -exec rm {} \;
```

#### 移动找到的文件

```
find /path/to/search -name "*.txt" -exec mv {} /new/path/ \;
```

例如，移动当前目录及其子目录中所有 `.txt` 文件到 `/new/path/` 目录：

```
find . -name "*.txt" -exec mv {} /new/path/ \;
```

#### 列出找到的文件的详细信息

```
find /path/to/search -name "*.txt" -exec ls -l {} \;
```

例如，列出当前目录及其子目录中所有 `.txt` 文件的详细信息：

```
find . -name "*.txt" -exec ls -l {} \;
```

#### 压缩找到的文件

```
find /path/to/search -name "*.log" -exec gzip {} \;
```

例如，压缩当前目录及其子目录中所有 `.log` 文件：

```
find . -name "*.log" -exec gzip {} \;
```

### 一般的 `find` 命令语法

```
find /path/to/search [options] [conditions] [-exec command {} \;]
```

- `/path/to/search`：指定要搜索的目录。
- `[options]`：可选项，例如 `-type f` 查找文件，`-type d` 查找目录。

## 查看字体路径的方法

1. **使用 `fc-list` 命令**：这个命令可以列出系统中安装的所有字体及其路径。运行以下命令：

   ```
   fc-list | grep -i "regular"
   ```

   这将列出所有具有 "regular" 属性的字体及其完整路径。

2. **查看常见字体目录**：Linux 系统中的字体通常安装在以下目录之一：

   - `/usr/share/fonts/`
   - `~/.fonts/` (当前用户的本地字体)

   您可以使用 `ls` 或 `find` 命令来查看这些目录中的字体文件。

3. **使用 `locate` 命令**：如果您的系统中安装了 `locate` 命令，可以使用它来快速搜索字体文件：

   ```
   locate ttf
   ```

   这将列出所有以 `ttf` 结尾的文件，即 TrueType 字体文件。

## pdf 工具

pdftk file1.pdf file2.pdf cat output output.pdf

这个工具可以用于合并 pdf 文件

## trash

`sudo apt install trash-cli`

1. **trash**: 这个命令用于将文件或目录移动到垃圾桶中。您可以使用它来代替 `rm` 命令，以便删除文件时将其移动到垃圾桶而不是永久删除。例如：

   ```bash
   trash filename
   ```

2. **trash-empty**: 此命令用于清空垃圾桶，永久删除其中的所有文件。如果您确定不需要恢复任何已删除的文件，可以使用此命令来释放磁盘空间。例如：

   ```bash
   trash-empty
   ```

3. **trash-list**: 这个命令用于列出垃圾桶中的所有文件。这对于查看之前删除的文件，并决定是否恢复它们很有帮助。例如：

   ```bash
   trash-list
   ```

4. **trash-put**: 此命令用于将文件或目录移动到垃圾桶中，与 `trash` 命令类似，但它接受文件路径作为参数。例如：

   ```bash
   trash-put /path/to/file
   ```

5. **trash-restore**: 这个命令用于从垃圾桶中还原文件或目录。您可以使用此命令将先前删除的文件恢复到原来的位置。例如：

   ```bash
   trash-restore filename
   ```

6. **trash-rm**: 此命令与 `trash` 类似，用于将文件或目录移动到垃圾桶中，但是它更接近 `rm` 命令的用法。例如：

   ```bash
   trash-rm filename
   ```

## while 循环

```bash
(base) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:~/ebooks/physics/convert$ while true;do
> ls | grep "pdf" | tail -n 1
> sleep 5
> done
 #这是一个用于检测任务执行情况的工具，间隔五秒执行一次
```

## 防火墙策略

当使用 UFW 时，您可以使用以下命令来配置和管理防火墙规则：

1. **启用/禁用 UFW**：

   - 启用 UFW：`sudo ufw enable`
   - 禁用 UFW：`sudo ufw disable`

2. **查看当前防火墙状态**：

   - `sudo ufw status`：显示当前防火墙规则的状态和开启/关闭状态。

3. **添加/删除规则**：

   - 添加规则：`sudo ufw allow <port>/<protocol>`：允许指定端口和协议的传入连接。
   - 删除规则：`sudo ufw delete allow <port>/<protocol>`：删除指定端口和协议的传入连接规则。

4. **指定来源 IP 地址**：

   - 允许特定 IP 地址：`sudo ufw allow from <IP>`：允许特定 IP 地址的连接。
   - 禁止特定 IP 地址：`sudo ufw deny from <IP>`：禁止特定 IP 地址的连接。

5. **指定应用程序**：

   - 允许应用程序：`sudo ufw allow <app>`：允许指定的应用程序通过防火墙。
   - 禁止应用程序：`sudo ufw deny <app>`：禁止指定的应用程序通过防火墙。

6. **指定端口范围**：

   - 允许端口范围：`sudo ufw allow <start_port>:<end_port>/<protocol>`：允许指定端口范围和协议的连接。
   - 禁止端口范围：`sudo ufw deny <start_port>:<end_port>/<protocol>`：禁止指定端口范围和协议的连接。

7. **指定传输方向**：

   - 允许出站连接：`sudo ufw allow out <port>/<protocol>`：允许指定端口和协议的出站连接。
   - 禁止出站连接：`sudo ufw deny out <port>/<protocol>`：禁止指定端口和协议的出站连接。

8. **查看已定义的规则**：

   - `sudo ufw status numbered`：按编号列出所有已定义的规则。

这些是 UFW 的基本用法。您可以根据需要使用这些命令来配置您的防火墙规则。

## 查询自己的 ip

### 公网 ip 地址

`curl ifconfig.me`

### ifconfig 查询结果分析

```bash
接口名称 (wlp0s20f3)： 这是网络接口的名称。在 Linux 中，网络接口通常以类似 eth0、wlan0 或者像这里的 wlp0s20f3 这样的形式命名。
标志 (flags)： 这是描述网络接口当前状态的标志。在这种情况下，UP 表示接口已启用，BROADCAST 表示接口支持广播通信，RUNNING 表示接口正在运行，MULTICAST 表示接口支持多播通信。
MTU (mtu)： MTU（最大传输单元）是网络接口可以传输的数据包的最大大小。在这里，MTU 为 1500 字节。
IP 地址 (inet)： 这是网络接口的 IPv4 地址。在这个例子中，IP 地址是 10.166.83.73。
子网掩码 (netmask)： 子网掩码定义了网络中主机的范围。它指示哪些 IP 地址属于同一网络。在这里，子网掩码是 255.254.0.0。
广播地址 (broadcast)： 这是广播地址，用于在网络上发送广播消息。在这里，广播地址是 10.167.255.255。
IPv6 地址 (inet6)： 这是网络接口的 IPv6 地址。在这个例子中，IPv6 地址是 fe80::1ee0:5ed9:9489:881c。
MAC 地址 (ether)： 这是网络接口的物理地址，也称为 MAC 地址。在这里，MAC 地址是 68:3e:26:0e:6e:74。
传输队列长度 (txqueuelen)： 这是网络接口发送队列的长度。
接收数据包数量 (RX packets) 和发送数据包数量 (TX packets)： 这些是网络接口接收和发送的数据包数量。
```

## 创建桌面图标

### 生成 icon 图片大小 256\*256px

![制作icon图片](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240510101324359.png)

![image-20240711134930218](https://raw.githubusercontent.com/Cipivious/my_try/main/img/image-20240711134930218.png)

### 撰写`.desktop`文件

```bash
(base) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:/usr/share/applications$ cat upload.desktop
[Desktop Entry]
Type=Application
Name=upload-resource
Comment=Run the Typora script located in ~/typora/
AllowExecutables=true
Exec=/bin/bash -c "~/typora/run.sh"
Icon=https://raw.githubusercontent.com/Cipivious/my_try/main/upload.png
Terminal=false
Categories=Utility;
```

### 运行`update-desktop-database`重新加载桌面数据

### 建立符号链接显示到桌面

`ln -s /usr/share/applications/run-typora.desktop ~/Desktop/run-typora.desktop`

### 设置图标在桌面显示的位置

![显示位置](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240510102138583.png)

## 下载

### wget

wget 是一个在命令行下用来下载文件的工具，它支持断点续传功能。下面是一些 wget 命令的基本使用方法和断点续传的操作：

1. **基本使用方法**：

   ```
   wget [options] [URL]
   ```

   例如，要下载一个文件，你可以使用以下命令：

   ```
   wget http://example.com/file.zip
   ```

2. **断点续传**：

   要使用 wget 进行断点续传，你需要添加 `-c` 或 `--continue` 选项。当你重新下载一个已经存在的文件时，wget 会检查文件的大小和本地文件的大小，如果它们不同，wget 将会继续下载缺少的部分。

   ```
   wget -c http://example.com/file.zip
   ```

   如果下载过程中意外中断，你可以再次使用相同的命令来继续下载文件，wget 将会从上次中断的地方继续下载。

## sed

[sed 使用教程](https://www.runoob.com/linux/linux-comm-sed.html)

[sed 使用案例](file://https://raw.githubusercontent.com/Cipivious/my_try/main/mindmap.sh)

```bash
#!/bin/bash
cd https://raw.githubusercontent.com/Cipivious/my_try/main/
cp resources.md mindmap.md
# 输入文件路径
input_file="mindmap.md"

# 输出文件路径
output_file="mindmap.puml"

# 使用 grep 筛选以 # 开头的行，并保存到输出文件中
grep -E '^#{1,3} ' "$input_file"  > "$output_file"
# 在输出文件的首行前添加 @startmindmap
# 在输出文件的末尾添加 @endmindmap
sed -i '$a\@endmindmap' "$output_file"
sed -i 's/#/\*/g' "$output_file"
sed -i 's/^\*/\*\*/g' "$output_file"
sed -i '1i\* notebook' "$output_file"
sed -i '1i\@startmindmap' "$output_file"
echo "制作完成完成"

plantuml $output_file
silence mindmap.png
```

## 系统修复的方法

进入 recovery mode 里面的 root 输入命令来修复，这是最稳妥的方法。

## 输入

### 输入法

感觉 ubuntu24.04 里面输入法是一个很麻烦的事情，我还按照 sogou 官方给的教程安装输入法，但是出现了闪屏的问题，[我找到了一个之前的问题，但这个是 23.10 版本的，我尝试之后并没有解决问题](https://blog.csdn.net/hsyxxyg/article/details/137676045)，[然后从这里面找到了一个说法，说是搜狗输入法需要 fcitx5,然后我就把之前的 fcitx 卸载了，重新安装了 fcitx5,在语言支持那里作了切换，但这个时候又出现了新的问题，就是我再 dpkg -i sogou.deb 的时候，它说需要 fcitx，于是我又下回了之前的那个，反复几次都没有妥善的解决。](https://forum.ubuntu.com.cn/viewtopic.php?t=494350)目前官方还没有给从妥善的解决方法，我觉得最好的办法还是用 ubuntu 默认的 ibus 输入法，这个输入法一般不会有什么问题，[这是一个在命令行安装中文输入法的教程](https://juejin.cn/post/7274626136328552500)，当然也可以直接从右上角的 ibus 设置那里安装。如果新安装 ibus 的话（比如我之前把 ibus 卸载了然后安装的 fcitx），可能右上角不会出现 ibus 的配置图标，重启一下电脑就出现了。

## 设置默认窗口最大化

在 Ubuntu 中，你可以使用 CompizConfig 设置来实现窗口默认最大化的功能。以下是具体步骤：

1. **安装 CompizConfig 设置管理器**：如果你还没有安装 CompizConfig 设置管理器，请在终端中运行以下命令安装：

```
sudo apt update
sudo apt install compizconfig-settings-manager
```

1. **打开 CompizConfig 设置管理器**：打开终端，运行以下命令：

```
ccsm
```

1. **在 CompizConfig 设置管理器中找到窗口管理器**：在 CompizConfig 设置管理器的搜索框中搜索 "窗口管理器"，然后点击 "窗口管理器"。
2. **设置默认最大化**：在 "窗口管理器" 设置中，找到 "开始最大化" 选项，勾选它以启用窗口默认最大化。
3. **保存设置**：关闭 CompizConfig 设置管理器，你所做的更改应该已自动保存。

## 键盘映射

### [修改配置文件](https://blog.csdn.net/L141210113/article/details/106616629)

先用 xev 工具获取键位的 keycode 的值，然后到`/usr/share/X11/xkb/keycodes/evdev`这个文件作出修改。

### [xmodmap 工具](https://www.cnblogs.com/yinheyi/p/10146900.html)

首先也是通过 xev 工具获取 keycode 的值，然后写`.Xmodmap`文件。

### 配置 emacs 全局快捷键

我尝试过很多方法，以下是唯一一个成功的

[xkeysnail](https://github.com/mooz/xkeysnail?tab=readme-ov-file)

如果你没有使用 conda 环境的话，参考上面的教程就可以完成设置，如果你使用的话，可能会遇到一些小坑，可以往下看一下。

因为 xkeysnail 需要系统权限，必须用 sudo 才能启用，因此你必须有一个系统的 python 环境才可以。

1. 首先运行`sudo apt install python3-pip`安装 sudo 的 pip 环境
2. 这时候不可以直接运行`sudo pip3 install xkeysnail`,否则会产生下面的报错
3. 要运行`sudo /usr/bin/pip3 install xkeysnail --break-system-packages`这个才可以
4. [然后你把这个文件保存到本地的`~/config.py`](https://github.com/mooz/xkeysnail/blob/master/example/config.py),然后运行`sudo xkeysnail config.py`就可以了

![报错](https://raw.githubusercontent.com/Cipivious/my_try/main/image/截图 2024-05-07 10-36-20.png)

![成功](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240507104137409.png)

### 获得活动窗口信息

[xprop](#https://blog.csdn.net/qq_43287763/article/details/121461656)

xprop 实用程序用于在 X 服务器中显示窗口和字体属性。通过单击所需的窗口，使用命令行参数或可能在窗口的情况下选择一个窗口或字体。然后给出属性列表，可能带有格式化信息。

## ubuntu24.04 双系统重装教程

[附一个 archlinux 启动盘制作的安装教程](https://zhuanlan.zhihu.com/p/405352705?utm_id=0)

[这是一个安装 archlinux 的教程](https://juejin.cn/post/7224418285797965884)

[制作**Ubuntu 系统完整备份**](https://www.zhihu.com/question/66316139/answer/3486065028?utm_campaign=shareopn&utm_medium=social&utm_psn=1769729835855896576&utm_source=wechat_session)

### 刻录系统

### 进入 BIOS 模式使用 usb 启动

### 这里主要讲硬盘分区那里

由于我是双系统，所以在安装的的时候，就需要考虑在那里安装的问题

之前我的系统的硬盘划分是这样的

|     | 硬盘分区       | 内容                                   |
| --- | -------------- | -------------------------------------- |
| 1   | /dev/nvme0n1p1 | Windows Boot Manager                   |
| 2   | /dev/nvme0n1p2 | 这一块是 window 系统预留的区域，比较小 |
| 3   | /dev/nvme0n1p3 | 这一块是 Windows 文件系统的区域        |
| 4   | /dev/nvme0n1p4 | 这一块是 ubuntu20.04 的系统的区域      |

![_cgi-bin_mmwebwx-bin_webwxgetmsgimg__&MsgID=8414554967511900702&skey=@crypt_7118dab0_7ee78741ab70fd2a65acc7d332dbc230&mmweb_appid=wx_webfilehelper](https://raw.githubusercontent.com/Cipivious/my_try/main/image/_cgi-bin_mmwebwx-bin_webwxgetmsgimg__&MsgID=8414554967511900702&skey=@crypt_7118dab0_7ee78741ab70fd2a65acc7d332dbc230&mmweb_appid=wx_webfilehelper.jpeg)

这个是我配置好的一个界面

我是把之前的/dev/nvme0n1p4 先按 change 那里的“-”移除，然后它就变成了“freespace”，之后把光标移动到 freespace 的地方，然后点击下面的+号，就可以重新划分硬盘的区域了。

我计划了三块区域。第一块是启动区域，他必须在 nvme0n1p1，因为他在第一个块，不过你不要担心如果你这样会损害之前的 Windows 启动项，因为我这样做是成功的。第二块是交换内存，这块也可以不设置，不过我在这里设置了，它可以作为系统内存的扩展区域，在一定程度上可以提高性能。第三块是 Linux 文件系统的区域，它挂载系统的根目录。

### 其他的部分和安装其他系统的过程差不多，就不啰嗦了

### 下面是安装后的界面，大家可以参考一下

![image-20240501165637475](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240501165637475.png)

## 亮度条件

[亮度调节](https://blog.csdn.net/ftimes/article/details/119907899)

## ubuntu 包管理器

在 Ubuntu 中，软件包管理器会根据一定的优先级顺序来确定要从哪个软件源下载软件包。这个顺序通常如下所示（从高到低）：

1. **本地源（Local Sources）：** 本地源的软件包会优先于远程软件源进行安装。这包括已经从 CD/DVD 或 USB 驱动器加载的软件包以及通过本地网络共享提供的软件包。
2. **PPA（Personal Package Archives）：** 如果你已经添加了个人软件包存档（PPA），系统会优先考虑从这些源中下载软件包。
3. **主要软件源（Main Repositories）：** 官方 Ubuntu 软件源的主要部分，例如 `http://archive.ubuntu.com/ubuntu/`。
4. **更新软件源（Updates Repositories）：** 包含更新的软件包，通常位于 `http://archive.ubuntu.com/ubuntu/` 的 `-updates` 子目录。
5. **安全软件源（Security Repositories）：** 包含针对安全漏洞的修复程序的软件包，通常位于 `http://security.ubuntu.com/ubuntu/`。
6. **后备软件源（Backports Repositories）：** 包含从后续版本的 Ubuntu 中提取的软件包，通常位于 `http://archive.ubuntu.com/ubuntu/` 的 `-backports` 子目录。
7. **宇宙和多元宇宙软件源（Universe and Multiverse Repositories）：** 包含社区维护的软件包和非自由软件包的软件源。

### snap 商店

### dpkg （debain package manager）

dpkg --list

dpkg --remove

dpkg --purge

### apt（调用 dpkg 来完成）

添加源的方法

要向 `dpkg` 中添加软件包源，你需要编辑 `/etc/apt/sources.list` 文件或在 `/etc/apt/sources.list.d/` 目录中创建一个新的 `.list` 文件。以下是向 `dpkg` 添加源的一般步骤：

**编辑 `sources.list` 文件：**

打开终端并使用你喜欢的文本编辑器（如 `nano`、`vim` 或 `gedit`）编辑 `/etc/apt/sources.list` 文件。在文件中添加新源的行，格式如下：

Types: deb
URIs: http://mirrors.tuna.tsinghua.edu.cn/ubuntu/
Suites: noble
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

其中，`http://repository.example.com/ubuntu` 是软件包存储库的 URL，`distribution` 是发行版的代号（如 `bionic`、`focal`），`component1`, `component2` 等是软件包的组件（如 `main`, `contrib`, `non-free`）。

**添加 PPA：**

使用 `add-apt-repository` 命令添加 PPA。例如：

```
sudo add-apt-repository ppa:example/ppa
```

这里的 `ppa:example/ppa` 是 PPA 的名称。在命令中使用实际的 PPA 名称。

### [使用 appimage](https://github.com/AppImage/AppImageKit/wiki/FUSE)

参考上面的教程下载即可，可以给应用创建一个.desktop 的图标，便于之后使用

## 邮件系统

[ubuntu 对 postfix 的官方帮助文档](https://wiki.ubuntu.org.cn/Postfix_%E5%BF%AB%E9%80%9F%E6%8C%87%E5%8D%97)

MTA（Mail Transfer Agent）是用于发送和路由电子邮件的软件。常见的 MTA 包括 Postfix、Sendmail、Exim 等。以下是一般步骤来设置和使用 MTA：

1. **安装 MTA**：首先，你需要安装一个 MTA。在 Ubuntu 和 Debian 等 Linux 发行版上，你可以使用包管理器来安装，例如：

   ```
   sudo apt-get update
   sudo apt-get install postfix
   ```

   上述命令会安装 Postfix MTA。

2. **配置 MTA**：安装完成后，你需要对 MTA 进行一些配置。Postfix 的配置文件通常位于 `/etc/postfix/main.cf`。你可以编辑这个文件来配置域名、邮箱别名、邮件转发规则等。

3. **启动 MTA 服务**：配置完成后，你需要启动 MTA 服务。在大多数情况下，安装完成后 MTA 会自动启动，你可以使用以下命令来确认服务是否正在运行：

   ```
   sudo systemctl status postfix
   ```

   如果服务没有运行，你可以使用以下命令来启动：

   ```
   sudo systemctl start postfix
   ```

4. **测试发送邮件**：配置完成后，你可以测试 MTA 是否正常工作。你可以使用命令行工具 `mail` 来发送测试邮件：

   ```
   echo "This is a test email" | mail -s "Test Email" recipient@example.com
   ```

   替换 `recipient@example.com` 为你自己的邮箱地址。如果一切正常，你应该会收到一封来自你的服务器的测试邮件。

5. **查看日志**：如果遇到问题，你可以查看 MTA 的日志文件来排查。Postfix 的日志文件通常位于 `/var/log/mail.log` 或 `/var/log/maillog`。

## 静默打开

silence() {
open $1 >/dev/null 2>&1 &
}

[参见这里](file:///home/yang/.bashrc)

## 复制

`xclip` 是一个在 Linux 系统中用于与剪贴板进行交互的命令行工具。要使用 `xclip` 复制文件到剪贴板，你可以使用以下命令：

```
xclip -selection clipboard -t <MIME_type> -i <file_path>
```

其中：

- `-selection clipboard` 表示选择剪贴板作为目标。
- `-t <MIME_type>` 指定要复制的数据的 MIME 类型。对于文件，通常可以使用 `application/octet-stream`。
- `-i <file_path>` 指定要复制的文件的路径。

例如，要将文件 `example.txt` 复制到剪贴板，可以运行以下命令：

```
xclip -selection clipboard -t application/octet-stream -i example.txt
```

运行这个命令后，文件 `example.txt` 的内容将被复制到剪贴板中。你可以在其他应用程序中使用粘贴操作（通常是使用 Ctrl+V）来粘贴这个文件的内容。

## 执行定时任务

### 查看定时任务(当前用户)

crontab -l

### 编辑定时任务

crontab -e

m h m d y https://raw.githubusercontent.com/Cipivious/my_try/main/run.sh

### 检查定时任务的执行效果

/var/log/syslog 中存放着系统执行文件的记录，可以从里面查看执行情况

使用 `grep CRON /var/log/syslog` 可以筛选出定时文件的执行情况

## 自动启动程序

### 通过 gnome 的开机启动项目来自动启动

除了使用 systemctl 以外，还可以使用 gnome 自带的一个开机启动项目来进行设置，如下图所示，感觉这个执行的效果也不错

![启动应用首选项](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240507183014458.png)

### **桌面环境的自启动目录**

桌面环境通常提供了一个专门的目录，用于存放用户登录后要自动运行的程序。例如，在 GNOME 桌面环境中，可以将脚本放置在 `~/.config/autostart/` 目录中。这样，在用户登录后，桌面环境会自动运行该脚本，它和上面的应用的效果是一样的。

注意里面的一个开关，X-GNOME-Autostart-enabled 只有把这个设置成 true，程序才会在开机的时候自动启动

![autostart路径](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240508100325385.png)

### systemctl

#### [官方教程](https://systemd.io/)

#### [高级用法教程](https://ioflood.com/blog/systemctl-linux-command/#:~:text=It%20is%20a%20highly%20customizable,configure%20them%20to%20your%20needs.&text=In%20this%20example%2C%20we%20use,service%20)

#### 开机

在 Linux 系统中，您可以通过编辑启动脚本或者使用系统服务来实现在开机或关机时自动执行脚本的功能。

1. **使用启动脚本**： 您可以编辑 `/etc/rc.local` 文件，将您希望在系统启动时执行的命令或脚本添加到文件中。编辑完成后，保存文件并重新启动系统，系统启动时将会自动执行该脚本。

2. **使用 systemd 服务**： 在较新的 Linux 发行版中，通常使用 systemd 来管理系统服务。您可以创建一个 systemd 服务单元文件，并在其中指定要在系统启动时执行的脚本。以下是一个示例 systemd 服务单元文件的内容：

   ```
   plaintextCopy code[Unit]
   Description=My Script

   [Service]
   Type=oneshot
   ExecStart=/path/to/your/script.sh

   [Install]
   WantedBy=multi-user.target
   ```

   在这个示例中，`ExecStart` 指定了要执行的脚本的路径。编辑完成后，将该文件保存为 `.service` 后缀的文件（例如 `myscript.service`），然后将该文件移动到 `/etc/systemd/system/` 目录下。

   然后，运行以下命令来启用该服务并在系统启动时执行脚本：

   ```
   sh
   Copy code
   sudo systemctl enable myscript.service
   ```

   重新启动系统后，该脚本将会在系统启动时自动执行。

#### 关机

对于在 Linux 系统关闭时执行脚本的需求，您可以使用 systemd 的关机钩子（shutdown hook）来实现。关机钩子允许您在系统关闭时执行特定的命令或脚本。

以下是如何使用 systemd 的关机钩子来执行脚本的步骤：

1. 创建一个脚本文件，其中包含您希望在系统关闭时执行的命令。假设您的脚本文件是 `/path/to/your/shutdown_script.sh`。
2. 创建一个 systemd 单元文件，用于定义关机钩子。命名为 `your-shutdown-hook.service`，内容如下：

```
plaintextCopy code[Unit]
Description=Shutdown Hook
DefaultDependencies=no
Before=shutdown.target reboot.target halt.target
Requires=network.target
After=network.target

[Service]
Type=oneshot
ExecStart=/path/to/your/shutdown_script.sh

[Install]
WantedBy=halt.target reboot.target shutdown.target
```

在这个示例中，`ExecStart` 指定了要在系统关闭时执行的脚本的路径。

1. 将该文件保存到 `/etc/systemd/system/` 目录下。
2. 使用以下命令启用服务：

```
sudo systemctl enable your-shutdown-hook.service
```

这样，当系统关闭时，您的脚本 `/path/to/your/shutdown_script.sh` 将会自动执行。

## chmod

chmod 是改变文件权限的方法

[Linux 系统误将 chmod 权限改成 了 000，如何恢复?](https://www.zhihu.com/question/590661860/answer/3288127626?utm_psn=1771052214779686912)

## 使用 git

### 技巧

code 里面可以搜到相关的代码，有时候从 repo 中找不到可以从这里看看

![寻找需要的文件](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240506094709757.png)

### 上传代码

一旦您的 Markdown 文件准备好了，您可以使用 Git 工具将文件上传到 GitHub。以下是一个基本的上传流程：

- 首先，确保您已经在本地使用 Git 初始化了一个仓库，并将其与 GitHub 上的远程仓库关联。
- 将您的 Markdown 文件添加到 Git 中：`git add your_file.md`
- 提交更改：`git commit -m "Add your_file.md"`
- 推送到 GitHub：`git push origin master`

在上面的命令中，`your_file.md` 是您要上传的 Markdown 文件的文件名，`origin` 是您与 GitHub 关联的远程仓库的名称，`master` 是您要推送到的分支名称。

可以使用 git commit -m "Add new feature - $(date +"%Y-%m-%d")"按日期更新

如果你想要舍弃本地的更改，并将本地仓库恢复到与远程仓库相同的状态，你可以使用 `git reset --hard` 命令。这个命令会将工作目录、暂存区和 HEAD 指针都重置到指定的提交（或分支），并且会丢弃所有未提交的更改。

在你的情况下，你可以执行以下命令来舍弃本地的更改并将本地仓库恢复到与远程仓库相同的状态：

```
git reset --hard origin/main
```

这个命令会将你当前所在分支（假设是 `main` 分支）重置为与远程 `main` 分支相同的状态，丢弃本地的所有更改。

### [run.sh](file://https://raw.githubusercontent.com/Cipivious/my_try/main/my_try/run.sh)

这是一个自动上传的脚本

### [下载单个文件](https://worktile.com/kb/ask/210361.html)

```bash
git archive –format=zip –output=file.zip HEAD:path/to/file
```

### [删除仓库](https://worktile.com/kb/ask/261517.html)

要删除远程分支的文件，需要按照以下步骤进行操作：

1. 首先，使用以下命令查看当前的远程分支列表：

   git branch -r

   这将显示所有的远程分支列表，包括远程分支的名称和对应的远程仓库。

2. 然后，使用以下命令切换到对应的本地分支，用于进行文件删除操作：

   git checkout

   这将切换到本地分支 。

3. 接下来，使用以下命令查看当前分支的文件列表：

   git ls-files

   这将显示当前分支的所有文件列表。

4. 然后，使用以下命令删除指定的文件：

   git rm

   处填写要删除的文件路径。

5. 接着，使用以下命令提交删除的文件变更：

   git commit -m “Delete file: ”

   在 `` 处填写要删除的文件路径。

6. 最后，使用以下命令推送删除的文件变更到远程分支：

   git push origin

   这将推送删除的文件变更到远程分支 ``。

## ssh 使用方法

下面是使用 SSH 的一般操作步骤：

1. **生成 SSH 密钥对：** 在客户端生成 SSH 密钥对，包括公钥和私钥。你可以使用以下命令生成 SSH 密钥对：

```
ssh-keygen -t rsa -b 2048 -C "your_email@example.com"
```

这个命令会生成一个 RSA 类型的密钥对，并将其保存在默认的路径（通常是 `~/.ssh/id_rsa`）。

2. **将公钥添加到服务器：** 将生成的公钥（通常是 `~/.ssh/id_rsa.pub` 文件中的内容）添加到服务器的 `~/.ssh/authorized_keys` 文件中。这样，客户端就可以使用私钥与服务器进行安全通信了。

```
ssh-copy-id user@server_ip
```

3. **使用 SSH 连接服务器：** 客户端可以使用以下命令连接到服务器：

```
ssh user@server_ip
```

在连接时，SSH 会使用客户端的私钥对通信进行加密和认证，以确保连接的安全性。如果私钥与服务器的公钥匹配，连接将会成功建立。

## 创建链接以及使用方法

### 创建链接的方法

ln -s /path/to/target /path/to/symlink

### 查看链接的文件

ls -l /path/to/directory

### 删除链接

rm /path/to/link

### 操作链接

要打开符号链接代表的文件或目录，您可以像打开任何其他文件或目录一样操作。只需提供符号链接的路径即可。

## 查看硬件信息

### 查看电源设置

upower -d /org/freedesktop/UPower/devices/battery_BATO

### 查看 CPU 设置

lscpu

### 查看显卡设置

lspci

### 查看内存信息

cat /proc/meminfo

### 查看硬盘信息

sudo du -h --max-depth=1 查看硬盘空间使用情况

lsblk

### 查看全部的信息

lshw

### 结果

[参见这里](#电脑硬件)

## [临时当做计算器](https://blog.csdn.net/focus_lyh/article/details/112371286)

expr 1 + 2（注意空格）

expr 28 \* 28（运算符需要转义）

## [修改默认应用](https://blog.csdn.net/hustrains/article/details/8652098)

如果你想指定 Okular 和 Emacs 作为默认的应用程序来打开特定类型的文件，你需要做以下步骤：

1. **确定应用程序的.desktop 文件名：** 首先，你需要确定 Okular 和 Emacs 的.desktop 文件名。通常，Okular 的.desktop 文件名可能是`okular.desktop`，Emacs 的.desktop 文件名可能是`emacs.desktop`。你可以在`/usr/share/applications`目录中查找这些文件，或者使用`locate`命令搜索它们。

2. **编辑文件关联：** 一旦确定了.desktop 文件名，你可以编辑文件关联列表以将其与特定类型的文件关联起来。你可以通过在终端中使用文本编辑器（如 Nano 或 Vim）打开`~/.local/share/applications/mimeapps.list`文件，然后添加以下行：

```
application/oxps=okular.desktop
application/pdf=okular.desktop
application/postscript=okular.desktop
application/rtf=emacs.desktop
```

这样就会将 Okular 关联到`.oxps`、`.pdf`和`.ps`文件，将 Emacs 关联到`.rtf`文件。

3. **保存更改：** 保存并关闭`mimeapps.list`文件。

4. **更新文件关联：** 最后，你可能需要重新启动你的文件管理器或者重启会话来应用这些更改。

## linux 下图像编辑工具

### gimp

它是支持项目最多的软件

[官方网站](https://www.gimp.org/downloads/)

[中文教程](https://docs.gimp.org/2.10/zh_CN/)

[画各种形状](https://blog.csdn.net/tody_guo/article/details/7628508)

## 破解密码

### [aircrack-ng---破解 WiFi 密码](https://github.com/conwnet/wpa-dictionary)

首先获取数据包，然后使用字典暴力破解，上述的链接存着常用的密码字典

### [aircrack 教程](https://blog.csdn.net/MyJDL/article/details/52629383)

### [rarcrack](https://www.kali.org/tools/rarcrack/)

破解 rar，zip，7z 格式的压缩包

## gnome-extension

[集成 gnome 浏览器](https://extensions.gnome.org/)

在 app-store 中可以下载 gnome-extension，插件的路径是`~/.local/share/gnome-shell/extensions`这个。

## [QtDbus](https://blog.csdn.net/u011942101/article/details/123393592)

D-Bus 是一种进程间通信（IPC）和远程过程调用（RPC）机制，最初是为 Linux 开发的，用于用一个统一的协议取代现有的和相互竞争的 IPC 解决方案。它还被设计为允许系统级进程（如打印机和硬件驱动程序服务）与正常用户进程之间的通信。
它使用一种快速的二进制消息传递协议，由于其低延迟和低开销，适用于同一台机器的通信。其规范目前由 freedesktop 定义。org 项目，并可供各方使用。

## 桌面图形系统

要确定你正在使用的 Ubuntu 桌面系统是 X 还是 Wayland：

```bash
echo $XDG_SESSION_TYPE
```

X11 是传统的图形显示服务器，而 Wayland 是一个新兴的图形显示协议，旨在替代 X11 并提供更现代、更高效、更安全的图形显示解决方案。

X11 和 Wayland 之间的主要区别包括：

1. **架构和设计**：X11 是一个复杂的图形显示系统，具有分离的服务器和客户端，而 Wayland 是一个更简单、更直接的图形显示协议，将显示服务器和客户端整合在一起。

2. **性能**：由于 Wayland 的设计更现代化，它通常比 X11 具有更好的性能和更低的延迟。这意味着在使用 Wayland 的系统上，图形显示更加流畅和响应。

3. **安全性**：Wayland 在设计上考虑了安全性，并提供了更严格的权限控制机制，以确保图形显示系统的安全性。

4. **硬件加速支持**：Wayland 提供了更好的硬件加速支持，可以更充分地利用现代图形硬件的性能优势。

除了 X11 和 Wayland 外，还有其他类似的图形显示系统，比如 Mir，它是由 Canonical 开发的用于 Ubuntu Touch 和 Ubuntu 桌面系统的另一种图形显示协议。Mir 的目标与 Wayland 类似，旨在提供更现代、更高效、更安全的图形显示解决方案。
