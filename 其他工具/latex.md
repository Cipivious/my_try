# latex

## 数学表达式书写

当在 LaTeX 中书写数学表达式时，可以使用多种命令和环境来表示各种数学符号和结构。下面是一些常用的数学表达式的书写方法：

### 求和

```latex
\sum_{i=1}^{n} x_i
```

表示从 1 到 n 的求和：\[ \sum_{i=1}^{n} x_i \]

### 积分

```latex
\int_{a}^{b} f(x) \, dx
```

表示从 a 到 b 的函数 f(x) 的积分：\[ \int_{a}^{b} f(x) \, dx \]

### 求导

```latex
\frac{d}{dx} f(x)
```

表示对函数 f(x) 求导：\[ \frac{d}{dx} f(x) \]

### 求偏导数

```latex
\frac{\partial}{\partial x} f(x, y)
```

表示对函数 f(x, y) 求 x 的偏导数：\[ \frac{\partial}{\partial x} f(x, y) \]

### 多重积分

```latex
\iint_{D} f(x, y) \, dx \, dy
```

表示对区域 D 上的函数 f(x, y) 进行二重积分：\[ \iint_{D} f(x, y) \, dx \, dy \]

### 矩阵

```latex
\begin{pmatrix}
  a & b \\
  c & d
\end{pmatrix}
```

表示一个 2x2 的矩阵：\[ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \]

#### 输入多行矩阵

```latex
A_{m,n} = 

\begin{pmatrix} 

a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\ 

a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\ 

\vdots & \vdots & \ddots & \vdots \\ 

a_{m,1} & a_{m,2} & \cdots & a_{m,n} 

\end{pmatrix}
```

效果如图

![image-20240514150942458](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240514150942458.png)

### 分数

```latex
\frac{a}{b}
```

表示分数 a/b：\[ \frac{a}{b} \]

### 开方

```latex
\sqrt{n}
```

表示 n 的平方根：\[ \sqrt{n} \]

### 上下标

```latex
x^{2}, x_{1}
```

表示 x 的平方和 x 的下标 1：\[ x^{2}, x_{1} \]

### 等号、不等号、箭头

```latex
x = y, x \neq y, x \rightarrow y
```

表示等号、不等号、箭头：\[ x = y, x \neq y, x \rightarrow y \]

### 矢量表示

通常可以使用 `\mathbf{}` 命令来表示加粗的矢量。下面是一个示例：

```latex
\mathbf{v}
```

### 撇

在 LaTeX 中，可以使用 `^{\prime}` 来表示右上角添加一个撇。下面是一个示例：

```latex
x^{\prime}
```

$$
Re_v^{\prime}=\sum_\rho (Re_\rho)S_{\rho v}=\sum_{\mu \rho}e_\mu D_{\mu \rho}(R)S_{\rho v}
$$



LaTeX 还支持各种数学函数、符号和操作符，如三角函数、对数、极限、向量等，你可以根据需要查阅相关文档或书籍，探索更多的数学表达式书写方法。

## 希腊字母

以下是常用的希腊字母及其 LaTeX 表示方法：

1. **小写字母**：
   - α：`\alpha`
   - β：`\beta`
   - γ：`\gamma`
   - δ：`\delta`
   - ε：`\epsilon`
   - ζ：`\zeta`
   - η：`\eta`
   - θ：`\theta`
   - ι：`\iota`
   - κ：`\kappa`
   - λ：`\lambda`
   - μ：`\mu`
   - ν：`\nu`
   - ξ：`\xi`
   - ο：`\omicron`
   - π：`\pi`
   - ρ：`\rho`
   - σ：`\sigma`
   - τ：`\tau`
   - υ：`\upsilon`
   - φ：`\phi`
   - χ：`\chi`
   - ψ：`\psi`
   - ω：`\omega`

