# SQL

## 学习笔记

### 设计数据库

#### [数据库设计工具](https://zhuanlan.zhihu.com/p/694452923?utm_psn=1776890537222062080)

DrawDB是一款多功能且用户友好的在线工具，允许用户轻松设计数据库实体关系。通过简单直观的界面，DrawDB使用户能够创建图表、导出SQL脚本、自定义编辑环境，而无需创建账户。

#### 示例

![数据库示例](https://raw.githubusercontent.com/Cipivious/my_try/main/image/gmdb.png)

#### 设计原则

![设计原则](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240514205553543.png)

### 创建一个新用户

要在 MySQL 数据库中创建一个新用户，你需要以 root 身份登录到 MySQL，并使用 CREATE USER 和 GRANT 语句来完成。以下是创建新用户的步骤：

1. 以 root 身份登录到 MySQL：

   ```bash
   mysql -u root -p
   ```

   然后输入你的 root 密码来登录。

2. 创建一个新用户。例如，创建一个名为 `newuser` 的用户并指定密码：

   ```sql
   CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
   ```

   这将创建一个名为 `newuser` 的用户，他只能从本地主机连接，并且使用 `password` 作为密码。请确保将 `password` 替换为你选择的实际密码。

3. 授予新用户所需的权限。例如，你可以授予新用户对所有数据库的全部权限：

   ```sql
   GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost' WITH GRANT OPTION;
   ```

   这将授予 `newuser` 用户对所有数据库的所有权限，并且允许他对这些权限进行授权。

4. 刷新 MySQL 权限：

   ```sql
   FLUSH PRIVILEGES;
   ```

5. 退出 MySQL：

   ```sql
   exit;
   ```

现在，你已经成功创建了一个名为 `newuser` 的新用户，并且授予了他适当的权限。记得将 `localhost` 替换为你的实际主机名，如果你希望该用户能够从其他主机连接。

### 基本数据库操作

1. **创建数据库**：

```sql
CREATE DATABASE database_name;
```


2. **显示当前的数据库**：

```sql
SHOW DATABASES;
```

这将列出 MySQL 服务器上当前存在的所有数据库。

3. **选择数据库**：

```sql
USE database_name;
```


4. **查看数据库中的表**：

```sql
SHOW TABLES;
```

这将列出当前活动数据库中的所有表。

5. **创建表**：

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

例如，要创建名为 `users` 的表，具有 `id` 和 `username` 列：

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL
);
```

6. **删除数据库**：

```sql
DROP DATABASE database_name;
```

请小心使用此命令，因为它将永久删除指定的数据库及其所有内容。例如：

```sql
DROP DATABASE mydatabase;
```

这些是 MySQL 中最基本的数据库操作。根据您的需求，您可能还需要了解如何向表中插入数据、查询数据、更新数据和删除数据等更高级的数据库操作。

### 基本的 MySQL 表操作：

1. **创建表**：

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

例如，要创建名为 `users` 的表，具有 `id` 和 `username` 列：

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL
);
```

2. **查看表结构**：

```sql
DESCRIBE table_name;
```

这将显示指定表的结构，包括列名、数据类型和其他属性。

3. **插入数据**：

