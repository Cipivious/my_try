装饰器
======

![image-20240819132806646](https://raw.githubusercontent.com/Cipivious/my_try/main/img/image-20240819132806646.png)

例子
----

```python
import time


def timer(time_type):

    def outer(func):

        def inner(*args, **kwargs): # 这里可以接受不同数量和格式的参数
            start_time = time.time()
            old_result = func(*args, **kwargs) 
            end_time = time.time()
            result = end_time - start_time
            if time_type == "m":
                result = result / 60
            elif time_type == "h":
                result = result / 3600
            elif time_type == "s":
                result = result
            else:
                print("time_type is error!")
            print("runnig time is " + str(result))
            return old_result

        return inner

    return outer


@timer(time_type="s")  # add = timer(time_type="s")(add)
def add(a, b, *args):
    time.sleep(1)
    # a = 2
    # b = 8
    sum = a + b
    for arg in args:
        sum += arg

    return sum


print("the sum is = " + str(add(8, 9, 2, 8, 8)))
```

多线程
======

在选择使用多线程还是多进程时，主要考虑以下几点：

### 1. **任务的性质**

   - **CPU密集型任务**：
     - 任务主要消耗 CPU 资源，如复杂计算、数据处理、图像处理等。
     - **建议使用多进程**。由于 Python 的 Global Interpreter Lock (GIL)，多线程在 CPU 密集型任务中无法有效并行处理，多进程可以绕过 GIL，实现真正的并行处理。

   - **I/O密集型任务**：
     - 任务主要等待 I/O 操作，如文件读写、网络请求、数据库操作等。
     - **建议使用多线程**。多线程在 I/O 密集型任务中能有效提升效率，因为线程可以在等待 I/O 时释放 GIL，让其他线程继续工作。

### 2. **任务的执行环境**

   - **多核环境**：
     - 如果运行环境具有多个 CPU 核心，使用多进程可以更好地利用多个核心的计算能力。
     - **多进程**模式可以充分利用多核 CPU，提供更好的性能。

   - **单核环境**：
     - 在单核 CPU 环境下，多线程可以提供更好的响应性，因为线程切换的开销比进程切换小。
     - **多线程**在这种环境下可能是更好的选择，尤其是 I/O 密集型任务。

### 3. **任务的内存需求**

   - **内存占用较大**：
     - 如果任务需要大量内存，使用多进程会增加内存占用，因为每个进程都有独立的内存空间。
     - **建议使用多线程**，因为线程共享进程的内存空间，避免了不必要的内存复制。

   - **内存共享需求**：
     - 如果任务需要在多个并发执行单元之间共享大量内存数据，**建议使用多线程**，因为线程之间共享内存更方便。

### 4. **代码的复杂度**

   - **进程间通信复杂度**：
     - 多进程需要考虑进程间通信（IPC），如使用队列、管道等。这些机制比线程间通信（共享内存、锁、条件变量等）要复杂。
     - 如果不想增加代码的复杂度，**多线程**可能是更简单的选择。

### 5. **程序的可移植性和稳定性**

   - **跨平台兼容性**：
     - 多进程在不同操作系统上的行为可能有所不同（例如，Windows 不支持 `fork` 系统调用）。
     - 如果需要跨平台支持，**多线程**通常更具可移植性。

   - **稳定性**：
     - 多线程由于共享内存，容易导致数据竞争等并发问题。如果不小心处理，可能导致死锁等复杂问题。
     - **多进程**在稳定性上可能更优，因为进程间数据独立，互不干扰。

### 总结

- **使用多进程**：适合 CPU 密集型任务，或在多核环境下运行时，追求性能提升。
- **使用多线程**：适合 I/O 密集型任务，或任务需要共享大量内存时，追求更高响应性和较低内存开销。

根据实际的任务需求和环境来选择使用多进程或多线程，这样才能充分发挥并发编程的优势。

多线程有几种实现的方式，一种是使用threading来实现，这种在开始的时候往往要自己创建一个线程的类，继承原本的threading中定义的线程的类，要重写里面的run方法来确定要执行的内容，在执行的时候可能还会碰到线程锁这样的调度几个不同的线程的东西，它内部提供了一个local_data的方法，可以快捷的区分不同的线程之间的名称和变量，类似于使用一个字典的形式创建的，每个线程有一个自己独立的变量的字典。至于concurrent.future这个内容的集成度更高一些，可以直接调用里面的线程池来便捷操作。

一般来说，集成度高的东西使用起来更加的方便，而集成度低的东西使用起来则更加的灵活，要结合具体的情况来考虑具体使用哪一个。后面还有一种高并发的实现，时使用的协程的方式，也可以进行参考。

示例代码

```python
# 使用threading
import threading

local_data = threading.local()

local_data.name = "local_data"


class Mythread(threading.Thread):
    def run(self):
        print("赋值前，子进程", threading.current_thread(), local_data.__dict__)
        local_data.name = self.name
        print("赋值后，子进程", threading.current_thread(), local_data.__dict__)


if __name__ == "__main__":
    print("开始前，主进程", local_data.__dict__)

    t1 = Mythread()
    t1.start()
    t1.join()

    t1 = Mythread()
    t1.start()
    t1.join()

    print("开始后，主进程", local_data.__dict__)
    
------------------------------------------------------------------------------------------------------------------------------------
# 使用concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

executor = ThreadPoolExecutor(max_workers=3)

num = 1


def get_html(exe_time, i):
    time.sleep(exe_time)
    return i


# for i in range(10):
#     exe_time = random.random()
#     return_num = executor.submit(get_html, exe_time, i)
#     print("线程{}加载完成".format(return_num.result()))

all_tasks = [executor.submit(get_html, random.random(), i) for i in range(10)]

for item in as_completed(all_tasks):
    print("线程{}加载完成".format(item.result()))
```



协程
====

![image-20240821193752488](https://raw.githubusercontent.com/Cipivious/my_try/main/img/image-20240821193752488.png)

示例代码

```python
import asyncio
import time
import os


async def create_file(file_name):
    with open("txt_file/" + file_name + ".txt", "w", encoding="utf-8") as f:
        pass
    return file_name + "创建完成！"


if __name__ == "__main__":
    start_time = time.time()
    os.makedirs("txt_file")
    tasks = [
        asyncio.ensure_future(create_file("text" + str(i))) for i in range(1, 10001)
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print("result is ：{}".format(task.result()))
    end_time = time.time()
    print("all time needed is {}".format(end_time - start_time))
```

魔术方法
========

示例代码

```python
from typing import Any

class Student:
    __isinstance = False

    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance:
            cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(self)

    def run(self, method):
        if hasattr(self, method):
            try:
                getattr(self, method)()
            except:
                print(getattr(self, method))
        else:
            print("Student 没有这个属性或者方法！")

    # def __repr__(self):
    #     return "class:\t Student\nname:\t {}\nage:\t {}\n".format(self.name, self.age)
    def __repr__(self):
        # self.__getattribute__("age")
        return type(self).__name__ + "[" + str(self.__dict__)[1:-1] + "]"

    def __getattribute__(self, item):
        if item == "age":
            print("又过了一年，{}长大了一岁".format(super().__getattribute__("name")))
            new_age = str(int(super().__getattribute__(item)) + 1)
            super().__setattr__(item, new_age)
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("访问未定义的属性")
        return "default"

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "name":
            print("姓名为{}的对象被创建".format(value))
        self.__dict__[name] = value


stu = Student("张三", "18")
print(stu)
print("")
new_stu = Student("李四", "38")
print(stu)

if sorted(stu.__dir__()) == sorted(dir(stu)):
    print("sorted(stu.__dir__()) = sorted(dir(stu))\n")
else:
    print("sorted(stu.__dir__()) ！= sorted(dir(stu))\n")

new_stu.__dict__["gender"] = "男"
print(stu)
print(stu.age)
print(stu)
print(stu.xxx)
print("-----------------------------")
stu.run("say_hello")
stu.run("name")
print("-----------------------------")


def create_baoshu():
    num = None

    def baoshu():
        nonlocal num
        if not num:
            num = 1
        print(num)
        num += 1

    return baoshu


baoshu = create_baoshu()
setattr(stu, "baoshu", baoshu)
for i in range(5):
    stu.baoshu()

delattr(stu, "baoshu")
try:
    stu.baoshu()
except:
    print("stu没有{}这个方法".format('"baoshu"'))
```

python 中的对象类型
===================

通过定义类型可以帮助触发编辑器自动补全
--------------------------------------

```python
# 在下面这个例子当中，当函数定义里面声明driver的类型以后，find_element触发了自动补全，而后面用这个函数活得的“ele”这个元素虽然没有实际的值，但是还是能够触发下面的自动补全，在函数里面的时候最好做一下变量声明，这样既便于理解，也便于编辑器开启自动补全
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

def find_element_by_id(driver: WebDriver, id: str) -> WebElement:
    return driver.find_element(by=By.ID, value=id)

ele = find_element_by_id(driver=driver, id="submit")

ele.find_element()
```



以下是一些常用的类型名称及其用途，这些类型提示可以帮助编辑器理解变量的预期类型：
--------------------------------------------------------------------------------

### 基本类型

- **`int`**: 整数类型，如 `1`, `2`, `3`
- **`float`**: 浮点数类型，如 `1.0`, `2.5`
- **`str`**: 字符串类型，如 `"hello"`, `"world"`
- **`bool`**: 布尔类型，表示 `True` 或 `False`
- **`None`**: 表示空值，常用于函数的返回类型

### 容器类型

- **`list`**: 列表类型，表示元素有序可变的集合，如 `[1, 2, 3]`
- **`tuple`**: 元组类型，表示元素有序不可变的集合，如 `(1, 2, 3)`
- **`dict`**: 字典类型，表示键值对的无序集合，如 `{"key": "value"}`
- **`set`**: 集合类型，表示元素无序不重复的集合，如 `{1, 2, 3}`

### 类型提示中的泛型容器

- **`List[Type]`**: 表示一个元素类型为 `Type` 的列表，如 `List[int]`
- **`Tuple[Type1, Type2]`**: 表示一个具有固定元素类型的元组，如 `Tuple[str, int]`
- **`Dict[KeyType, ValueType]`**: 表示键为 `KeyType`，值为 `ValueType` 的字典，如 `Dict[str, int]`
- **`Set[Type]`**: 表示元素类型为 `Type` 的集合，如 `Set[str]`

### 其他常用类型

- **`Any`**: 可以代表任意类型，用于类型不确定的情况下
- **`Union[Type1, Type2]`**: 表示一个变量可以是 `Type1` 或 `Type2`，如 `Union[str, int]`
- **`Optional[Type]`**: 表示一个变量可以是 `Type` 或 `None`，如 `Optional[int]`（等同于 `Union[int, None]`）
- **`Callable[[ArgType1, ArgType2], ReturnType]`**: 表示一个函数类型，其参数为 `ArgType1` 和 `ArgType2`，返回值为 `ReturnType`

常见python库用法总结
====================

之前我在爬虫模块学过一些python的标准库，但是当时还并不理解深刻，我准备看视频重新学习一次，下面是我的学习笔记。

os[模块](https://www.bilibili.com/video/BV15Y411s7t9/?spm_id_from=333.337.search-card.all.click&vd_source=7e6cfdab613c324e6f610acca57d1135)
-------------------------------------------------------------------------------------------------------------------------------------------

### os

os.rename

os.renames 这个和上面的是一组用于文件的重命名，区别主要在于下面的可以创建新的不存在的文件夹，上面的没有对应的文件夹会报错

os.remove 这个用于移除简单的文件

os.rmdir 这个用于移除空的文件夹

os.removedir 这个也是用于移除空的文件夹，但是这个会递归的移除

os.mkdir 这个用于创建目录

os.listdir 列出文件夹中所有的文件

os.getcwd 获取当前工作路径

os.chdir 切换路径

os.system 执行系统命令

一般文件直接用open创建，不适用os模块

### path

os.path.getcurrentdir 类似于这样，获取当前目录

os.path.exists 是否存在某一个文件或者文件夹

os.path.is(dir file abs) 是否是目录，文件，绝对路径

os.path.split(text) 用于分离文件的名称和文件夹的名称

os.path.join 这个用于拼接两个字符串组成一个路径

os.path.basename 获取文件名或文件夹名

os.path.dirname 获取路径

![image-20240824095125937](https://raw.githubusercontent.com/Cipivious/my_try/main/img/image-20240824095125937.png)

[时间模块](https://www.bilibili.com/video/BV1TW41137nD/?spm_id_from=333.337.search-card.all.click&vd_source=7e6cfdab613c324e6f610acca57d1135)
---------------------------------------------------------------------------------------------------------------------------------------------

### time

time.time() 获取当前的时间戳

time.localtime(时间戳) 这个用于把一个时间戳转换成一个时间元组

time.strftime() 这个用于把一个时间戳转换成一个格式化的时间字符串

time.strptime() 这个用于把一个时间字符串转换成一个时间的元组

time.mktime() 这个用于把时间元组转换成一个时间戳

![image-20240824101304091](https://raw.githubusercontent.com/Cipivious/my_try/main/img/image-20240824101304091.png)

### calendar

month 这个用于打印某一个月份的日历

re模块
------

### 直接使用方式

re.match(pattern, string) 这个会从第一个字符开始匹配，如果不符合就返回None

re.findall(pattern, string) 这个会匹配所有的，返回一个列表

re.search(pathern, string) 这个会匹配第一个搜索到的，但是并不限定是第一个字符

**`re.findall`**: 返回所有匹配项的列表。如果有捕获组，则返回捕获组的列表。

**`re.finditer`**: 返回所有匹配项的迭代器，每个匹配项都是一个 `Match` 对象，你可以通过这个对象获取更多信息（比如匹配的起始位置、结束位置等）。(迭代器是动态加载，动态产生的，并不是一次加载所有的，比较节约内存空间)

re.split 这个用于分割一个字符串，默认是使用匹配到的元组来进行分割，也可以使用其他模式字符来进行分割，分割之后生成对应的列表

re.sub 这个是用于替换的，他有一个回调函数，可以在替换以后执行相应的操作，类似threading 的线程池在返回以后可以执行一个回调函数一样，也可以直接用简单的字符串替换匹配到的内容

迭代器使用示例

```python
import re

content = """
<html>
<head>
<title>Title 1</title>
</head>
<body>
<p>Paragraph 1</p>
<p>Paragraph 2</p>
</body>
</html>
"""

# 使用 finditer 来获取所有匹配的 <p> 标签
matches = re.finditer(r"<p>(.*?)</p>", content)

for match in matches:
    print(f"Matched content: {match.group(1)} at position {match.start()} to {match.end()}")
```

### 使用compile匹配对象的模式

首先使用使用res = re.compile(pattern)将模式生成一个模式对象，之后利用对象来进行操作

res.search, res.match, res.finditer, res.findall, 使用的方法和上面是类似的

json模块
--------

```python
# 直接使用一般采用 dumps, loads, 前者用于把字典转换成字符串，后者用于把字符串转换成字典
# 从文件中读写一般采用 dump, load， 前者用于写入，后者用于读取
import json

dog = {"name": "xiaohuang", "age": "1", "gender": "famale"}

dog_info = json.dumps(dog)
print(dog_info)

dog_info = dog_info[:-1] + ', "hobby": "eat"}'
print(dog_info)

dog = json.loads(dog_info)
print(dog)

with open("./dog.json", "w", encoding="utf-8") as f:
    json.dump(dog, f)

with open("./dog.json", "r", encoding="utf-8") as f:
    dog = json.load(f)

print(dog)
```

字符串定义模块
--------------

在 Python 中，定义字符串有多种方法，主要包括单引号、双引号、三引号（用于多行字符串）以及通过不同的前缀（如 `r`、`u`、`f` 等）来创建不同类型的字符串。下面是详细介绍：

### 1. 单引号 (`'`) 和双引号 (`"`)
- **定义方式**:
  ```python
  s1 = 'Hello, World!'
  s2 = "Hello, World!"
  ```
- **背后原理**:
  - 在 Python 中，单引号和双引号定义的字符串没有区别，它们是完全等价的。这使得代码书写更加灵活，特别是在字符串中包含引号时。
  - 例如，单引号字符串中可以包含双引号，反之亦然：
    ```python
    s3 = "He said, 'Hello!'"
    s4 = 'She replied, "Hi!"'
    ```

### 2. 三引号 (`'''` or `"""`)
- **定义方式**:
  ```python
  s3 = '''This is a multi-line string.
  It can span multiple lines.'''
  
  s4 = """This is another multi-line string.
  It also spans multiple lines."""
  ```
- **背后原理**:
  - 三引号字符串允许定义多行字符串，内部可以包含换行符和其他引号，而不需要使用转义字符。
  - 三引号字符串常用于文档字符串（docstring），即函数或类的说明文档。

### 3. 原始字符串 (`r` or `R` 前缀)
- **定义方式**:
  ```python
  s5 = r'C:\Users\Name\Desktop\New Folder'
  s6 = R'C:\Users\Name\Desktop\New Folder'
  ```
- **背后原理**:
  - 原始字符串保持字符串的原始形式，忽略转义字符。这在处理正则表达式或文件路径时非常有用，因为你不需要为反斜杠 (`\`) 使用双重转义。
  - 例如，普通字符串 `C:\\Users\\Name` 在原始字符串中可以直接写为 `r'C:\Users\Name'`。

### 4. Unicode 字符串 (`u` or `U` 前缀)
- **定义方式**:
  ```python
  s7 = u'Hello, World!'
  s8 = U'Hello, World!'
  ```
- **背后原理**:
  - 在 Python 3.x 中，所有字符串默认都是 Unicode，因此 `u` 前缀通常不再需要。但在 Python 2.x 中，`u` 前缀用于定义 Unicode 字符串，以支持多语言字符集。
  - 例如，`u'你好'` 在 Python 2.x 中表示 Unicode 字符串，而 `'你好'` 则是字节字符串。

### 5. 格式化字符串 (`f` or `F` 前缀)
- **定义方式**:
  ```python
  name = "John"
  s9 = f'Hello, {name}!'
  s10 = F'Hello, {name}!'
  ```
- **背后原理**:
  - 格式化字符串（f-string）允许在字符串中直接嵌入表达式，使用 `{}` 包围。这些表达式在运行时被计算，并替换为对应的值。
  - f-string 在 Python 3.6 引入，比之前的 `%` 和 `str.format()` 方法更简洁高效。

### 6. 字节字符串 (`b` or `B` 前缀)
- **定义方式**:
  ```python
  s11 = b'Hello, World!'
  s12 = B'Hello, World!'
  ```
- **背后原理**:
  - 字节字符串用于表示二进制数据，而不是文本数据。在 Python 3.x 中，字节字符串以 `b` 或 `B` 开头，并使用 ASCII 编码。
  - 字节字符串与普通字符串不同，无法直接与普通字符串进行拼接或比较。

### 7. 三引号和格式化字符串的组合
- **定义方式**:
  ```python
  name = "John"
  s13 = f'''Hello, {name}!
  Welcome to the Python world.'''
  ```
- **背后原理**:
  - 你可以将 f-string 和三引号结合使用，以创建多行格式化字符串。

这些不同的字符串定义方式为 Python 编程提供了极大的灵活性，可以根据具体需求选择最合适的方法。

python包管理
------------

要将自己的配置写成一个 Python 包，并使用 `pip` 安装，可以按照以下步骤操作：

### 1. 创建项目目录结构

首先，创建一个新的项目目录，通常结构如下：

```
myconfig/
│
├── myconfig/             # 包的源代码目录
│   ├── __init__.py       # 包的初始化文件
│   └── config.py         # 你定义的配置文件
│
├── tests/                # 测试目录
│   └── test_config.py    # 测试脚本
│
├── setup.py              # 包的安装脚本
├── README.md             # 包的说明文档
└── LICENSE               # 许可证文件（可选）
```

### 2. 编写配置代码

在 `myconfig/myconfig/` 目录中编写你的配置代码，例如 `config.py`：

```python
# myconfig/config.py

def get_default_config():
    return {
        'setting1': 'value1',
        'setting2': 'value2',
    }
```

### 3. 编写 `setup.py`

`setup.py` 文件用于定义包的安装方式。这里是一个基本的 `setup.py` 示例：

```python
# setup.py

from setuptools import setup, find_packages

setup(
    name='myconfig',
    version='0.1.0',
    packages=find_packages(),
    description='My custom configuration package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/myconfig',  # 替换为你的仓库URL
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
```

### 4. 创建 `README.md` 和 `LICENSE`

为你的包创建一个简单的 `README.md` 文件，描述包的用途和使用方法。选择一个适合的许可证（如 MIT 许可证），并在 `LICENSE` 文件中包含相关内容。

### 5. 构建和打包

使用 `setuptools` 构建和打包你的项目：

```bash
# 进入项目目录
cd myconfig

# 安装打包工具
pip install setuptools wheel

# 构建包
python setup.py sdist bdist_wheel
```

这将在 `dist/` 目录中生成 `.tar.gz` 和 `.whl` 文件，这些文件可以用于安装或发布。

### 6. 安装和测试包

使用 `pip` 安装刚刚构建的包：

```bash
pip install dist/myconfig-0.1.0-py3-none-any.whl
```

安装后，你可以在 Python 中导入并使用你的配置包：

```python
import myconfig.config as config

cfg = config.get_default_config()
print(cfg)
```

### 7. 发布到 PyPI（可选）

如果你希望将包发布到 [PyPI](https://pypi.org/)，可以使用 `twine`：

```bash
# 安装 twine
pip install twine

# 发布包
twine upload dist/*
```

在发布之前，你需要在 [PyPI](https://pypi.org/account/register/) 上创建一个账户，并使用该账户的凭据进行登录。

完成这些步骤后，你的包将可通过 `pip` 进行安装和使用。

你可以通过 `pip` 直接从 GitHub 仓库安装 Python 包。要实现这一点，可以使用以下命令：

```bash
pip install git+https://github.com/Cipivious/myconfig.git
```

这条命令会直接从你的 GitHub 仓库中下载并安装 `myconfig` 包。

### 重要提示

1. **确保 `setup.py` 文件正确**: `setup.py` 文件需要正确配置，才能让 `pip` 成功安装包。

2. **版本控制**: 你可以指定一个特定的分支、标签或提交哈希来安装特定版本。例如：

   - 安装某个分支的代码:
     ```bash
     pip install git+https://github.com/Cipivious/myconfig.git@branch_name
     ```
   - 安装某个标签的代码:
     ```bash
     pip install git+https://github.com/Cipivious/myconfig.git@v1.0.0
     ```
   - 安装某个特定提交的代码:
     ```bash
     pip install git+https://github.com/Cipivious/myconfig.git@commit_hash
     ```

3. **更新包**: 如果你在 GitHub 仓库中对包进行了更新，可以使用以下命令来更新本地安装的版本：
   ```bash
   pip install --upgrade git+https://github.com/Cipivious/myconfig.git
   ```

通过以上方法，你可以很方便地通过 `pip` 从 GitHub 仓库中安装和管理自己的 Python 包。

sys模块
-------

sys.version 获取python的版本

sys.argv 获取命令的参数，返回一个列表，包括python文件的名称

sys.platform 获取运行平台的名称

sys.path 获取python运行的环境变量的路径，返回一个列表

matplotlib模块
--------------

```python
# 画图的时候可以先从官网上面找类似类型的图片，然后下载下来之后修改绘制
# 设置字体 font_prop = font_manager.FontProperties(fname=r"C:\Windows\Fonts\msjh.ttc")
# plot 折线图
# scatter 散点图
# hist 直方图
# bar 柱形图
# tick设置的时候第一个参数表示tick的位置，第二个是想要标注的对应的值，二者都是列表
from matplotlib import pyplot as plt
import random
import math
import time
from matplotlib import font_manager

font_prop = font_manager.FontProperties(fname=r"C:\Windows\Fonts\msjh.ttc")

y = []
x = []
num = 1
base_num = 1
x_label = []
other_y = []
for i in range(20):
    if i > 13:
        x.append(num)
    y.append(base_num)
    other_y.append(base_num * random.uniform(0.9, 1.1))
    x_label.append(f"12点{i+1}分")
    num = num * math.e
    base_num = base_num * math.e

plt.figure(figsize=(20, 8))
plt.yticks(x)
plt.xticks(
    ticks=range(len(x_label)), labels=x_label, rotation=270, fontproperties=font_prop
)
plt.xlabel("时间", fontproperties=font_prop)
plt.ylabel("强度", fontproperties=font_prop)
plt.grid()
plt.title("强度随温度的变化图", fontproperties=font_prop)
plt.plot(range(20), y, label="line1")
plt.scatter(range(20), other_y, label="line2")
plt.legend()
plt.show()
plt.close()
plt.figure(figsize=(20, 8))
plt.yticks(x)
plt.xticks(
    ticks=range(len(x_label)), labels=x_label, rotation=270, fontproperties=font_prop
)
plt.xlabel("时间", fontproperties=font_prop)
plt.ylabel("强度", fontproperties=font_prop)
plt.grid()
plt.title("强度随温度的变化图", fontproperties=font_prop)
bar_width = 0.2
plt.bar(range(20), y, label="line1", width=bar_width)
plt.bar([i + bar_width for i in range(20)], other_y, label="line2", width=bar_width)
plt.legend()
plt.show()
```

numpy模块
---------

```python
# 生成ndarray数据结构 np.array(list对象)
# 获取对应的形状以及重新定义形状，形状参数是一个元组，对应函数是shape,reshape
# 从文件中加载的函数时loadtxt里面有类型，分隔符，是否转置等参数
# 构造一些特殊的ndarray的数据，比如ones， zeros， eyes， randn等等，生成随机数的时候可以使用seed随机数种子来生成相同的随机数
# 拼接有两种，一种是水平（hstack）另一种是垂直（vstack）
# 利用布尔值来做切片索引，相当于先通过计算得到一个和原来的数据形状一样的只包含bool型类型的数据，然后进行索引
import numpy as np
from numpy import ndarray

us_data = np.loadtxt("./us_data.csv", dtype="int", delimiter=",")
uk_data = np.loadtxt("./uk_data.csv", dtype="int", delimiter=",")

zeros = np.zeros((us_data.shape[0], 1), dtype="float")
ones = np.ones((uk_data.shape[0], 1), dtype="float")

us_data = np.hstack((us_data, zeros))
uk_data = np.hstack((uk_data, ones))

data = np.vstack((us_data, uk_data))
# print(np.asarray(data.mean(axis=0), dtype="int"))
data[1, 2:] = np.nan
print(data)


def fill_ndarray(data: ndarray):
    for i in range(data.shape[1]):
        temp = data[:, i]
        nan_num = np.count_nonzero(temp != temp)
        if nan_num != 0:
            temp_not_non_col = temp[temp == temp]
            temp[np.isnan(temp)] = temp_not_non_col.mean()
    return data


data = fill_ndarray(data)
print(data)
```

pandas模块
----------

### pandas的基础对象是Series， DataFrame对象是Series 的容器

![image-20240825101915914](https://raw.githubusercontent.com/Cipivious/my_try/main/img/image-20240825101915914.png)

### 分组聚合的操作

groupby 通过一个columns的列名可以进行分组，分组返回的是一个可以迭代的对象，里面是元组，元组里面分别是类别以及对应的dataframe数据。

这个分类得到的数据可以直接调用各种数据处理方法进行处理，比如count可以统计各个数据

由于分组之后得到了dataframe对象，所以可以在分组之后继续循环进行分组的处理

### 对对应的元素进行单独的处理

```python
import pandas as pd

# 假设这是你的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# 定义处理函数
def process_value(x):
    return x * 2  # 示例：将每个值乘以2

# 使用 apply 方法对 DataFrame 的某一列进行操作
df['A'] = df['A'].apply(process_value)

print(df)
```

迭代器的通用方法
----------------

在 Python 中，有几种内置的方法可以将函数应用到迭代器的每个元素上。这些方法可以用于不同的操作，如映射、过滤、聚合等。以下是这些方法的详细介绍：

### 1. `map()`

**用途**: 将一个函数应用到可迭代对象的每个元素，返回一个迭代器。

```python
nums = [1, 2, 3, 4]
result = map(lambda x: x * 2, nums)
print(list(result))  # 输出: [2, 4, 6, 8]
```

### 2. `filter()`

**用途**: 过滤可迭代对象中的元素，返回一个只包含函数返回 `True` 的元素的迭代器。

```python
nums = [1, 2, 3, 4]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))  # 输出: [2, 4]
```

### 3. `reduce()`

**用途**: 将函数连续应用于可迭代对象的元素，最终将其归约为一个单一值。`reduce()` 在 Python 3 中位于 `functools` 模块中。

```python
from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums)
print(result)  # 输出: 10
```

### 4. `all()`

**用途**: 检查可迭代对象的所有元素是否都为 `True`。

```python
nums = [1, 2, 3, 4]
result = all(x > 0 for x in nums)
print(result)  # 输出: True
```

### 5. `any()`

**用途**: 检查可迭代对象的至少一个元素是否为 `True`。

```python
nums = [0, 2, 3, 4]
result = any(x > 0 for x in nums)
print(result)  # 输出: True
```

### 6. `zip()`

**用途**: 将多个可迭代对象的元素打包成元组，返回一个迭代器。

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = zip(list1, list2)
print(list(result))  # 输出: [(1, 'a'), (2, 'b'), (3, 'c')]
```

### 7. `enumerate()`

**用途**: 将可迭代对象的每个元素与其索引值打包，返回一个迭代器。

```python
words = ['a', 'b', 'c']
result = enumerate(words)
print(list(result))  # 输出: [(0, 'a'), (1, 'b'), (2, 'c')]
```

### 8. `sorted()`

**用途**: 对可迭代对象进行排序，返回一个新的排序后的列表。

```python
nums = [4, 1, 3, 2]
result = sorted(nums)
print(result)  # 输出: [1, 2, 3, 4]
```

### 9. `reversed()`

**用途**: 返回一个反转过的迭代器。

```python
nums = [1, 2, 3, 4]
result = reversed(nums)
print(list(result))  # 输出: [4, 3, 2, 1]
```

### 10. `itertools.starmap()`

**用途**: 类似于 `map()`，但适用于接受多个参数的函数。位于 `itertools` 模块中。

```python
import itertools

pairs = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(lambda x, y: x + y, pairs)
print(list(result))  # 输出: [3, 7, 11]
```

### 11. `itertools.accumulate()`

**用途**: 对可迭代对象的元素进行累计操作，返回一个迭代器。位于 `itertools` 模块中。

```python
import itertools

nums = [1, 2, 3, 4]
result = itertools.accumulate(nums, lambda x, y: x + y)
print(list(result))  # 输出: [1, 3, 6, 10]
```

这些方法为处理迭代器中的元素提供了强大的工具，允许你使用函数式编程风格来操作数据。

pillow模块
----------

```python
# 下面这个可以自定义的制作一个mask，这个mask可以根据需要来进行定制，然后通过mask调用paste方法，可以把一张图片粘贴到一张白色背景的图片上面，从而可以实现让图像变成圆角，ImageFilter的作用是一个过滤器，可以对图像进行边缘美化，模糊处理等等操作
# 更多的代码可以从 hello_python 中的pillow模块中找到
from PIL import Image, ImageDraw, ImageFilter

# 打开原始图像
img = Image.open("./cat.png").convert("RGBA")

# 创建一个白色背景的图像，与原图大小相同
white_background = Image.new("RGBA", img.size, "white")

# 创建一个遮罩图像，与原图大小相同
mask = Image.new("L", img.size, 0)

# 创建绘图对象
draw = ImageDraw.Draw(mask)
w, h = img.size
# 设置圆角的半径
corner_radius = 50

# # 绘制圆角矩形的遮罩
# draw.rounded_rectangle([(0, 0), img.size], radius=corner_radius, fill=255)
draw.pieslice((0, 0, corner_radius, corner_radius), start=180, end=270, fill=255)
draw.pieslice((0, h - corner_radius, corner_radius, h), start=90, end=180, fill=255)
draw.pieslice((w - corner_radius, h - corner_radius, w, h), start=0, end=90, fill=255)
draw.pieslice((w - corner_radius, 0, w, corner_radius), start=270, end=360, fill=255)
draw.rectangle((0, corner_radius / 2, w, h - corner_radius / 2), fill=255)
draw.rectangle((corner_radius / 2, 0, w - corner_radius / 2, h), fill=255)

# 对遮罩进行模糊处理，使边缘更加平滑
mask = mask.filter(ImageFilter.DETAIL)

# 将原图粘贴到白色背景上，并使用遮罩
white_background.paste(img, (0, 0), mask=mask)

# 转换为RGB模式去掉透明度
final_img = white_background.convert("RGB")

# 显示最终的圆角图像
final_img.show()
```

logging模块
-----------

![image-20240826102011949](https://raw.githubusercontent.com/Cipivious/my_try/main/img/image-20240826102011949.png)

使用logging一般有两种方式，一种是函数式编程的方式，一种是配置文件的方式，后期一般会采用配置文件的方式，因为这种的可维护性更高，一般来说只需要复制配置文件，到需要用到的地方调用既可。一般的简单的则不要写logger， 直接使用logging来做debug即可

```python
import logging

logger = logging.getLogger("applog")
logger.setLevel(logging.DEBUG)

consoleHander = logging.StreamHandler()
consoleHander.setLevel(logging.WARNING)

fileHander = logging.FileHandler(filename="new_demo.log")

formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
flt = logging.Filter("appm")
consoleHander.setFormatter(formatter)
fileHander.addFilter(flt)
fileHander.setFormatter(formatter)

logger.addHandler(consoleHander)
logger.addHandler(fileHander)

logger.debug("this is a debug log")
logger.info("this is an info log")
logger.warning("this ia a warning log")
logger.error("this is an error log")
logger.critical("this is a critical log")
```

config配置模块
--------------

配置有几种常见的模式，不如yaml， json， xml， 还有一些采用txt格式的，我觉得最好还是采用json格式的，这种格式的时候，写到文件里的时候是json格式的，读出来也直接是一个字典，感觉很方便，我准备之后的配置文件都采取json格式的，vscode， 网页开发中使用的格式往往也是json格式的，我最近也比较喜欢字典这种格式，之后可以好好开发一下它的潜力.

以下是四种常用的配置的方式,配置的方式主要是为了避免重复,以及理清自己的思路,之后我在写一些内容的时候都要善于使用配置文件文件的方式,来增强我的代码的强健性,可以最小限度的修改代码,主要修改配置文件,最好能够做到在做改动的时候只修改配置文件的内容,而不用修改代码里面的内容.

```yaml
# : 表示键值对
# - 表示列表
# 其他的地方的单个元素是纯值
key:
	value1: 1
	value2: 3
	value3: 5
	
key2:
	- value1
	- value2
	- value3
```

```ini
[test]
ip=127.0.0.1
port=8000

[production]
ip=47.93.85.206
port=80
```

```json
{
  "dog": {
    "__comment": "这是一个小狗的配置",
    "name": "xiaoli",
    "age": "18",
    "gender": "famale"
  }
}
```

```python
# config.py
test = {
    "ip": "127.0.0.1",
    "port": "8000"
}

production = {
    "ip": "47.93.85.206",
    "port": "80"
}
```

argparse模块
------------

```python
import argparse
import json

if __name__ == "__main__":
    # 读取默认的配置
    file = open("./config.json", "r", encoding="utf-8")
    config = json.load(file)
    file.close()
    # 从命令行加载配置,default 后面是默认的配置，如果命令行没有的话
    parser = argparse.ArgumentParser()
    parser.add_argument("--first-arg", default=config["argparser"]["first_arg"])
    parser.add_argument("--secend-arg", default=config["argparser"]["secend_arg"])
    # 将parser解析成一个namespaces对象
    args = parser.parse_args()
    # print(args)
    # 这个可以吧args变成一个字典然后遍历它的键值对
    # for key, arg in vars(args).items():
    #     print(key)
    #     print(arg)
    # 用这种方法可以获取对应的参数的值
    print(args.first_arg)
    print(args.secend_arg)
```

加密算法
--------

在Python中，常见的几种加密算法可以通过以下库实现：

1. **哈希算法**：
   - **SHA-256, SHA-512, MD5等**：可以使用`hashlib`库来实现。
   ```python
   import hashlib
   
   # SHA-256
   hash_object = hashlib.sha256(b'Your data here')
   hash_digest = hash_object.hexdigest()
   print(hash_digest)
   ```

2. **对称加密算法**：
   - **AES, DES等**：可以使用`PyCryptodome`库来实现。
   ```python
   from Crypto.Cipher import AES
   
   key = b'Sixteen byte key'
   cipher = AES.new(key, AES.MODE_EAX)
   nonce = cipher.nonce  # 在加密时生成的随机数
   ciphertext, tag = cipher.encrypt_and_digest(b'Your data here')
   
   # 解密
   cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
   plaintext = cipher_dec.decrypt(ciphertext)
   print(plaintext.decode())
   ```
   
3. **非对称加密算法**：
   - **RSA**：可以使用`PyCryptodome`库来实现。
   ```python
   from Crypto.PublicKey import RSA
   from Crypto.Cipher import PKCS1_OAEP
   
   key = RSA.generate(2048)
   cipher_rsa = PKCS1_OAEP.new(key)
   encrypted_message = cipher_rsa.encrypt(b'Your data here')
   ```

4. **HMAC（基于哈希的消息认证码）**：
   - 可以使用`hmac`库来实现。
   ```python
   import hmac
   import hashlib
   
   key = b'secret_key'
   message = b'Your data here'
   hmac_object = hmac.new(key, message, hashlib.sha256)
   print(hmac_object.hexdigest())
   ```

这些库和方法可以帮助你在Python中实现各种常见的加密算法。

faker模块
---------

这一块主要用于生成随机的数据，[这是一个教程](https://www.bilibili.com/video/BV1K94y127vx/?spm_id_from=333.337.search-card.all.click&vd_source=7e6cfdab613c324e6f610acca57d1135)， [这个是官方的文档](https://faker.readthedocs.io/en/master/#indices-and-tables)，下面是一个示例，

```python
from faker import Faker
import random

fake = Faker(locale="zh_CN")
student_informations = [(fake.name(), random.randint(16, 25), random.choice(["男", "女"]), fake.email()) for i in range(10)]
```

enum模块
--------

这一块是可以给元组里面的变量来进行命名的，其实也可以做一些一般的有规则的变量的命名，比如第一错误的代码，比如定义网络通信协议的代号，就像这样的一组代号，都可以利用这个库来进行简单的划归和命名，不过有的时候如果写在包里面，很多时候会把变量划归在具体的类下面，不过在大多数时候，自己简单使用的时候可以通过这种方式来进行简化操作，下面是一个例子：

```python
# 这里面的具体的数据是使用上面的faker来进行生成的
from enum import IntEnum

class StudentEnum(IntEnum):
    Name, Age, Gender, Email = range(4)
   
for student_information in student_informations:
    print("name", student_information[StudentEnum.Name], "age", student_information[StudentEnum.Age], "gender", student_information[StudentEnum.Gender], "email", student_information[StudentEnum.Email])
    
-------------------------------下面是一个输出的结果----------------------------------------------

name 王东 age 19 gender 女 email jing62@example.net
name 祝玉 age 16 gender 女 email zhu@example.org
name 金红梅 age 16 gender 女 email jiehe@example.com
name 蔡玉 age 24 gender 男 email eyi@example.net
name 徐璐 age 24 gender 男 email ddong@example.net
name 郭淑华 age 21 gender 男 email yhou@example.net
name 张华 age 20 gender 女 email daiqiang@example.net
name 鞠欢 age 18 gender 女 email tliao@example.com
name 卢帅 age 24 gender 男 email pingcui@example.com
name 周兰英 age 17 gender 女 email syu@example.com
```

property模块
------------

![image-20240830173910404](https://raw.githubusercontent.com/Cipivious/my_try/main/img/image-20240830173910404.png)

