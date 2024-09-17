# python

[python文档](https://docs.python.org/zh-cn/3.10/)

pytest
------

`pytest` 是一个功能强大的 Python 测试框架，通常在以下情况下使用：

### 适合使用 pytest 的情况：

1. **单元测试：** 对单个函数、类或模块进行测试，验证其行为是否符合预期。

2. **集成测试：** 测试多个组件之间的交互和集成，确保整体系统功能正常。

3. **功能测试：** 针对整个功能或特定功能模块进行测试，模拟用户实际使用场景。

4. **自动化测试：** 编写自动化测试脚本来代替手动测试，提高测试效率和一致性。

### pytest 的详细使用方法：

1. **安装 pytest：** 首先确保已经安装了 Python 和 pip 工具，然后可以使用以下命令安装 pytest：

   ```bash
   pip install pytest
   ```

2. **编写测试代码：** 创建一个或多个以 `test_` 开头的 Python 测试函数或方法，例如：

   ```python
   # test_example.py
   def add(x, y):
       return x + y
   
   def test_addition():
       assert add(2, 3) == 5
       assert add(1, 1) != 3
   ```

3. **运行测试：** 在命令行中进入测试代码所在的目录，然后运行 pytest：

   ```bash
   pytest
   ```

   pytest 将会自动查找并执行当前目录及其子目录中的所有测试文件和测试函数。

4. **断言：** 使用 `assert` 断言来检查测试条件是否为真。pytest 支持丰富的断言方式，如 `assert <expression>`、`assert <expression>, <message>` 等。

5. **参数化测试：** 使用 `@pytest.mark.parametrize` 装饰器进行参数化测试，测试多组输入的情况。

   ```python
   import pytest
   
   @pytest.mark.parametrize("input1, input2, expected", [
       (2, 3, 5),
       (1, 1, 2),
       (0, 0, 0),
   ])
   def test_addition(input1, input2, expected):
       assert add(input1, input2) == expected
   ```

6. **测试运行选项：** pytest 提供多种选项和标记来控制测试的运行，如 `-v`（详细输出）、`-x`（遇到第一个失败即停止）、`-k <expression>`（匹配测试名称模式）、`--maxfail=<num>`（允许最大失败数）等。

7. **测试报告：** pytest 可以生成详细的测试报告，支持多种格式如文本、HTML、JUnit XML 等，通过选项 `-r` 控制输出格式。

8. **扩展和插件：** 可以通过 pytest 的插件系统扩展功能，如参数化、覆盖率、测试运行分布等。

9. **集成 CI/CD：** pytest 可以轻松集成到持续集成和持续部署系统中，如 Jenkins、Travis CI 等，自动运行和监控测试。

通过这些详细的使用方法，你可以更好地利用 pytest 进行 Python 测试，提高代码质量和稳定性。

object
------

在 Python 中，`object` 是所有类的基类，默认情况下所有的类都继承自 `object`。这是因为 Python 是一种面向对象的编程语言，所有的东西都是对象（包括类本身）。以下是 `object` 的一些特征和类型信息：

### 特征

1. **基类**:

   - 所有类都是 `object` 的子类。

   - 如果定义一个类没有显式地继承某个基类，那么它默认继承自 `object`。

   - 示例：

     ```
     pythonCopy codeclass MyClass:
         pass
     
     # 等价于
     class MyClass(object):
         pass
     ```

2. **统一的类型体系**:

   - Python 使用一种统一的类型体系，即所有的类型都派生自 `object`。
   - 这使得各种类型（如整数、列表、用户定义的类等）可以使用通用的接口和功能。

3. **内置方法**:

   - 由于所有类都继承自 

     ```
     object
     ```

     ，它们可以使用 

     ```
     object
     ```

      提供的内置方法。例如：

     - `__str__`: 返回对象的字符串表示。
     - `__repr__`: 返回对象的正式字符串表示（通常可以用来重新创建对象）。
     - `__eq__`: 用于比较两个对象是否相等。
     - `__hash__`: 返回对象的哈希值（如果对象是可哈希的）。
     - `__init__`: 对象初始化方法。

4. **多态和继承**:

   - 通过继承 `object`，可以实现多态，即不同类型的对象可以通过相同的接口进行操作。
   - 可以创建复杂的继承层次，重用和扩展功能。

try机制
-------

`try` 语句是 Python 提供的一种用于处理异常的结构。它允许你捕获和处理在程序运行期间可能发生的异常，从而避免程序崩溃，并能够进行适当的错误处理。这个的帮助非常大，尤其是程序是执行完之后才做从内存到文件的写入的时候，如果中途中断的话可能就要重新来过，而如果使用这个，可以在中断以后触发错误处理机制，及时保存和处理一部分内容，非常有帮助。

### 结构与基本用法

一个典型的 `try` 语句由四个部分组成：`try`、`except`、`else` 和 `finally`。其中 `else` 和 `finally` 是可选的。

```
pythonCopy codetry:
    # 可能引发异常的代码
except ExceptionType1:
    # 当捕获到 ExceptionType1 时执行的代码
except ExceptionType2 as e:
    # 当捕获到 ExceptionType2 时执行的代码，并将异常实例保存到变量 e
else:
    # 如果没有引发任何异常，执行的代码
finally:
    # 无论是否引发异常，都会执行的代码
```

### 详细介绍

1. **`try` 块**：
   - 放置可能引发异常的代码。如果没有异常发生，`try` 块内的所有代码会正常执行。
2. **`except` 块**：
   - 放置处理特定异常的代码。可以有多个 `except` 块来处理不同类型的异常。
   - 可以使用 `except ExceptionType as e` 的形式，将异常实例保存到变量 `e` 中，以便在 `except` 块内进一步处理。
3. **`else` 块**（可选）：
   - 如果 `try` 块没有引发任何异常，`else` 块内的代码会执行。
   - `else` 块通常用于那些不希望在 `try` 块内执行的代码，因为它们只有在 `try` 块成功时才会运行。
4. **`finally` 块**（可选）：
   - 无论 `try` 块是否引发异常，`finally` 块中的代码都会执行。
   - 常用于清理操作，如关闭文件、释放资源等。

文件加密
--------

使用Cython将Python代码编译为C扩展模块后，生成的文件是共享对象文件（.so或.pyd），这些文件不能直接使用Python解释器执行。相反，它们需要作为模块导入到Python脚本中。

### 使用Cython编译和运行Python脚本

1. **安装Cython**：

   ```sh
   pip install cython
   ```

2. **创建`setup.py`文件**：

   创建一个名为`setup.py`的文件，内容如下：

   ```python
   from setuptools import setup
   from Cython.Build import cythonize
   
   setup(
       ext_modules=cythonize("your_script.py")
   )
   ```

3. **编译Python脚本**：

   在命令行中运行以下命令：

   ```sh
   python setup.py build_ext --inplace
   ```

   这将生成一个共享对象文件（.so或.pyd），例如`your_script.cpython-38-x86_64-linux-gnu.so`或`your_script.cp38-win_amd64.pyd`，具体取决于你的Python版本和操作系统。

4. **创建主脚本**：

   创建一个主脚本，用于导入并执行生成的C扩展模块。假设你的Cython编译文件名是`your_script`：

   ```python
   import your_script
   
   # 如果 your_script 有 main 函数或其他入口函数，直接调用
   your_script.main()  # 假设有一个 main 函数
   ```

5. **运行主脚本**：

   在命令行中运行主脚本：

   ```sh
   python main_script.py
   ```

### 示例

假设你有一个`buy.py`脚本，内容如下：

```python
# buy.py
def main():
    print("Executing buy.py script")

if __name__ == "__main__":
    main()
```

#### 创建`setup.py`文件：

```python
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("buy.py")
)
```

#### 编译`buy.py`脚本：

```sh
python setup.py build_ext --inplace
```

这会生成一个名为`buy.cpython-38-x86_64-linux-gnu.so`（或其他相应名称）的共享对象文件。

#### 创建`main.py`文件：

```python
import buy

buy.main()
```

#### 运行`main.py`脚本：

```sh
python main.py
```

这样，你就可以通过编译后的共享对象文件运行Python脚本，同时保护源代码。

python安装包的方法
------------------

1. 最一般的方法是直接使用pip install `package name`来进行安装，但有时候在网络不好的时候
2. 可以采用先把包的“.whl”文件下载下来，然后使用 `python -m pip install package-name.whl`来进行下载

修改浏览器默认的文件夹的路径
----------------------------

### [通过注册表](https://blog.csdn.net/weixin_51623642/article/details/131609755)

在【开始菜单或运行中】输入regedit打开注册表编辑器，展开HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft，查看是否存在Edge文件夹，不存在久右键点击Microsoft，选择【新建 - 项】，命名为Edge。如果存在则无需创建。


右键点击Edge，选择 新建 - 字符串值，命名如下：

DiskCacheDir：设置磁盘缓存目录

UserDataDir ：设置用户数据目录

然后双击修改其数据为指定目录。