```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

例如，向名为 `users` 的表中插入新的用户记录：

```sql
INSERT INTO users (username) VALUES ('John'), ('Alice'), ('Bob');
```

4. **查询数据**：

```sql
SELECT * FROM table_name;
```

这将返回指定表中的所有数据。

5. **更新数据**：

```sql
UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
```

例如，更新名为 `users` 的表中 `id` 为 1 的用户的用户名：

```sql
UPDATE users SET username = 'Jane' WHERE id = 1;
```

6. **删除数据**：

```sql
DELETE FROM table_name WHERE condition;
```

例如，删除名为 `users` 的表中 `id` 为 2 的用户：

```sql
DELETE FROM users WHERE id = 2;
```

7. **删除表**：

```sql
DROP TABLE table_name;
```

请小心使用此命令，因为它将永久删除指定的表及其所有数据。例如：

```sql
DROP TABLE users;
```

这些是 MySQL 中最基本的表操作。根据您的需求，您可能还需要了解如何使用索引、约束、视图和存储过程等更高级的表操作。

### select的高阶用法

`SELECT` 是 SQL 中最常用的语句之一，用于从数据库中检索数据。以下是 `SELECT` 语句的基本用法以及一些常见的用法变体：

#### 基本用法：

```sql
SELECT column1, column2, ... FROM table_name;
```

这个语句用于从指定的表中选择指定的列。您可以使用 `*` 来选择所有列。

#### 带有条件的查询：

```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
```

在 `WHERE` 子句中指定条件，以筛选出满足条件的行。条件可以包括比较运算符（例如 `=`, `>`, `<`, `>=`, `<=`, `!=`），逻辑运算符（例如 `AND`, `OR`, `NOT`），以及其他条件。

```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
```

在 `WHERE` 子句中指定条件，以筛选出满足条件的行。条件可以包括比较运算符（例如 `=`, `>`, `<`, `>=`, `<=`, `!=`），逻辑运算符（例如 `AND`, `OR`, `NOT`），以及其他条件。

#### 排序：

```sql
SELECT column1, column2, ... FROM table_name ORDER BY column1, column2, ... ASC|DESC;
```

使用 `ORDER BY` 子句对结果进行排序。您可以指定一个或多个列来排序，并使用 `ASC`（升序）或 `DESC`（降序）来指定排序顺序。

#### 聚合函数：

```sql
SELECT COUNT(*), SUM(column), AVG(column), MAX(column), MIN(column) FROM table_name;
```

聚合函数允许您对数据进行汇总和计算。例如，`COUNT()` 用于计算行数，`SUM()` 用于计算总和，`AVG()` 用于计算平均值，`MAX()` 和 `MIN()` 用于计算最大值和最小值。

```sql
SELECT COUNT(*), SUM(column), AVG(column), MAX(column), MIN(column) FROM table_name;
```

聚合函数允许您对数据进行汇总和计算。例如，`COUNT()` 用于计算行数，`SUM()` 用于计算总和，`AVG()` 用于计算平均值，`MAX()` 和 `MIN()` 用于计算最大值和最小值。

#### 分组：

```sql
SELECT column1, AGGREGATE_FUNCTION(column2) FROM table_name GROUP BY column1;
```

使用 `GROUP BY` 子句将数据分组，以便对每个组应用聚合函数。例如，您可以按照某个列的值对数据进行分组，并对每个组的其他列应用聚合函数。

#### 连接：

```sql
SELECT table1.column1, table2.column2 FROM table1 JOIN table2 ON table1.column = table2.column;
```

`JOIN` 用于将多个表中的数据合并在一起。您可以通过 `ON` 子句指定连接条件，以确定如何将两个表中的行匹配起来。

```sql
SELECT table1.column1, table2.column2 FROM table1 JOIN table2 ON table1.column = table2.column;
```

`JOIN` 用于将多个表中的数据合并在一起。您可以通过 `ON` 子句指定连接条件，以确定如何将两个表中的行匹配起来。

这些是 `SELECT` 语句的一些常见用法。通过组合这些用法，您可以执行复杂的查询来获取所需的数据。在实践中，您可能会根据具体的业务需求使用 `SELECT` 语句的不同变体。

#### 选择奇数列

```sql
SELECT * FROM guitarwars WHERE MOD(id, 2) = 1;
```

#### 选择包含一定字符的内容

```sql
SELECT * FROM cookies c WHERE host_key LIKE '%zhihu%';
```

### 多表操作

#### join关联查询

在数据库中，`JOIN` 是一种非常常用的操作，用于根据两个或多个表之间的某些相关列之间的关系，从这些表中查询数据。以下是几种常见的 `JOIN` 类型及其使用方法：

1. **INNER JOIN（内连接）**

   例子

   ```mysql
   mysql> SELECT mismatch_topic.topic_id , mismatch_category.name FROM mismatch_topic INNER JOIN mismatch_category ON (mismatch_topic.category_id = mismatch_category.category_id ) WHERE mismatch_topic.name = 'Horror movies';
   +----------+---------------+
   | topic_id | name          |
   +----------+---------------+
   |        8 | Entertainment |
   +----------+---------------+
   1 row in set (0.00 sec)
   //如果列名相同的时候可以简化成USING，比如上面可以简化成(列名都为category)
   SELECT mismatch_topic.topic_id , mismatch_category.name FROM mismatch_topic INNER JOIN mismatch_category USING(category_id) WHERE mismatch_topic.name = 'Horror movies';
   ```

   

   返回两个表中都有的数据。当两个表中指定的列的值相等时，返回行。

   ```sql
   SELECT columns  
   FROM table1  
   INNER JOIN table2  
   ON table1.column_name = table2.column_name;
   ```

2. **LEFT JOIN（左连接，或 LEFT OUTER JOIN）**

     

   返回左表中的所有记录，以及右表中匹配的行。如果右表中没有匹配的行，则结果中对应列的值将是 NULL。

   ```sql
   SELECT columns  
   FROM table1  
   LEFT JOIN table2  
   ON table1.column_name = table2.column_name;
   ```

3. **RIGHT JOIN（右连接，或 RIGHT OUTER JOIN）**

     

   与 LEFT JOIN 相反，返回右表中的所有记录，以及左表中匹配的行。如果左表中没有匹配的行，则结果中对应列的值将是 NULL。

   ```sql
   SELECT columns  
   FROM table1  
   RIGHT JOIN table2  
   ON table1.column_name = table2.column_name;
   ```

   注意：虽然 RIGHT JOIN 在技术上可用，但在实践中，LEFT JOIN 通常更常用，因为可以通过调整表顺序和连接条件来模拟 RIGHT JOIN。

4. **FULL JOIN（全连接，或 FULL OUTER JOIN）**

     

   返回左表和右表中的所有记录。当某一边没有匹配时，对应列的值将是 NULL。

   ```sql
   -- 注意：不是所有的数据库系统都支持 FULL JOIN，但可以使用 UNION 来模拟  
   SELECT columns  
   FROM table1  
   FULL JOIN table2  
   ON table1.column_name = table2.column_name;
   ```

   如果数据库不支持 FULL JOIN，你可以通过结合 LEFT JOIN 和 RIGHT JOIN（并使用 UNION 去除重复行）来模拟它。

5. **CROSS JOIN（交叉连接）**

     

   返回左表中的每一行与右表中的每一行的组合。如果没有指定连接条件，将返回左表和右表的笛卡尔积。

   ```sql
   SELECT columns  
   FROM table1  
   CROSS JOIN table2;
   ```

6. **SELF JOIN（自连接）**

     

   一个表与其自身进行连接。通常用于比较表内的行或查找表内的相关行。

   ```sql
   SELECT columns  
   FROM table1 t1  
   JOIN table1 t2  
   ON t1.column_name = t2.other_column_name;
   ```

   在上面的查询中，`t1` 和 `t2` 是对同一个表 `table1` 的不同引用（别名），允许你在查询中区分它们。

当使用 JOIN 时，确保选择正确的连接类型，并明确指定连接条件，以确保查询返回所需的结果。同时，为了提高性能，确保连接的列已经被适当地索引。

### 防止注入攻击（php version）

```php
$first_name = mysqli_real_escape_string($dbc, trim($_POST['firstname']));
$last_name = mysqli_real_escape_string($dbc, trim($_POST['lastname']));
```



这段代码涉及到了对用户输入进行处理，以防止 SQL 注入和去除不必要的空白字符。

1. **mysqli_real_escape_string() 函数**：这是一个用于转义 SQL 查询中的特殊字符的函数。当用户输入包含引号等特殊字符时，如果不进行处理，可能会导致 SQL 注入攻击。`mysqli_real_escape_string()` 函数会将这些特殊字符转义，使其成为安全的文本数据，可以安全地插入到 SQL 查询中。它的语法是：

   ```php
   $escaped_string = mysqli_real_escape_string($connection, $string);
   ```

   其中，`$connection` 是数据库连接对象，通常使用 `mysqli_connect()` 或 `mysqli_init()` 函数创建；`$string` 是要转义的字符串。

2. **trim() 函数**：这是一个用于去除字符串两端的空白字符（空格、制表符、换行符等）的函数。在用户输入时，可能会存在不小心输入多余的空白字符，使用 `trim()` 函数可以去除这些不必要的空白字符，以保证数据的一致性。它的语法是：

   ```php
   $trimmed_string = trim($string);
   ```

   其中，`$string` 是要去除空白字符的字符串。

因此，以上代码段将 `$_POST` 中的 `firstname` 和 `lastname` 值进行了处理：先使用 `trim()` 函数去除了两端的空白字符，然后使用 `mysqli_real_escape_string()` 函数对字符串进行了转义，以防止 SQL 注入攻击。

### 执行sql脚本

#### 示例sql脚本

```sql
CREATE TABLE `guitarwars` (
  `id` INT AUTO_INCREMENT,
  `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `name` VARCHAR(32),
  `score` INT,
  `screenshot` VARCHAR(64),
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
);

INSERT INTO `guitarwars` VALUES (1, '2008-04-22 14:37:34', 'Paco Jastorius', 127650, 'pacosscore.gif');
INSERT INTO `guitarwars` VALUES (2, '2008-04-22 21:27:54', 'Nevil Johansson', 98430, 'nevilsscore.gif');
INSERT INTO `guitarwars` VALUES (4, '2008-04-23 09:12:53', 'Belita Chevy', 282470, 'belitasscore.gif');
INSERT INTO `guitarwars` VALUES (6, '2008-04-23 14:09:50', 'Kenny Lavitz', 64930, 'kennysscore.gif');
INSERT INTO `guitarwars` VALUES (7, '2008-04-24 08:13:52', 'Phiz Lairston', 186580, 'phizsscore.gif');
INSERT INTO `guitarwars` VALUES (8, '2008-04-25 07:22:19', 'Jean Paul Jones', 243260, 'jeanpaulsscore.gif');
INSERT INTO `guitarwars` VALUES (9, '2008-04-25 11:49:23', 'Jacob Scorcherson', 389740, 'jacobsscore.gif');
```



####  直接在命令行执行sql脚本

```bash
(base) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:/var/www/html/ch05/final$ mysql -uyang -p game < guitarwars.sql 
 #这是选择数据库的操作，也可以直接用下面的
 (base) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:~/code/sql$ mysql -uyang -p < create_database.sql 
  #这样是直接执行sql脚本，不需要选择是那个数据库来操作
```



#### 在登陆mysql以后执行

```bash
mysql> source /var/www/html/ch05/final/guitarwars.sql;
Query OK, 0 rows affected (0.02 sec)

Query OK, 1 row affected (0.01 sec)

Query OK, 1 row affected (0.00 sec)

Query OK, 1 row affected (0.00 sec)

Query OK, 1 row affected (0.00 sec)

Query OK, 1 row affected (0.01 sec)

Query OK, 1 row affected (0.00 sec)

Query OK, 1 row affected (0.00 sec)
```

### 将SQLite数据库导出成sql脚本

要将 SQLite 数据库中的数据导出为 SQL 文件，可以使用 SQLite 提供的命令行工具 `sqlite3`。以下是基本的步骤：

1. 使用以下命令连接到要导出的 SQLite 数据库文件：

   ```
   sqlite3 /path/to/your/database.db
   ```

   这里 `/path/to/your/database.db` 是你要导出的 SQLite 数据库文件的路径。

2. 输入以下命令导出数据到 SQL 文件：

   ```
   .output /path/to/your/output.sql
   .dump
   ```

   这里 `/path/to/your/output.sql` 是你要导出的 SQL 文件的路径。`.dump` 命令会将数据库中的所有表格结构和数据输出到当前指定的输出文件中。

3. 通过执行上述步骤，你就可以将 SQLite 数据库中的数据导出为 SQL 文件。接下来，你可以使用其他数据库管理工具或编程语言中的 MySQL 客户端来执行该 SQL 文件，将数据导入到 MySQL 数据库中。

### 导出数据

```sql
TEE information.txt  
DESCRIBE mismatch_category;  
NOTEE	
```

执行效果如下：

```bash
(base) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:/var/www/html/ch08/final$ cat information.txt 
mysql> DESCRIBE mismatch_category;
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| category_id | int         | NO   | PRI | NULL    | auto_increment |
| name        | varchar(48) | YES  |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)
 #它会把命令行所有输入输出信息都导入到information.txt当中
```



## 安装mysql数据库及命令行工具

在Ubuntu命令行中安装MySQL数据库服务器和MySQL命令行工具可以使用以下步骤：

### **安装MySQL数据库服务器：**

```bash
sudo apt update
sudo apt install mysql-server
```

安装过程中会提示您设置MySQL root用户的密码，请根据提示完成设置。

安装完成后，MySQL服务器会自动启动，并且会随系统启动而启动。

### **安装MySQL命令行工具：**

```bash
sudo apt update
sudo apt install mysql-client
```

安装完成后，您可以使用以下命令连接到MySQL服务器：

```bash
sudo mysql -u root -p
```

其中，用户名是您在MySQL服务器上的用户名。输入此命令后，系统将提示您输入密码，输入与该用户名关联的密码即可登录到MySQL服务器。

您还可以使用其他MySQL命令行工具，例如`mysqladmin`、`mysqldump`等，它们通常随着`mysql-client`软件包一起安装。

### **禁止mysql自动启动**

如果您只想在需要时启动 MySQL，而不希望它在系统启动时自动启动，您可以禁用 MySQL 服务器的自动启动：

```
sudo systemctl disable mysql
```

这样做后，MySQL 将不会在系统启动时自动启动，您需要手动执行 `sudo systemctl start mysql` 才能启动它。

![安装mysql-server](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240506162408921.png)

![连接本地数据库](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240506163536112.png)



### mysql内部文件

在Ubuntu上，默认情况下，MySQL 数据库文件存储在 `/var/lib/mysql/` 目录下。这个目录包含了MySQL数据库的所有数据文件，包括数据库、表和数据，以下是具体的信息。

1. `auto.cnf`: 包含自动生成的 MySQL 配置信息。
2. `binlog.*`: 二进制日志文件，用于记录数据库的更改操作。
3. `client-cert.pem`, `client-key.pem`: 客户端 SSL/TLS 证书和密钥。
4. `debian-5.7.flag`: 一个标志文件，指示该 MySQL 实例是由 Debian 软件包管理器安装的。
5. `ib_buffer_pool`: InnoDB 存储引擎的缓冲池文件。
6. `ibdata1`: InnoDB 存储引擎的共享表空间文件。
7. `mysql`: MySQL 系统数据库，包含用户权限、配置等信息。
8. `performance_schema`: 用于存储 MySQL 性能监控数据的数据库。
9. `sys`: 用于存储 MySQL 系统表的数据库。
10. `undo_*`: InnoDB 存储引擎的 undo 日志文件。
11. `*.pem`: SSL/TLS 证书和密钥文件，用于安全连接。





## 学习笔记

### pexpect

这个脚本用于模拟输入变量。

```py
import pexpect
import random
import time

# 启动程序
child = pexpect.spawn('../c/draw_array')

# # 模拟输入
# inputs = ["5", "10", "15", "0"]

# for value in inputs:
#     child.expect("Enter a number")
#     child.sendline(value)

while True:
    value = random.random() * 10
    value = str(value)
    child.expect("Enter a number")
    child.sendline(value)
    time.sleep(0.5)  # 间隔0.5秒

# 打印程序的输出
child.interact()
```



### os

#### os.walk(folder_path)

遍历文件夹下所有的内容，返回（root,dirs,files）

#### os.path.join(path1,path2)

将两个路径拼接到一起，返回一个路径字符串

#### os.path.isfile(file_path)

判断file_path这个字符串是否存在一个文件

### 列表

列表可以嵌套其他的结构，也可以嵌套列表

#### 创建一个列表

lists = [ ]

#### 在列表尾部添加一个元素

lists.append(element)

#### 列表索引

从零开始，以可以从后向前索引

### 文件读写操作

```python
with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
//lines是一个列表
```





## python 程序包

### [生成python项目需要的最小requirements.txt文件](https://www.zhihu.com/question/463332914/answer/3433457082?utm_psn=1777328303856664576)

#### pip freeze方法

#### 使用第三方库[pipreqs](https://www.zhihu.com/search?q=pipreqs&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A3433457082})

### [EasySpider](https://www.zhihu.com/question/36292298/answer/3035289149?utm_psn=1771060801685999616)

EasySpider是一款[完全免费](https://www.zhihu.com/search?q=完全免费&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A3035289149})和开源的可视化爬虫软件，此软件可以让大家使用图形化界面，无代码可视化的设计和执行爬虫任务。

### [sympy](https://docs.sympy.org/latest/modules/vector/basics.html)

### [Python/Sympy 计算梯度、散度和旋度](https://blog.csdn.net/ouening/article/details/80712269)

### [python-markdown](https://github.com/Python-Markdown/markdown)

#### 我想通过下面的方法添加一个扩展

from markdown.preprocessors import Preprocessor
import markdown
import re

class AddIdToHeaders(Preprocessor):
    """ Add id attribute to headers starting with '#' """
    def run(self, lines):
        new_lines = []
        for line in lines:
            if line.startswith('#'):
                # Match the header text after '#' and remove any special characters
                header_text = line.strip('#').strip()
                # Determine the header level
                header_level = line.count('#')
                id_value = re.sub(r'\W+', '-', header_text.lower())
                # Add id attribute to the header tag
                new_lines.append(f'<h{header_level} id="{id_value}">{line.strip("#").strip()}</h{header_level}>')
            else:
                new_lines.append(line)
        return new_lines

 将自定义的预处理器作为扩展添加到 Markdown 转换中
extensions = [AddIdToHeaders()]

 读取 Markdown 文件内容
with open('your_markdown_file.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

 将 Markdown 转换为 HTML，并应用自定义的预处理器
html_content = markdown.markdown(markdown_content, extensions=extensions)



## python 爬虫

###06 爬虫

12306 是被访问量最高的网站之一，有相当多的软件针对 12306 设计，它们可以自动化的实现很多 12306 上的任务，导致普通人难以直接买到票，官方为了解决这些问题，也做出了很多的努力，但上有政策，下有对策，这个问题一时之间还是难以解决。技术黄牛已然成为了提高普通人生活成本的一项重大因素。和这个类似的还有网购时的价格策略，千人千价，通过算法来剥削用户。

### 地图爬虫

地图爬虫主要分为高德地图和百度地图，爬取的范围比较广泛，需要使用对应的 api 接口，这在网站当中也是十分常见的，两种服务在咸鱼上都有售卖。

### 词频统计软件

把它放到这里，主要是它也是爬虫需要的一个部分，如果能处理爬虫的问题，那么一般来说词频统计一类的也都不是问题。

### 爬虫技术

我学过一些爬虫的技术，比如 request 和 beautifulsoup 组合爬取网页的内容，也学习过使用包模拟登录浏览器的程序，我倒是成功打开浏览器了，但是没有能够进一步操作，我觉得最方便的是 scrapy 这个包，它可以充分的和浏览器的开发者工具结合，直接锁定页面里面对应的内容，功能非常的强大。但是随着 [网站验证技术的提高](#网站验证), 导致爬虫的技术难度也逐渐提高，不过总有高手可以解决问题。

## python 微信自动化工具

### [wxpy](https://github.com/youfou/wxpy/releases)

已经不行了，微信不支持网页版

### itchat

基本框架

### pywin

现在的主要方法，使用按键模拟的方法进行控制