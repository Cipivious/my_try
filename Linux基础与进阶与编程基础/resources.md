



# 架构

## 参考资料

### [程序员你是怎么绘制架构图？](https://zhuanlan.zhihu.com/p/214373872?utm_psn=1776214505611386880)

### [为什么很多程序员没有升级到架构师？](https://zhuanlan.zhihu.com/p/101086202)

### [path to a software architect](https://github.com/justinamiller/SoftwareArchitect)

## 架构师成长路线

![架构师成长路线](https://raw.githubusercontent.com/Cipivious/my_try/main/image/archRoadmap.jpg)

上图展示了成为架构师的路线图，涵盖了多方面的知识和技能，具体包括以下几个主要领域：

### 工具（Tools）
- **Atlassian 工具**（Atlassian tools）
- **Slack**
- **Trello**

### 管理（Management）
- **Scaled: Less, SAFe**
- **敏捷（Agile）, Scrum**
- **PMI**, **ITIL**, **Prince 2**, **RUP**

### 数据（Data）
- **SQL**
  - **Postgre SQL**
  - **Oracle**
  - **MySQL**
- **NoSQL**
- **分析**（Analytics）
  - **Apache Spark**
  - **Hadoop**
- **ETL**, **数据仓库**（Data warehouses）
- **大数据工具**（Hadoop, Spark, MapReduce）

### 架构（Architectures）
- **无服务器（Serverless）**
- **微服务（Microservices）**
- **客户端/服务器架构**（Client server）
- **分层架构**（Layered）
- **分布式系统**（Distributed systems）
- **面向服务架构（SOA）**

### 模式（Patterns）
- **MVC**, **MVP**, **MVVM**
- **演员模型**（Actors）
- **SOLID**
- **领域驱动设计（DDD）**
- **面向对象编程（OOP）**
- **CQRS**, **最终一致性（Eventual consistency）**
- **ACID**, **CAP 定理（CAP theorem）**

### 网页和移动开发（Web, mobile）
- **响应式和函数式编程（Reactive & functional programming）**
- **React**, **Angular**, **Vue**
- **单页应用（SPA）**
- **渐进式网页应用（PWA）**
- **W3C 和 WHATWG 标准**（W3C & WHATWG standards）
- **设计思维、UI、UX、CX**（Design thinking, UI, UX, CX）

### 框架（Frameworks）
- **TOGAF**
- **UML**
- **IAF**
- **BABOK**
- **云计算（Cloud）**
  - **Azure**, **AWS**
  - **公有云、私有云、混合云**（Public, private, hybrid）
  - **无服务器概念**（Serverless concepts）
- **JBoss**

### 操作（Operations）
- **Ansible**, **Terraform**
- **CI/CD 工具**（CI/CD tools）
- **服务网格（Service mesh）**
- **SRE**
- **Docker**, **Kubernetes（K8s）**
- **Linux**

### 企业软件（Enterprise software）
- **Salesforce**
- **EMC DMS**
- **IBM BPM**
- **MS Dynamics**
- **SAP EPR**, **HANA**, **Business objects**

### 集成（Integration）

- **MQ**
- **业务流程管理（BPM）**, **BPEL**
- **企业服务总线（ESB）**, **SOAP**
- **API 网关及管理（API GWs, Management）**
- **REST**

### 编程（Programming）

- **.NET**
- **Java/Kotlin/Scala**
- **JavaScript/TypeScript**
- **PHP**
- **Python**
- **Go**
- **Spring**

### 安全（Security）

- **OAuth2**, **Open ID Connect**
- **OWASP**
- **公钥基础设施（PKI）**

通过掌握以上领域的知识和技能，可以帮助你成为一名全面的架构师。这个路线图展示了成为架构师所需的各方面知识，包括工具、管理、数据、架构、模式、网页和移动开发、框架、操作、企业软件、集成、编程和安全等。





# 自动化按键操作

## sikulix

下载存在问题，在2023年停止维护

## [pyautogui](https://github.com/asweigart/pyautogui)

去年停止维护

## [autohotkey](https://github.com/AutoHotkey/AutoHotkey?tab=readme-ov-file)

仍然在活跃运转，但是它主要只运行在windows平台

The ultimate automation scripting language for Windows

# 算法

## 数独

```python
# 这个函数用于判断在‘board’的‘row’行‘col’列能否插入‘num’元素，要判断横，竖，以及所属的九宫格
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[row//3*3 + i//3][col//3*3 + i%3] == num:
            return False
    return True
# 这个函数递归的调用自身，先假设在某个位置插入数字，然后一直计算下去，如果遍历完九个数都不能填入的话，就返回‘false’，否则就一直继续下去。它会在搜索到第一个解以后返回‘true’然后终止
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# 这个函数用于打印九宫格
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# 示例数独谜题
sudoku_board = [
    [4, 0, 0, 0, 0, 2, 3, 1, 8],
    [8, 0, 1, 0, 0, 7, 6, 0, 0],
    [0, 9, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 4, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 2, 5, 0, 0, 7, 0],
    [0, 6, 5, 0, 0, 0, 0, 0, 0],
    [1, 0, 9, 0, 0, 3, 2, 0, 0],
    [7, 0, 0, 0, 0, 4, 9, 5, 0]
]

# 调用函数解决问题
if solve_sudoku(sudoku_board):
    print_board(sudoku_board)
else:
    print("No solution exists")
```



## [递归和回溯算法](https://www.cnblogs.com/fanguangdexiaoyuer/p/11224426.html)

### 递归

```
程序调用自身的编程技巧称为递归（ recursion）。 
递归做为一种算法在程序设计语言中广泛应用。 一个过程或函数在其定义或说明中有直接或间接调用自身的一种方法，它通常把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解，递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算，大大地减少了程序的代码量。
```

### 回溯

```
回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。
```

```python
 #这是一个python版本的回溯的基本框架
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```









# nginx

[书单整理](https://github.com/YunaiV/Blog/blob/master/Books/2019_06_04_Nginx%20%E4%B9%A6%E5%8D%95%E6%95%B4%E7%90%86.md)

## 配置指南

### [配置教程](https://blog.csdn.net/qq_36722955/article/details/116573765)

### [深入理解nginx：模块开发与架构解析](file:///home/yang/ebooks/nginx/)

### [Beginner’s Guide](http://nginx.org/en/docs/beginners_guide.html)

```coffeescript
#/data的结构树
.
├── element-ui
│   ├── assets
│   │   ├── index-CQ2efGjd.css
│   │   └── index-CwQeXXGm.js
│   ├── CNAME
│   ├── element-plus-logo-small.svg
│   ├── favicon.svg
│   ├── index.html
│   └── vite.svg
├── images
│   ├── dir
│   │   └── gmdbs.png
│   └── gmdb.png
├── tree.txt
├── up1
│   └── index.html
└── www
    └── index.html

7 directories, 12 files

#nginx.conf配置文件部分内容
http {
    include /etc/nginx/mime.types;
    server {
        # location / {
        #     root /data/www;
        # }
        location / {
            proxy_pass http://localhost:8080;
        }
        # location /images/ {
        #     root /data;
        #}
        location ~ \.(gif|jpg|png)$ {
            root /data/images;
        }
         location ~ (hello|src|vite) {
             proxy_pass http://localhost:5173;
 }
        location /element-ui/ {
            root /data;
}
    }
    server {
        listen 8080;
        root /data/up1;

        location / {
        }
    }
}
```







# wechat-mini-program

## [微信公众平台](https://mp.weixin.qq.com/)

## [微信开发者参考网站](https://developers.weixin.qq.com/doc/)





# xmind

## [官方博客](https://xmind.cn/blog/)

在经历很久的考虑之后，我还是决定购买了正版的xmindpro，我觉得与其花时间去思考要不要买，还不如直接把它买下来，虽然贵了一点，但它也节省了我思考和其他的时间，也是很有价值的。

## [如何快速掌握XMind?](https://www.zhihu.com/question/325571223/answer/3029510224?utm_psn=1772745758120468480)

## [输入方程](https://xmind.cn/blog/how-to-use-latex-in-xmind/)

如果同时想输入方程和文字的话，就全部都当作方程输入就好了，如果分开来它们会变成独立的两块，不好看

## [在xmind中绘制流程图](https://xmind.cn/blog/make-flow-chart-with-xmind/)



<a name="javascript"> </a>



数据处理
========

[中文实体命名识别工具使用汇总：Stanza、LAC、Ltp、Hanlp、foolnltk、NLTK、BosonNLP](https://blog.csdn.net/weixin_37913042/article/details/112723589)
--------------------------------------------------------------------------------------------------------------------------------------------------

### Stanford CoreNLP 命名实体识别

[使用教程](https://www.52nlp.cn/%E6%96%AF%E5%9D%A6%E7%A6%8F%E5%A4%A7%E5%AD%A6nlp%E7%BB%84python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86%E5%B7%A5%E5%85%B7stanza%E8%AF%95%E7%94%A8)

CoreNLP是Java自然语言处理的一站式服务！CoreNLP使用户能够导出文本的语言注释，包括标记和句子边界、词性、命名实体、数值和时间值、依赖和选区解析、共指、情感、引用属性和关系。CoreNLP的核心是管道。管道接收原始文本，对文本运行一系列NLP注释器，并生成最终的注释集。管道产生核心文档，包含所有注释信息的数据对象，可以通过简单的API访问，并且可以序列化到Google协议缓冲区。

指定pipeline的操作步骤以及对应的语料文件的位置，可以自定义配置文件，再引入代码中。实际上我们可能用不到所有的步骤，或者要使用不同的语料库，因此可以自定义配置文件，然后再引入。那在我的项目中，我就直接读取了该properties文件。（有时候我们只想使用ner功能，但不想使用其他功能，想去掉。然而，Stanford CoreNLP有一些局限，就是在ner执行之前，一定需要tokenize, ssplit, pos, lemma 的引入，大大增加了耗时。）

### [FoolNLTK](https://github.com/rockyzhengwu/FoolNLTK)

这个已经被废弃了，我直接安装以后有环境的问题，它使用的是tensorflow，版本有严重的问题

文本匹配
--------

`re` 是 Python 中用于处理正则表达式的标准库，它允许你在文本中搜索、匹配和操作字符串。下面是 `re` 库的一些基本用法和常见方法：

### 导入模块

首先，需要导入 `re` 模块：

```python
import re
```

### 基本函数和方法

1. **re.match(pattern, string, flags=0)**:

   - 尝试从字符串的起始位置匹配一个模式，如果不在起始位置匹配成功的话，match() 将返回 None。

   ```python
   pattern = r"hello"
   text = "hello world"
   match = re.match(pattern, text)
   if match:
       print("Matched!")
   else:
       print("Not matched.")
   ```

2. **re.search(pattern, string, flags=0)**:

   - 扫描整个字符串，并返回第一个成功的匹配。

   ```python
   pattern = r"world"
   text = "hello world"
   match = re.search(pattern, text)
   if match:
       print("Matched!")
   else:
       print("Not matched.")
   ```

3. **re.findall(pattern, string, flags=0)**:

   - 返回字符串中所有与模式匹配的字符串列表。

   ```python
   pattern = r"\d+"
   text = "There are 123 apples and 456 oranges."
   numbers = re.findall(pattern, text)
   print(numbers)  # ['123', '456']
   ```

4. **re.finditer(pattern, string, flags=0)**:

   - 返回一个迭代器，包含所有与模式匹配的匹配对象。

   ```python
   pattern = r"\d+"
   text = "There are 123 apples and 456 oranges."
   matches = re.finditer(pattern, text)
   for match in matches:
       print(match.group())  # 打印每个匹配对象的字符串形式
   ```

5. **re.sub(pattern, repl, string, count=0, flags=0)**:

   - 替换字符串中的模式匹配项，并返回替换后的字符串。

   ```python
   pattern = r"\d+"
   text = "There are 123 apples and 456 oranges."
   replaced_text = re.sub(pattern, "X", text)
   print(replaced_text)  # There are X apples and X oranges.
   ```

### 正则表达式模式语法

在 `re` 中，正则表达式模式使用特定的语法来描述要匹配的字符串模式。以下是一些常见的模式元字符和语法：

- **普通字符**：字母和数字按照它们的字面意思匹配。
- **`.`**：匹配除换行符 `\n` 外的任何字符。
- **`^`** 和 **`$`**：匹配字符串的开始和结束。
- **`*`, `+`, `?`**：匹配前面的字符零次或多次、一次或多次、零次或一次。
- **`{}`**：指定匹配次数的范围。
- **`[]`**：定义字符集合。
- **`()`**：组合模式并标记一个子组。
- **`\`**：转义字符，用于特殊字符的匹配。

### 示例

```python
import re

text = "The quick brown fox jumps over the lazy dog"

# 查找包含 "fox" 的单词
pattern = r"\bfox\b"
matches = re.findall(pattern, text)
print(matches)  # ['fox']

# 替换所有的元音字母为 "X"
pattern = r"[aeiou]"
replaced_text = re.sub(pattern, "X", text)
print(replaced_text)  # ThX qXXck brXwn fXx jXmps XvXr thX lXzy dXg
```

这些示例展示了如何使用 `re` 库进行基本的文本搜索、匹配和替换操作。正则表达式的语法非常丰富，可以实现复杂的文本处理需求，需要根据具体情况选择合适的模式和方法。


-



<a name="broswer"> </a>









<a name="computer-knowledge"> </a>

### 



# uniapp

## hbuider安装

- 首先去官网下载安装包
- 然后解压（这时注意，可以直接解压到program file文件夹下面，一般在Download下面可能后来会移动，会比较麻烦）
- 下载相关引擎，由于是在program file文件下下载，所以要开启管理员才可以



[electron](https://www.electronjs.org/zh/docs/latest/)
======================================================

npm配置
-------

npm 的配置文件可以存在多个位置，具体的配置文件目录取决于配置的作用范围（全局、用户或项目级别）。以下是常见的 npm 配置文件位置：

### 全局配置文件

全局配置文件保存全局设置，通常位于以下目录：

- **Linux/Mac**：

  ```bash
  /usr/local/etc/npmrc
  ```

- **Windows**：

  ```bash
  %ALLUSERSPROFILE%\npmrc
  ```

### 用户配置文件

用户配置文件保存用户级别的设置，通常位于以下目录：

- **Linux/Mac**：

  ```bash
  ~/.npmrc
  ```

- **Windows**：

  ```bash
  %USERPROFILE%\.npmrc
  ```

### 项目配置文件

项目配置文件保存项目级别的设置，通常位于项目的根目录下：

```bash
<project-root>/.npmrc
```

### 查看配置文件路径

你可以使用以下命令查看所有配置文件的路径：

```bash
npm config get userconfig
npm config get globalconfig
```

这些命令将显示用户和全局配置文件的路径。例如：

```bash
$ npm config get userconfig
/home/username/.npmrc

$ npm config get globalconfig
/usr/local/etc/npmrc
```

### 验证注册表设置

你可以通过以下命令查看当前的注册表设置，以确认是否已更改：

```bash
npm config get registry
```

你应该会看到类似以下的输出：

```text
https://registry.npmmirror.com/
```

### 示例：查看和修改用户配置文件

假设你在 Linux 或 Mac 系统上，你可以打开和编辑 `~/.npmrc` 文件来查看和修改用户级别的配置。你可以使用任何文本编辑器打开这个文件，例如：

```bash
nano ~/.npmrc
```

在 Windows 上，你可以使用命令提示符打开和编辑 `%USERPROFILE%\.npmrc` 文件。例如：

```cmd
notepad %USERPROFILE%\.npmrc
```

编辑 `.npmrc` 文件后，保存更改，然后你可以运行 `npm config get registry` 命令来验证更改是否生效。

通过这些方法，你可以确认和管理 npm 的配置文件及其内容。

安装electron
------------

[在安装的过程中会碰到网络问题，安装很麻烦，最后采用cnpm才安装成功](https://blog.csdn.net/weixin_46645965/article/details/130304508)

这是另一个解决下载慢的方法，[感觉没什么用](https://segmentfault.com/a/1190000020932174)

<a name="网站部署"> </a>

# 网站部署

## 域名备案

1. 在下面的网站购买一个域名

https://wanwang.aliyun.com/domain 

2.  参考下面的网站下载域名证书

https://help.aliyun.com/zh/icp-filing/basic-icp-service/support/the-domain-name-certificate?spm=5176.beian-homepage-app.0.0.6f3f594d3QFPam#section-ej7-czl-8di

3. 从下面的网站进行备案

https://beian.aliyun.com/pcContainer/myorder

4. 注意：备案的时候主题不能选个人

## 新建站点

域名

## 安装软件

php7.4

redis

fileinfo





End
