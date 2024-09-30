# jupyter 配置教程

## 在 Jupyter 中配置并使用 Mathematica 作为内核

### 1. 安装 Mathematica

确保你已经安装了 Mathematica 或者 Wolfram Engine。如果你还没有安装，可以从 [Wolfram 官网](https://www.wolfram.com/)下载 Mathematica 或免费的 Wolfram Engine。

### 2. 安装 Jupyter

如果你还没有安装 Jupyter Notebook，可以通过以下命令来安装它（需要 Python 和 `pip`）：

```bash
pip install jupyter
```

### 3. 安装 WolframLanguageForJupyter 内核

Wolfram 官方提供了一个开源的 Jupyter 内核，名为 WolframLanguageForJupyter。安装步骤如下：

1. **Clone the repository**: 在终端中运行以下命令来克隆内核的 GitHub 仓库：

   ```bash
   git clone https://github.com/WolframResearch/WolframLanguageForJupyter.git
   ```

2. **运行安装脚本**：进入仓库目录并运行安装脚本：

   ```bash
   cd WolframLanguageForJupyter
   ```

   对于 Mathematica，运行以下命令来安装 Wolfram 语言的 Jupyter 内核：

   ```bash
   ./configure-jupyter.wls add
   ```

   > 如果你使用的是 Wolfram Engine（而不是 Mathematica），你可以先通过运行 `wolframscript` 命令来查看 Wolfram Engine 的可执行文件路径，然后用它来运行 `configure-jupyter.wls` 脚本。比如：

   ```bash
   wolframscript -f configure-jupyter.wls add
   ```

3. **验证安装**：确保内核安装成功。可以通过以下命令列出可用的 Jupyter 内核：

   ```bash
   jupyter kernelspec list
   ```

   如果安装成功，你应该能看到 `wolframlanguage` 内核列在内核列表中。

### 4. 在 Jupyter 中使用 Mathematica

1. 打开 Jupyter Notebook：

   ```bash
   jupyter notebook
   ```

2. 新建一个笔记本。在启动时选择 `Wolfram Language` 作为内核。

3. 现在你可以在 Jupyter 笔记本中编写并执行 Mathematica（Wolfram 语言）代码了。例如，输入以下代码来测试：

   ```mathematica
   Plot[Sin[x], {x, 0, 2*Pi}]
   ```

   运行后你应该会看到 Sin 函数的图像。

### 5. 卸载 Wolfram Language 内核

如果你以后不再需要 Wolfram Language 内核，可以通过以下命令将其卸载：

```bash
./configure-jupyter.wls remove
```

## 配置 Node.js 内核来使 Jupyter 支持 JavaScript 代码

### 1. 安装 Node.js

如果你还没有安装 Node.js，请先安装它：

- 访问 [Node.js 官网](https://nodejs.org/)并下载适合你操作系统的最新版本。
- 安装完成后，在命令行中运行以下命令来确认是否安装成功：

  ```bash
  node -v
  npm -v
  ```

### 2. 安装 Jupyter Kernel Gateway

在 Jupyter 中运行 JavaScript 代码需要为 Jupyter 安装 Node.js 内核。这个过程需要借助 `ijavascript`。

1. 打开命令行并全局安装 `iJavaScript` 包：

   ```bash
   npm install -g ijavascript
   ```

2. 安装完成后，运行以下命令以注册 iJavaScript 作为 Jupyter 的内核：

   ```bash
   ijsinstall
   ```

   这会将 Node.js 内核安装到 Jupyter 中。

### 3. 启动 VSCode 的 Jupyter 环境

1. 打开 VSCode，并确保安装了以下两个扩展：

   - **Jupyter** 扩展：用于运行 Jupyter 笔记本。
   - **Python** 扩展：通常和 Jupyter 配合使用。

2. 打开一个 `.ipynb` 笔记本文件，或者新建一个笔记本文件。

3. 在笔记本界面顶部，点击当前的内核名称（通常是 Python），在下拉列表中选择 **JavaScript** 或者 **Node.js**。

   > 如果你没有看到 `Node.js`，请确保你已经按照上面的步骤安装了 `ijavascript`，并且可以通过 `jupyter kernelspec list` 命令确认它已被安装。

### 4. 使用 Node.js 代码

现在你就可以在 Jupyter 笔记本中编写并执行 Node.js（JavaScript）代码了。例如，在一个单元格中输入以下代码：

```javascript
console.log("Hello, Node.js in Jupyter!");
```

然后运行该单元格，你应该会看到控制台输出。

### 5. 检查 Node.js 内核的安装状态

如果你想确认 Node.js 内核是否安装成功，可以使用以下命令列出所有可用的内核：

```bash
jupyter kernelspec list
```

如果看到 `javascript` 或 `nodejs`，说明安装成功。

这样你就可以在 VSCode 的 Jupyter 环境中使用 Node.js 了。