2. **大写字母**：
   - Α：`\Alpha`
   - Β：`\Beta`
   - Γ：`\Gamma`
   - Δ：`\Delta`
   - Ε：`\Epsilon`
   - Ζ：`\Zeta`
   - Η：`\Eta`
   - Θ：`\Theta`
   - Ι：`\Iota`
   - Κ：`\Kappa`
   - Λ：`\Lambda`
   - Μ：`\Mu`
   - Ν：`\Nu`
   - Ξ：`\Xi`
   - Ο：`\Omicron`
   - Π：`\Pi`
   - Ρ：`\Rho`
   - Σ：`\Sigma`
   - Τ：`\Tau`
   - Υ：`\Upsilon`
   - Φ：`\Phi`
   - Χ：`\Chi`
   - Ψ：`\Psi`
   - Ω：`\Omega`

使用这些命令可以在 LaTeX 中方便地插入希腊字母。

## 基本结构

LaTeX 是一种用于排版科技文档的强大工具，它使用 TeX 作为排版引擎。下面是 LaTeX 的一些基本语法：

### LaTeX 文档结构

一个简单的 LaTeX 文档由以下几部分组成：

```latex
\documentclass{article} % 文档类

\begin{document} % 文档内容开始

% 正文内容

\end{document} % 文档内容结束
```

### 基本命令

- LaTeX 命令以反斜杠 `\` 开头，通常具有以下形式：`\command[optional]{mandatory}`。
- 例如，`\documentclass{article}` 用于指定文档类为文章类型。
- LaTeX 使用大括号 `{}` 来组织命令的参数，方括号 `[]` 用于可选参数。

### 标题、作者、日期

```latex
\title{标题}
\author{作者}
\date{\today} % 使用当前日期，或者手动指定日期
```

在 `\begin{document}` 之前使用上述命令设置文档的标题、作者和日期。

### 生成文档标题

```latex
\maketitle
```

### 章节、段落

```latex
\section{章节标题}
\subsection{子章节标题}
\subsubsection{子子章节标题}

段落之间使用一个或多个空行分隔。
```

### 列表

```latex
\begin{itemize} % 无序列表
  \item 项目1
  \item 项目2
\end{itemize}

\begin{enumerate} % 有序列表
  \item 项目1
  \item 项目2
\end{enumerate}
```

### 文字格式

```latex
\textbf{加粗文本}
\emph{强调文本}
\underline{下划线文本}
```

### 插入图片

```latex
\usepackage{graphicx} % 导入图形包

\begin{figure}
  \centering
  \includegraphics[width=0.5\textwidth]{example-image} % 插入图片
  \caption{图片标题}
  \label{fig:example}
\end{figure}
```

### 插入表格

```latex
\begin{table}
  \centering
  \begin{tabular}{|c|c|} % 表格内容
    \hline
    列1 & 列2 \\
    \hline
    数据1 & 数据2 \\
    数据3 & 数据4 \\
    \hline
  \end{tabular}
  \caption{表格标题}
  \label{tab:example}
\end{table}
```

### 数学公式

```latex
\usepackage{amsmath} % 数学包

在文中插入数学公式，例如：$E=mc^2$ 或者

\begin{equation} % 单行公式
  F = ma
\end{equation}

\begin{align} % 多行公式
  E &= mc^2 \\
  F &= ma
\end{align}
```

### 注释

```latex
% 单行注释
```

### 插入代码

```latex
\documentclass{article}

% 加载宏包
\usepackage{listings}
\usepackage{xcolor}

% 设置代码样式
\lstset{
    language=C, % 代码语言
    basicstyle=\ttfamily, % 字体样式
    keywordstyle=\color{blue}, % 关键字颜色
    commentstyle=\color{green!50!black}, % 注释颜色
    numbers=left, % 行号显示位置
    numberstyle=\tiny\color{gray}, % 行号样式
    stepnumber=1, % 行号间隔
    numbersep=5pt, % 行号与代码间距
    frame=single, % 边框样式
    breaklines=true, % 自动换行
    breakatwhitespace=true, % 换行处是否允许分割
    tabsize=4, % 制表符宽度
    showspaces=false, % 是否显示空格
    showstringspaces=false % 是否显示字符串中的空格
}

\begin{document}

% 插入代码
\begin{lstlisting}
#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}
\end{lstlisting}

\end{document}
```



以上是 LaTeX 的一些基本语法，让你能够开始编写简单的文档。LaTeX 还有很多高级功能和定制选项，你可以根据需要查阅相关文档或书籍进一步学习。



