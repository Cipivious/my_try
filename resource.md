<a name="Tasks"> </a>

# Tasks

- [ ] ...
- [ ] [学习python-markdown](#python-markdown)
- [x] [学习nodejs](#运行环境)
- [x] 域名备案完成
- [ ] 银行卡认证
- [ ] [阅读typora主题的配置文件](#typora 自定义 css)
- [ ] [learn mini video](#mini video)
- [x] [emacs web-mode](https://web-mode.org/)配置
- [x] [修改emacs配置文件](#emacs修改配置文件)
- [ ] [学习正则表达式](#正则表达式)
- [x] [emacs写xhtml的插件的安装与使用](#emacs迈向xhtml)

<a name="Resource"> </a>

# Resource

## 本地资源

[电子书](file:///home/yang/ebooks)

## 网络资源

### web开发

[free-web-books](https://github.com/anzhihe/Free-Web-Books)

<a name="ChatGPT"> </a>

# ChatGPT

## [文心一言](https://yiyan.baidu.com/)

## [ChatGPT](https://chat.openai.com/)

## [Gemini](https://gemini.google.com/)

## Grok

grok 是 X 公司研发的一个模型，它有开源的版本

## [kimi](https://kimi.moonshot.cn/)

擅长长文本分析，可以达到二十万字

## 插件

### [推荐一款非常好用的 ChatGPT 插件 Superpower for ChatGPT](https://zhuanlan.zhihu.com/p/629361369)

<a name="Wolfram"> </a>

# Wolfram 

## [程序员入门](https://www.wolfram.com/language/fast-introduction-for-programmers/zh/iterators/)

<a name="Neural-Network"> </a>

# Neural-Network

## 学习笔记

1. ### 预备知识

- #### 数据操作

numpy pandas os

- #### 数据预处理

把训练数据化成方便读取的格式

- #### 线性代数

Y = W*X+b, 其中 W 和 X 都是矩阵，它们满足矩阵乘法原则，b 是列矩阵，他按照 torch 的广播机制和前者相加

- #### 自动微分

自动微分需要再定义变量（比如 x）的时候再后面添加，require_grad, 还需要其他的函数进行显示的 backward()以后才会被计算，这时候可以使用 x.grad 来进行调用

- #### 概率

pytorch 中有一个方法可以自动的批量进行随机模拟，产生具体的样本

2. ### 线性神经网络

- #### 线性回归

线性回归指的是是使用线性模型来对模型进行拟合

- #### 线性回归的从零开始实现

1. 数据迭代器（data_iter）用于获取一定 batch_size 的数据
2. 网络（net）用于具体的计算
3. 损失函数（loss）用于评估训练的准确度
4. 梯度下降函数（sgd）用于根据计算得到的梯度更新 w 已经 b 的值
5. epoch 表示训练的轮数

- #### 线性回归的简洁实现

![神经网络的基本框架](/home/yang/Pictures/machine_learning/基本框架.png)

- #### softmax 回归

主要区别于线性拟合的地方，在于使用的函数不相同，softmax 可以将结果映射成分类后的结果，而线性拟合的结果是连续的

- #### 图像分类数据集

这里主要介绍了图像分类数据集的预处理操作，他把 28 *28 的很多张图片转化成了 784*$(照片张数)的数据，然后写了一个迭代器用于获取每一次的训练数据

3. ### 多层感知器

- 多层感知机

它对多层感知机做了一个简单的介绍，它主要突出了上面的层的概念。

![layers](/home/yang/Pictures/machine_learning/layers.png)

- #### 多层感知器的简洁实现

它和之前线性回归的整体框架是类似的，主要区别只在于它中间的层级结构更多了一些，计算更复杂了一些

- #### 模型选择与欠拟合、过拟合

多项式维度低会欠拟合，而过高则会过拟合

- #### 权重衰减

- #### 向前传播

<img src="/home/yang/Pictures/machine_learning/forward.svg" alt="前向传播" style="zoom:150%;" />

- #### 训练神经网络

以上述简单网络为例：一方面，在前向传播期间计算正则项 [(4.7.5)](https://zh-v2.d2l.ai/chapter_multilayer-perceptrons/backprop.html#equation-eq-forward-s) 取决于模型参数和 的当前值。 它们是由优化算法根据最近迭代的反向传播给出的。 另一方面，反向传播期间参数 [(4.7.11)](https://zh-v2.d2l.ai/chapter_multilayer-perceptrons/backprop.html#equation-eq-backprop-j-h) 的梯度计算， 取决于由前向传播给出的隐藏变量

的当前值。

因此，在训练神经网络时，在初始化模型参数后， 我们交替使用前向传播和反向传播，利用反向传播给出的梯度来更新模型参数。 注意，反向传播重复利用前向传播中存储的中间值，以避免重复计算。 带来的影响之一是我们需要保留中间值，直到反向传播完成。 这也是训练比单纯的预测需要更多的内存（显存）的原因之一。 此外，这些中间值的大小与网络层的数量和批量的大小大致成正比。 因此，使用更大的批量来训练更深层次的网络更容易导致 *内存不足*（out of memory）错误。

- #### 数值稳定性和模型初始化

梯度消失 当 sigmoid 函数的输入很大或是很小时，它的梯度都会消失, 因此，更稳定的 ReLU 系列函数已经成为从业者的默认选择（虽然在神经科学的角度看起来不太合理）

梯度爆炸 矩阵乘积发生爆炸。 当这种情况是由于深度网络的初始化所导致时，我们没有机会让梯度下降优化器收敛

- #### 参数初始化

- #####  默认初始化 使用正态分布来初始化权重值

- ##### Xavier 初始化 

- #### 分布偏移

训练集和测试集并不来自同一个分布。这就是所谓的分布偏移

在相应的假设条件下，可以在测试时检测并纠正协变量偏移和标签偏移。在测试时，不考虑这种偏移可能会成为问题

## mathematica 神经网络

mathematica 神经网络综述

https://reference.wolfram.com/language/tutorial/NeuralNetworksOverview.html

mathematica 神经网络简述

https://reference.wolfram.com/language/tutorial/NeuralNetworksIntroduction.html.zh?source = footer

## python 神经网络

李沐电子版教程

https://zh-v2.d2l.ai/

本地文件夹配套李沐教程

[文件夹](file:///home/yang/d2l-zh/pytorch/)

## pytorch 官网

官方文档

https://pytorch.org/docs/stable/index.html

官方网站

https://pytorch.org

## MXNet

[官方网站](https://www.nvidia.cn/glossary/data-science/mxnet/)

mxnet 是英伟达推出的一项机器语言学习框架，可以直接适用于英伟达的芯片，而且在 GPU 组训练上更加具有优势

## 相关比赛

### [kaggle](https://www.kaggle.com/)

这是一个当今流行举办机器学习比赛的平台， 每场比赛都以至少一个数据集为中心

#### 选手

[SZU Bayes](https://www.kaggle.com/bayes2003)

它来源于 [甲骨文公司](https://docs.oracle.com/cd/E28280_01/bi.1111/b32122/orbr_concepts1004.htm#RSBDR152)，它是房价预测比赛的第一名

## 专家

微信名称 望风

<a name="wechat-mini-program"> </a>

# wechat-mini-program

## [微信公众平台](https://mp.weixin.qq.com/)

## 问答经验

1. **上传文件：** 讨论了如何通过前端页面使用 Fetch API 将文件上传到服务器，并提供了相应的 Flask 后端代码用于接收和处理上传的文件。
2. **处理 Markdown 文件：** 讨论了如何将 Markdown 文件转换为 HTML，并提供了相应的 Python Flask 后端代码以及 JavaScript 前端代码用于实现此功能。
3. **显示提示消息：** 讨论了如何在页面上显示提示消息，包括居中显示在页面上方，并提供了相应的 CSS 和 JavaScript 代码实现此功能。
4. **保存和编辑 Markdown 文件：** 讨论了如何在前端页面上保存和编辑 Markdown 文件，并提供了相应的 JavaScript 代码实现此功能。
5. **使用链接按钮：** 讨论了如何在页面上创建一个按钮，点击该按钮会跳转到指定的链接，提供了相应的 HTML 和 CSS 代码实现此功能。

## 网站编辑实时预览

类似于 Typora 这样的所见即所得（WYSIWYG）编辑工具，在 HTML 编辑方面并不是特别常见。然而，有一些编辑器提供了类似的功能，允许你在编辑 HTML 时实时预览效果。以下是一些可以考虑的工具：

1. **Adobe Dreamweaver：** Dreamweaver 是 Adobe 公司开发的一个功能强大的网页设计和编程软件，提供所见即所得的编辑功能，并且支持 HTML、CSS、JavaScript 等多种语言的编辑和预览。
2. **Microsoft Expression Web：** 这是一个微软开发的网络开发工具，提供所见即所得的编辑功能，适用于创建和编辑 HTML、CSS 和 JavaScript。
3. **BlueGriffon：** 这是一个开源的 WYSIWYG HTML 和 EPUB 编辑器，类似于 Dreamweaver，提供了可视化编辑和实时预览的功能。
4. **CKEditor：** CKEditor 是一个基于 Web 的富文本编辑器，可以集成到你的网站或应用程序中，提供了类似于 Typora 的实时编辑和预览功能。
5. **TinyMCE：** TinyMCE 是另一个流行的富文本编辑器，可以用于在网站或应用程序中创建和编辑 HTML 内容，并提供所见即所得的编辑功能。

对于 Ubuntu 或其他 Linux 系统，也有一些可用的所见即所得的 HTML 编辑工具。以下是一些常见的选择：

1. **Bluefish：** 这是一个功能强大的 HTML 编辑器，提供了实时预览功能，并支持多种编程语言的编辑。它可以在 Ubuntu 中通过软件包管理器安装。
2. **KompoZer：** KompoZer 是一个免费的 WYSIWYG HTML 编辑器，具有类似于 Dreamweaver 的界面和功能，可用于创建和编辑 HTML 页面。
3. **Quanta Plus：** Quanta Plus 是一个基于 KDE 的 HTML 编辑器，提供了所见即所得的编辑功能，并集成了代码编辑器、文件管理器等工具。
4. **BlueGriffon：** 此工具之前已经提到过，它也提供了 Linux 版本，可以在 Ubuntu 上使用。它是一个跨平台的 HTML 和 EPUB 编辑器，具有类似于 Dreamweaver 的界面和功能。
5. **Atom / Visual Studio Code / Sublime Text：** 虽然这些编辑器不是专门的所见即所得的 HTML 编辑器，但它们提供了丰富的插件和功能，可以安装插件来实现所见即所得的编辑和预览功能。

<a name="emacs"> </a>

# emacs

## 操作命令

执行init.el eval-buffer

执行单行代码 C-x C-e

## 用emacs读源代码

### [技巧](https://stardiviner.github.io/Blog/How-to-Read-Code-in-Emacs.html#org8a5067d)

### 比较差异

在 Emacs 中，有一些工具可以帮助您比较文件之间的差异，并了解文档相对于之前的版本所做的修改。以下是一些常用的工具：

1. **Ediff**： `Ediff` 是 Emacs 的内置工具，用于比较文件之间的差异并进行合并。您可以使用 `M-x ediff` 命令来启动 Ediff，并选择要比较的文件。Ediff 将会以交互方式显示两个文件之间的差异，并允许您进行修改和合并。
2. **Diff Mode**： `Diff Mode` 是 Emacs 的一个内置模式，用于显示文件之间的差异。您可以使用 `M-x diff-mode` 命令来将当前缓冲区切换到 Diff Mode，并使用 `diff` 命令生成的补丁文件来查看文件之间的差异。
3. **Vc-diff**： 如果您正在使用版本控制系统（如 Git），Emacs 还提供了 `Vc-diff` 工具，用于比较版本控制中的文件的差异。您可以使用 `M-x vc-diff` 命令来查看当前文件在版本控制系统中的修改情况，并以交互方式浏览差异。

这些工具都是 Emacs 自带的，可以帮助您比较文件之间的差异，并了解文档相对于之前的版本所做的修改。您可以根据自己的需求选择适合的工具来进行文件比较和修改。

## use emacs to write js

### 安装自动补全插件

[tern](https://github.com/ternjs/tern/tree/master?tab=readme-ov-file)

[company-tern这是一个坑人的玩意，非常麻烦](https://github.com/kevinushey/company-tern?tab=readme-ov-file)

[tern使用也非常的麻烦](https://github.com/webpack/webpack/issues/15127)

在emacs中想配置直接执行js非常麻烦，暂时放弃

### [安装js2-mode](https://github.com/mooz/js2-mode)

### [安装indium](https://indium.readthedocs.io/en/latest/installation.html)

#### [配置indium](https://emacs-china.org/t/indium-emacs-javascript/7051)

#### [下载json-process-client](https://github.com/emacsmirror/json-process-client)

要注意顺序

#### [下载js2-refactor](https://github.com/js-emacs/js2-refactor.el)

#### [下载s包](https://github.com/magnars/s.el)

#### [下载multiple-cursors](https://github.com/magnars/multiple-cursors.el)

### [安装Chrome浏览器](https://support.google.com/chrome/a/answer/9025903?hl=en&ref_topic=9025817&sjid=17686342759721064849-AP)

我反复尝试了好久都没有成功，主要在于我对这个语言掌握的太少，我准备先用替代的方法，之后有机会再安装。

## use emacs to write html

### [常用软件写网页html,新手用什么软件写html网页比较靠谱](https://blog.csdn.net/weixin_31056947/article/details/117853448)

### [用emacs写html文件](https://blog.csdn.net/paul08colin/article/details/6443266)

 p { margin-bottom: 0.21cm; } 

C-c C-f :  光标移动到当前所在位置的下一个HTML 标签。

 C-c C-b :  光标移到到当前所在位置的上一个HTML 标签。 

C-c \<left>/\<right> :  跳到该标签的开始/ 结束。

 C-c DEL :  删除标签。 C-c 1~6 :  插入标题h1~h6 。

 C-c Enter :  插入段落标记\<p> 。 

C-c /  ：闭合b 标签。比如可以结合上一条使用，就会自动插入\</p> 。

 C-c C-c h :  插入超级链接标记。

 C-c C-c n :  插入anchor （锚标），便于在文档其他位置跳转到该位置。

需要在Mini-buffer 中输入锚标名称。

 C-c C-c u :  插入无序列表标记\<ul>\<li>\</ul> 。

 C-c C-c o :  插入有序列表标记\<ol>\<li>\</ol> 。

 C-c C-c l :  插入标记\<li> 。

 C-c C-c - :  插入水平线\<hr> 。 

C-c C-c i :  插入图像引用标记 \<img> 。

 C-c C-j :  插入换行符\<br>

 有时需要在html文本中显示html标记，比如\<p>，不能直接输入。可以这样： C-c C-n < ，然后输入 p ，然后再 C-c C-n >;。其实 C-c C-n 后输入的字符都不会被html解析而直接输出了。 

c-c c-t 跳过之后的标签 [C-M-j](https://emacs.stackexchange.com/questions/35378/html-mode-insert-tag-without-attributes)

### [使用emacs写html](http://blog.chinaunix.net/uid-7591142-id-112460.html)

### emacs迈向xhtml

#### [tidy](http://www.hollenback.net/index.php?EmacsTidy)

#### [nxml-mode](https://www.emacswiki.org/emacs/NxmlModeForXHTML#h5o-1)

#### emacs修改配置文件

emacs修改文件过程

1. 使用C-h k 或者C-h m找到函数的定义
2. 更具一个已知的函数反复搜索，找到map定义
3. 更改原来的定义，以及hook的内容
4. 修改完以后，需要用M-x byte-compile-file来重新编译文件（这一步主要针对内置的文件，因为内置的文件经过编译以提高运行速率）

![image-20240425092053868](/home/yang/.config/Typora/typora-user-images/image-20240425092053868.png)

<a name="html"> </a>

# html

## [tools](#use emacs to write html)

## 学习笔记

### 学习教材

#### [headfirst html](file:///home/yang/ebooks/web/Head%20First%20HTML%E4%B8%8ECSS%E4%B8%AD%E6%96%87%E7%89%88.pdf)

### 学习笔记

#### 块元素与内联元素

在HTML中，元素可以分为块级元素（block-level elements）和内联元素（inline elements），它们在文档中的布局和显示行为有所不同。

**块级元素**：

1. 块级元素会在页面上以独立的块状区域显示，即元素会占据一整行或者一整个父容器的宽度。
2. 块级元素可以包含其他块级元素或者内联元素。
3. 常见的块级元素包括 `<div>`、`<p>`、`<h1>` - `<h6>`、`<ul>`、`<ol>`、`<li>`、`<blockquote>` 等。

**内联元素**：

1. 内联元素通常在行内显示，即它们不会独占一行，而是在同一行内随文本流动。
2. 内联元素只能容纳文本或者其他内联元素，不能包含块级元素。
3. 常见的内联元素包括 `<span>`、`<a>`、`<strong>`、`<em>`、`<img>`、`<br>`、`<input>` 等。

#### css样式大全

[css样式](file:///home/yang/ebooks/web/css.pdf)

#### 使用浏览器的开发者工具

浏览器的开发者工具具有非常强大的功能

- 增加或者取消css样式
- 查看样式的具体数值
- 获得具体的样式内容

<img src="/home/yang/typora/image/截图 2024-04-23 19-35-05.png" alt="开发者工具" style="zoom: 33%;" />

#### [在线颜色表](https://tool.oschina.net/commons?type=3)

<a name="javascript"> </a>

# javascript

## 运行环境

### [nodejs官方文档](https://nodejs.org/docs/latest/api/documentation.html)

|                                               | python       | javascript   |
| --------------------------------------------- | ------------ | ------------ |
| 脚本                                          | py脚本       | js脚本       |
| 运行环境                                      | python解释器 | nodejs解释器 |
| 包管理器（使用npm可以安装nodejs运行时的依赖） | pip          | npm          |
| 版本管理器（使用nvm可以安装不同版本的npm）    | conda        | nvm          |



### [Chrome浏览器](#安装Chrome浏览器)

### 重新安装npm以及nodejs

#### 卸载n

rm -rf ~/.nvm

exec "$SHELL"

dpkg -S /usr/bin/npm 查看npm是通过什么方式安装的

apt show npm 这将显示有关 `npm` 软件包的详细信息，包括版本、描述等。

sudo apt remove nodejs 卸载nodejs

#### 重新安装

[从该界面下载nvm](https://github.com/nvm-sh/nvm)

添加配置文件

```bash
(d2l2) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:~$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- -  0     0    0     0    0     0      0      0 --:--:-- --:--:-- -100 16555  100 16555    0     0  22238      0 --:--:-- --:--:-- --:--:-- 22221
=> Downloading nvm from git to '/home/yang/.nvm'
=> 正克隆到 '/home/yang/.nvm'...
remote: Enumerating objects: 365, done.
remote: Counting objects: 100% (365/365), done.
remote: Compressing objects: 100% (313/313), done.
remote: Total 365 (delta 43), reused 165 (delta 26), pack-reused 0
接收对象中: 100% (365/365), 365.08 KiB | 1.03 MiB/s, 完成.
处理 delta 中: 100% (43/43), 完成.
* （头指针在 FETCH_HEAD 分离）
  master
=> Compressing and cleaning up git repository

=> nvm source string already in /home/yang/.bashrc
=> bash_completion source string already in /home/yang/.bashrc
=> Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
(d2l2) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:~$ ema .bashrc
(d2l2) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:~$ source .bashrc
(d2l2) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:~$ nvm --version
0.39.7
(d2l2) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:~$ nvm install node
Downloading and installing node v22.0.0...
Downloading https://nodejs.org/dist/v22.0.0/node-v22.0.0-linux-x64.tar.xz...
########################################################## 100.0%
Computing checksum with sha256sum
Checksums matched!
Now using node v22.0.0 (npm v10.5.1)
Creating default alias: default -> node (-> v22.0.0)

```

<a name="python"> </a>

# python

## python 程序包

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

### 12306 爬虫

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

<a name="broswer"> </a>

# broswer

## 油猴脚本

### [无缝翻页](https://greasyfork.org/zh-CN/scripts/419215-%E8%87%AA%E5%8A%A8%E6%97%A0%E7%BC%9D%E7%BF%BB%E9%A1%B5)

### [知乎增强](https://greasyfork.org/zh-CN/scripts/419081-%E7%9F%A5%E4%B9%8E%E5%A2%9E%E5%BC%BA)

### [CSDN 增强](https://greasyfork.org/zh-CN/scripts/378351-csdngreener-csdn%E5%B9%BF%E5%91%8A%E5%AE%8C%E5%85%A8%E8%BF%87%E6%BB%A4-%E5%85%8D%E7%99%BB%E5%BD%95-%E4%B8%AA%E6%80%A7%E5%8C%96%E6%8E%92%E7%89%88-%E6%9C%80%E5%BC%BA%E8%80%81%E7%89%8C%E8%84%9A%E6%9C%AC-%E6%8C%81%E7%BB%AD%E6%9B%B4%E6%96%B0)

<a name="linux"> </a>

# linux 

## 执行定时任务

### 查看定时任务(当前用户)

crontab -l	

### 编辑定时任务

crontab -e

m h m d y /home/yang/typora/run.sh

### 检查定时任务的执行效果

/var/log/syslog 中存放着系统执行文件的记录，可以从里面查看执行情况

使用 `grep CRON /var/log/syslog` 可以筛选出定时文件的执行情况

## systemctl

### 开机

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

### 关机

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
sh
Copy code
sudo systemctl enable your-shutdown-hook.service
```

这样，当系统关闭时，您的脚本 `/path/to/your/shutdown_script.sh` 将会自动执行。

## 使用git

一旦您的 Markdown 文件准备好了，您可以使用 Git 工具将文件上传到 GitHub。以下是一个基本的上传流程：

- 首先，确保您已经在本地使用 Git 初始化了一个仓库，并将其与 GitHub 上的远程仓库关联。
- 将您的 Markdown 文件添加到 Git 中：`git add your_file.md`
- 提交更改：`git commit -m "Add your_file.md"`
- 推送到 GitHub：`git push origin master`

在上面的命令中，`your_file.md` 是您要上传的 Markdown 文件的文件名，`origin` 是您与 GitHub 关联的远程仓库的名称，`master` 是您要推送到的分支名称。

可以使用git commit -m "Add new feature - $(date +"%Y-%m-%d")"按日期更新

### [run.sh](file:///home/yang/typora/my_try/run.sh)

这是一个自动上传的脚本

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



## ssh使用方法

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

### 查看CPU设置

lscpu

### 查看显卡设置

lspci

### 查看内存信息

cat /proc/meminfo

### 查看硬盘信息

lsblk

### 查看全部的信息

lshw

### 结果

[参见这里](#电脑硬件)

## [临时当做计算器](https://blog.csdn.net/focus_lyh/article/details/112371286)

expr 1 + 2（注意空格）

expr 28 \* 28（运算符需要转义）

## [修改默认应用](https://blog.csdn.net/hustrains/article/details/8652098)

如果你想指定Okular和Emacs作为默认的应用程序来打开特定类型的文件，你需要做以下步骤：

1. **确定应用程序的.desktop文件名：** 首先，你需要确定Okular和Emacs的.desktop文件名。通常，Okular的.desktop文件名可能是`okular.desktop`，Emacs的.desktop文件名可能是`emacs.desktop`。你可以在`/usr/share/applications`目录中查找这些文件，或者使用`locate`命令搜索它们。

2. **编辑文件关联：** 一旦确定了.desktop文件名，你可以编辑文件关联列表以将其与特定类型的文件关联起来。你可以通过在终端中使用文本编辑器（如Nano或Vim）打开`~/.local/share/applications/mimeapps.list`文件，然后添加以下行：

```
application/oxps=okular.desktop
application/pdf=okular.desktop
application/postscript=okular.desktop
application/rtf=emacs.desktop
```

这样就会将Okular关联到`.oxps`、`.pdf`和`.ps`文件，将Emacs关联到`.rtf`文件。

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

<a name="ideas"> </a>

# ideas

## 网站验证

近期出现了一种新的网站验证方式，它需要经过 5 次图像验证才可以通过，我曾在 X 的登录以及 ChatGPT 的登录界面上看过，它的验证方式特别复杂，要好长时间才可以通过，特别麻烦。如果之后我做网站出于安全性考虑也可以采用这种验证方式。

之前网站验证的方式还有滑动滑块，识别文字等等，我对于这种验证一类的特别反感

## 大陆防火墙

### [Twitter 加载慢](https://www.aftzy.com/n/24084.html)

## Guido面试google

[Guido van Rossum 去 Google 应聘，只写了三个词「I wrote Python」的简历是真的吗？](https://www.zhihu.com/question/20661545)

## 中文还是英文

之前我耗费了很多时间，在尝试阅读英文的文档上，但是效果不好，我觉得最好的方法是用自己熟悉的语言来学习，在没有掌握英语的情况下，就踏踏实实的看中文的电子书，这样效果会比查词典看中文书好的多，而且查词典看中文书并不会显著提高阅读英语的水平，它只能给你一种你很厉害的幻想。

## 咸鱼

### [咸鱼网站](https://www.goofish.com/)

咸鱼是阿里巴巴出品的一个二手买卖平台，里面有很多二手和闲置的东西，有的价格很低，但是也并非全都如此。当咸鱼变得逐渐普及之后，有一些咸鱼开店的程序也应运而生，比如

```python
【闲鱼】https://m.tb.cn/h.g0mERg8?tk=nnQ5WIgrI8s CZ3458 「快来捡漏【【自动发货】闲鱼虚拟自动发货教程，闲鱼官方网站的一种方法，很】」
点击链接直接打开
```

以上是一个例子。

<a name="typora"> </a>


# typora

## [常用模版](https://blog.csdn.net/weixin_42306823/article/details/126629333)

包含会议模版，头脑风暴，甘特图等

## [typora 关闭拼写检查](https://blog.csdn.net/weixin_44924882/article/details/107826667)

## typora 与 html

typora 内置支持一些 html 的内容，但不支持 css 以及 js，导致一些显示的效果不好，如果能直接使用 html 做笔记会更爽

## [typora 这个公式块怎么删除，死活删不掉？](https://www.zhihu.com/question/457782965/answer/1874490937)

跳到代码模式，然后删掉对应的代码, 公式块 $$.

## [typora 更改代码块的语言](https://www.zhihu.com/question/630401625/answer/3292189749)

跳到代码模式，在、、、后面写语言, 最好的方法是使用按键直接输入```python

## [typora 内部实现衔接](https://support.typora.io/Links/#internal-links)

```
## This is a title
A [link](#this-is-a-title) to jump towards target heading
```

```
<a name="anchor"></a> Anchor
<a href="#anchor">Link to Anchor</a>
```

## [typora 降低或提高标题等级](https://www.zhihu.com/question/428959880/answer/1892820567)

ctrl + / 进入源代码模式

ctrl + F 查找替换

将 "# "（记得带空格）替换成 " "

[文本替换的方法](https://jingyan.baidu.com/article/ab69b27083ee026da7189fa1.html)

## [拆分 Markdown 文件](https://github.com/ayasa520/markown-splitter)

没什么用的小玩意儿，平时记笔记都是在一个文件里记的，所以借助这个脚本拆开来。功能如下：

- 将 md 文件按照一级标题拆分为多个文件
- 提升或者降低所有的标题等级

## [typora 自定义 css](https://juejin.cn/s/typora%20%E8%87%AA%E5%AE%9A%E4%B9%89css)

1. 打开 Typora 并新建一个 Markdown 文件。
2. 点击 Typora 菜单栏中的 "偏好设置"。
3. 在偏好设置窗口中，点击 "外观" 标签。
4. 在 "CSS" 下拉菜单中，选择 "打开自定义 CSS"。
5. 创建或编辑一个 CSS 文件来应用您的自定义样式。
6. 将您的 CSS 文件保存到 Typora 预设的文件夹中。这个文件夹的路径通常是：`%APPDATA%\Typora\themes` (Windows) 或 `~/Library/Application Support/abnerworks.Typora/themes/` (macOS)。
7. 关闭并重新启动 Typora 应用程序，以应用您的自定义 CSS 文件。

## [typora 主题自定义官方文档](https://support.typoraio.cn/About-Themes/)

## typora临时插入一行代码

`grep CRON /var/log/syslog` 



<a name="Github Project"> </a>

# Github Project

## 娱乐项目

### [在 idea 里面玩小游戏](https://github.com/anlingyi/xechat-idea?tab=readme-ov-file)



<a name="tools-box"> </a>

# tools-box

## [图片转文字](https://ocr.wdku.net/)

## [在线颜色表](#在线颜色表)

## 正则表达式

### [regex101](https://regex101.com/)

### [oschina](https://tool.oschina.net/regex#)

## 文件格式转化工具

### pandoc

#### [官方网站](https://support.typora.io/Install-and-Use-Pandoc/)

#### [教程](https://zhuanlan.zhihu.com/p/542683108)

sudo apt install pandoc

 pandoc --standalone --self-contained --metadata title="Your Document Title" --css ../.config/Typora/themes/github.css resource.md --output resource2.html 

## 浏览器测试工具

[BrowserBench](https://browserbench.org/Speedometer3.0/#running)

谷歌浏览器

![image-20240428155809123](/home/yang/.config/Typora/typora-user-images/image-20240428155809123.png)

edge浏览器

![image-20240428160532363](/home/yang/.config/Typora/typora-user-images/image-20240428160532363.png)

firefox浏览器

![image-20240428162328457](/home/yang/.config/Typora/typora-user-images/image-20240428162328457.png)



<a name="computer-knowledge"> </a>

# computer-knowledge

## 电脑硬件

### 输入设备

1. **`\*-input:0`**：描述了一个输入设备。
   - **product**: 设备的产品名称，此处是 "Lid Switch"（盖子开关）。
   - **physical id**: 设备的物理 ID，可能是设备在系统中的唯一标识。
   - **logical name**: 设备的逻辑名称，这里有两个：`input0` 和 `/dev/input/event0`，分别表示设备的逻辑名称和设备在系统中的事件文件路径。
   - **capabilities**: 设备的功能或能力，此处是 "platform"（平台）。
   
2. **`\*-input:1`**：另一个输入设备的描述，与第一个类似。

   - **product**: 设备的产品名称，此处是 "Power Button"（电源按钮）。
   - **physical id**: 设备的物理 ID。
   - **logical name**: 设备的逻辑名称，同样有两个：`input1` 和 `/dev/input/event1`。
   - **capabilities**: 设备的功能或能力，也是 "platform"。

3. **`\*-input:2`**：描述了第三个输入设备，这是一个触摸板。

   - **product**: 设备的产品名称，此处是 "ELAN0729:00 04F3:315D Touchpad"。
   - **physical id**: 设备的物理 ID。
   - **logical name**: 设备的逻辑名称，包括 `input10`、`/dev/input/event5` 和 `/dev/input/mouse1`。
   - **capabilities**: 设备的功能或能力，这里是 "i2c"。

4. **`\*-input:3`**：描述了另一个输入设备，HP 的 WMI 热键。

   - **product**: 设备的产品名称，此处是 "HP WMI hotkeys"。
   - **physical id**: 设备的物理 ID。
   - **logical name**: 设备的逻辑名称，包括 `input11` 和 `/dev/input/event8`。
   - **capabilities**: 设备的功能或能力，也是 "platform"。

5. **`\*-input:4`**：描述了一个视频总线输入设备。

   - **product**: 设备的产品名称，此处是 "Video Bus"。
   - **physical id**: 设备的物理 ID。
   - **logical name**: 设备的逻辑名称，包括 `input12` 和 `/dev/input/event7`。
   - **capabilities**: 设备的功能或能力，也是 "platform"。

6. **`\*-input:5`**：描述了另一个输入设备，一个音频输入设备。

      - **product**: 设备的产品名称，此处是 "sof-hda-dsp Mic"。
      - **physical id**: 设备的物理 ID。
      - **logical name**: 设备的逻辑名称，包括 `input13` 和 `/dev/input/event9`。
      - **capabilities**: 设备的功能或能力，未指定。


7. **`\*-input:6`**：描述了一个耳机输入设备。

   - **product**: 设备的产品名称，此处是 "sof-hda-dsp Headphone"。
   - **physical id**: 设备的物理 ID，这里是 8。
   - **logical name**: 设备的逻辑名称，包括 `input14` 和 `/dev/input/event10`。

8. **`\*-input:7`**：描述了一个 HDMI/DisplayPort 输入设备，对应着 PCM 通道 3。

   - **product**: 设备的产品名称，此处是 "sof-hda-dsp HDMI/DP,pcm=3"。
   - **physical id**: 设备的物理 ID，这里是 9。
   - **logical name**: 设备的逻辑名称，包括 `input15` 和 `/dev/input/event11`。

9. **`\*-input:8`**：描述了另一个 HDMI/DisplayPort 输入设备，对应着 PCM 通道 4。

   - **product**: 设备的产品名称，此处是 "sof-hda-dsp HDMI/DP,pcm=4"。
   - **physical id**: 设备的物理 ID，这里是 a。
   - **logical name**: 设备的逻辑名称，包括 `input16` 和 `/dev/input/event12`。

10. **`\*-input:9`**：描述了另一个 HDMI/DisplayPort 输入设备，对应着 PCM 通道 5。

    - **product**: 设备的产品名称，此处是 "sof-hda-dsp HDMI/DP,pcm=5"。
    - **physical id**: 设备的物理 ID，这里是 b。
    - **logical name**: 设备的逻辑名称，包括 `input17` 和 `/dev/input/event13`。

11. **`\*-input:10`**：描述了另一个电源按钮输入设备。

    - **product**: 设备的产品名称，此处是 "Power Button"（电源按钮）。
    - **physical id**: 设备的物理 ID，这里是 c。
    - **logical name**: 设备的逻辑名称，包括 `input2` 和 `/dev/input/event2`。
    - **capabilities**: 设备的功能或能力，这里是 "platform"（平台）。

12. **`\*-input:11`**：描述了一个键盘输入设备。

    - **product**: 设备的产品名称，此处是 "AT Translated Set 2 keyboard"。
    - **physical id**: 设备的物理 ID，这里是 d。
    - **logical name**: 设备的逻辑名称，包括 `input3`、`/dev/input/event3`、`input3::capslock`、`input3::numlock` 和 `input3::scrolllock`。
    - **capabilities**: 设备的功能或能力，这里是 "i8042"，指示这是一个通过标准的8042键盘控制器与系统连接的键盘。

13. **`\*-input:12`**：描述了一个无线热键输入设备。

    - **product**: 设备的产品名称，此处是 "Wireless hotkeys"。
    - **physical id**: 设备的物理 ID，这里是 e。
    - **logical name**: 设备的逻辑名称，包括 `input7` 和 `/dev/input/event6`。
    - **capabilities**: 设备的功能或能力，这里是 "platform"。

14. **`\*-input:13`**：描述了一个鼠标输入设备。

    - **product**: 设备的产品名称，此处是 "ELAN0729:00 04F3:315D Mouse"。
    - **physical id**: 设备的物理 ID，这里是 f。
    - **logical name**: 设备的逻辑名称，包括 `input8`、`/dev/input/event4` 和 `/dev/input/mouse0`。


### 内存

*-memory
          description: System memory
          physical id: 0
          size: 16GiB

### cpu

*-cpu
          product: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
          vendor: Intel Corp.
          physical id: 1
          bus info: cpu@0
          version: 6.140.1
          size: 3878MHz
          capacity: 4200MHz
          width: 64 bits
          capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp x86-64 constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l2 invpcid_single cdp_l2 ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves split_lock_detect dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid movdiri movdir64b fsrm avx512_vp2intersect md_clear ibt flush_l1d arch_capabilities cpufreq
          configuration: microcode=180

### 显卡

#### VGA兼容控制器

这段信息描述了一个 VGA 兼容控制器（VGA compatible controller），下面是对每个字段的解释：

- **description: VGA compatible controller：** 设备的描述，表示这是一个 VGA 兼容的图形控制器。
- **product: TigerLake-LP GT2 [Iris Xe Graphics]：** 设备的产品名称，指明这是 TigerLake-LP GT2 显卡，采用 Iris Xe 图形架构。
- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。
- **physical id: 2：** 设备的物理标识符，用于唯一标识系统中的硬件设备。
- **bus info: pci@0000:00:02.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:02.0`。
- **logical name: /dev/fb0：** 设备的逻辑名称，表示这个设备可以在 `/dev/fb0` 文件中找到。
- **version: 01：** 设备的版本信息，表示这个设备的版本号为 01。
- **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。
- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。
- **capabilities: vga_controller bus_master cap_list rom fb：** 设备的功能列表，包括 VGA 控制器、总线主控、容量列表、只读存储器（ROM）和帧缓冲（Framebuffer）等功能。
- **configuration: depth=32 driver=i915 latency=0 resolution=1920,1080：** 设备的配置信息，包括色深、驱动程序、延迟和分辨率等。
- **resources: irq:167 memory:54000000-54ffffff memory:40000000-4fffffff ioport:3000(size=64) memory:c0000-dffff memory:56000000-5cffffff：** 设备的资源信息，包括中断请求（IRQ）、内存地址范围和 I/O 端口范围等。

##### VGA概述

VGA 是视频图形阵列（Video Graphics Array）的缩写，是一种用于显示图形的计算机显示标准。VGA 最初由 IBM 公司于 1987 年推出，是后来的显示标准的基础。

VGA 主要用于连接计算机和显示器，用于在显示器上显示计算机的图形和图像。它通过传输模拟视频信号来实现显示，通常使用 D-sub 连接器（也称为 VGA 连接器）连接计算机的显卡和显示器。

VGA 标准定义了一组视频信号的参数，包括分辨率、刷新率、色深等。它最初支持最高分辨率为 640x480 像素，并随后引入了更高分辨率和色彩深度的变体。

虽然 VGA 已经被更先进的显示接口（如 HDMI、DisplayPort）所取代，但它仍然被广泛使用在许多老式的计算机和显示设备中，以及一些特定的应用场景中。

### 存储

这段文本描述了一个 NVMe 设备，其产品型号为英特尔 SSDPEKNW512G8H，具有版本号 HPS1 和序列号 BTNH047218GE512A。让我们逐段解释：

1. **`*-nvme0`**：这是 NVMe 设备的整体描述，说明这是一个 NVMe 设备，并给出了一些关于该设备的详细信息。
   - **description**: 描述了设备类型，即 NVMe 设备。
   - **product**: 设备的产品型号，此处是英特尔 SSDPEKNW512G8H。
   - **physical id**: 物理 ID，可能是设备在系统中的唯一标识。
   - **logical name**: 逻辑名称，这是设备的逻辑路径或标识，通常用于在系统中引用设备。
   - **version**: 设备的版本信息，此处为 HPS1。
   - **serial**: 设备的序列号，此处是 BTNH047218GE512A。
   - **configuration**: 设备的配置信息，例如此处给出了 NQN（NVMe Qualified Name）和状态信息。

2. **`*-namespace:0`**：这是设备的一个命名空间（Namespace）的描述，命名空间是 NVMe 设备中用于提供存储的逻辑单位。
   - **description**: 命名空间的描述，此处是 NVMe 磁盘。
   - **physical id**: 物理 ID，可能指示了此命名空间在设备中的位置。
   - **logical name**: 逻辑名称，用于在系统中引用命名空间的名称。

3. **`*-namespace:1`**：另一个命名空间的描述，包含了与第一个命名空间类似的信息，但此处还提供了逻辑名称 `/dev/ng0n1`。

4. **`*-namespace:2`**：第三个命名空间的描述。
   - **description**: 命名空间的描述，此处也是 NVMe 磁盘。
   - **physical id**: 物理 ID，可能指示了此命名空间在设备中的位置。
   - **bus info**: 总线信息，可能是指示了此命名空间连接的总线信息。
   - **logical name**: 逻辑名称，用于在系统中引用命名空间的名称。
   - **configuration**: 配置信息，例如此处给出了命名空间的全局唯一标识符（WWID）。

总体来说，这段文本描述了一个英特尔制造的 NVMe SSD 设备，具有三个命名空间，每个命名空间代表了不同的逻辑存储单元，提供了详细的硬件信息和配置。

### 主板

这段信息描述了一个主机桥（Host Bridge）的详细信息，下面是对每个字段的解释：

- **description: Host bridge：** 设备的描述，表明这是一个主机桥设备。
- **product: 11th Gen Core Processor Host Bridge/DRAM Registers：** 设备的产品名称，指明这是第 11 代 Intel Core 处理器的主机桥和 DRAM 寄存器。
- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。
- **physical id: 100：** 设备的物理标识符，用于唯一标识系统中的硬件设备。
- **bus info: pci@0000:00:00.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:00.0`。
- **version: 01：** 设备的版本信息，表示这个设备的版本号为 01。
- **width: 32 bits：** 设备的数据传输宽度，表示这个设备支持 32 位数据传输。
- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。

这些信息描述了主机桥设备的基本特征，包括其产品、制造商、物理标识符、总线信息、版本、数据传输宽度和时钟频率等。

#### 信号处理控制器

这段信息描述了一个信号处理控制器（Signal processing controller），下面是对每个字段的解释：

- **description: Signal processing controller：** 设备的描述，表示这是一个信号处理控制器。
- **product: TigerLake-LP Dynamic Tuning Processor Participant：** 设备的产品名称，指明这是 TigerLake-LP 动态调整处理器参与者。
- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。
- **physical id: 4：** 设备的物理标识符，用于唯一标识系统中的硬件设备。
- **bus info: pci@0000:00:04.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:04.0`。
- **version: 01：** 设备的版本信息，表示这个设备的版本号为 01。
- **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。
- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。
- **capabilities: bus_master cap_list：** 设备的功能列表，包括总线主控和容量列表。
- **configuration: driver=proc_thermal latency=0：** 设备的配置信息，包括驱动程序和延迟。
- **resources: irq:16 memory:55300000-5531ffff：** 设备的资源信息，包括中断请求（IRQ）和内存地址范围。

这些信息描述了信号处理控制器设备的基本特征，包括其产品、制造商、物理标识符、总线信息、版本、功能列表、配置和资源等。

#### 设备外设

这段信息描述了一个未声明的系统外设（System peripheral），下面是对每个字段的解释：

- **description: System peripheral：** 设备的描述，表示这是一个系统外设。
- **product: GNA Scoring Accelerator module：** 设备的产品名称，指明这是 GNA（Gaussian and Neural Accelerator）评分加速器模块。
- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。
- **physical id: 8：** 设备的物理标识符，用于唯一标识系统中的硬件设备。
- **bus info: pci@0000:00:08.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:08.0`。
- **version: 01：** 设备的版本信息，表示这个设备的版本号为 01。
- **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。
- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。
- **capabilities: bus_master cap_list：** 设备的功能列表，包括总线主控和容量列表。
- **configuration: latency=0：** 设备的配置信息，包括延迟。
- **resources: memory:5534c000-5534cfff：** 设备的资源信息，包括内存地址范围。

这些信息描述了系统外设设备的基本特征，包括其产品、制造商、物理标识符、总线信息、版本、功能列表、配置和资源等。值得注意的是，该设备被标记为未声明（UNCLAIMED），这可能意味着系统没有正确识别或配置该设备的驱动程序。

#### USB controller

##### usb1

这段信息描述了一个 USB 控制器（USB controller），下面是对每个字段的解释：

- **description: USB controller：** 设备的描述，表示这是一个 USB 控制器。

- **product: Tiger Lake-LP Thunderbolt 4 USB Controller：** 设备的产品名称，指明这是 Tiger Lake-LP Thunderbolt 4 USB 控制器。

- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。

- **physical id: d：** 设备的物理标识符，用于唯一标识系统中的硬件设备。

- **bus info: pci@0000:00:0d.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:0d.0`。

- **version: 01：** 设备的版本信息，表示这个设备的版本号为 01。

- **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。

- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。

- **capabilities: xhci cap_list：** 设备的功能列表，包括支持 USB 3.0 协议的 xHCI 控制器和容量列表。

- **configuration: driver=xhci_hcd latency=0：** 设备的配置信息，包括使用的驱动程序和延迟。

- **resources: irq:143 memory:55320000-5532ffff：** 设备的资源信息，包括中断请求（IRQ）和内存地址范围。

这些信息描述了 USB 控制器设备的基本特征，包括其产品、制造商、物理标识符、总线信息、版本、功能列表、配置和资源等。

##### usb2

这段信息描述了一个 USB 控制器（USB controller），下面是对每个字段的解释：

- **description: USB controller：** 设备的描述，表示这是一个 USB 控制器。

- **product: Tiger Lake-LP USB 3.2 Gen 2x1 xHCI Host Controller：** 设备的产品名称，指明这是 Tiger Lake-LP USB 3.2 Gen 2x1 xHCI 主机控制器。

- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。

- **physical id: 14：** 设备的物理标识符，用于唯一标识系统中的硬件设备。

- **bus info: pci@0000:00:14.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:14.0`。

- **version: 20：** 设备的版本信息，表示这个设备的版本号为 20。

- **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。

- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。

- **capabilities: xhci cap_list：** 设备的功能列表，包括支持 USB 3.2 Gen 2x1 协议的 xHCI 控制器和容量列表。

- **configuration: driver=xhci_hcd latency=0：** 设备的配置信息，包括使用的驱动程序和延迟。

- **resources: irq:144 memory:55330000-5533ffff：** 设备的资源信息，包括中断请求（IRQ）和内存地址范围。

这些信息描述了 USB 控制器设备的基本特征，包括其产品、制造商、物理标识符、总线信息、版本、功能列表、配置和资源等。

#### RAID总线控制器

这段信息描述了一个 RAID 总线控制器（RAID bus controller），下面是对每个字段的解释：

- **description: RAID bus controller：** 设备的描述，表示这是一个 RAID 总线控制器。

- **product: Volume Management Device NVMe RAID Controller：** 设备的产品名称，指明这是 Volume Management Device（VMD）NVMe RAID 控制器。

- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。

- **physical id: e：** 设备的物理标识符，用于唯一标识系统中的硬件设备。

- **bus info: pci@0000:00:0e.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:0e.0`。

- **version: 00：** 设备的版本信息，表示这个设备的版本号为 00。

- **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。

- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。

- **capabilities: raid bus_master cap_list：** 设备的功能列表，包括 RAID 功能、总线主控和容量列表。

- **configuration: driver=vmd latency=0：** 设备的配置信息，包括使用的驱动程序和延迟。

- **resources: irq:0 memory:50000000-51ffffff memory:52000000-53ffffff memory:55000000-550fffff：** 设备的资源信息，包括中断请求（IRQ）和内存地址范围。

这些信息描述了 RAID 总线控制器设备的基本特征，包括其产品、制造商、物理标识符、总线信息、版本、功能列表、配置和资源等。

#### 静态随机存取存储器

这段信息描述了一个未声明的内存设备（UNCLAIMED memory），下面是对每个字段的解释：

- **description: RAM memory：** 设备的描述，表示这是一个 RAM 内存。

- **product: Tiger Lake-LP Shared SRAM：** 设备的产品名称，指明这是 Tiger Lake-LP 共享的 SRAM（静态随机存取存储器）。

- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。

- **physical id: 14.2：** 设备的物理标识符，用于唯一标识系统中的硬件设备。

- **bus info: pci@0000:00:14.2：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:14.2`。

- **version: 20：** 设备的版本信息，表示这个设备的版本号为 20。

- **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。

- **clock: 33MHz (30.3ns)：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz，对应一个时钟周期为 30.3 纳秒。

- **capabilities: bus_master cap_list：** 设备的功能列表，包括总线主控和容量列表。

- **configuration: latency=0：** 设备的配置信息，包括延迟。

- **resources: memory:55340000-55343fff memory:5534d000-5534dfff：** 设备的资源信息，包括内存地址范围。

这些信息描述了内存设备的基本特征，包括其产品、制造商、物理标识符、总线信息、版本、功能列表、配置和资源等。值得注意的是，该内存设备被标记为未声明（UNCLAIMED），这可能意味着系统没有正确识别或配置该设备的驱动程序。

#### network interface

这段信息描述了一个网络接口（Network interface），下面是对每个字段的解释：

- **description: Wireless interface：** 设备的描述，表示这是一个无线接口。

- **product: Wi-Fi 6 AX201：** 设备的产品名称，指明这是 Wi-Fi 6 AX201 网络适配器。

- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。

- **physical id: 14.3：** 设备的物理标识符，用于唯一标识系统中的硬件设备。

- **bus info: pci@0000:00:14.3：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:14.3`。

- **logical name: wlp0s20f3：** 设备的逻辑名称，表示设备在系统中的命名。

- **version: 20：** 设备的版本信息，表示这个设备的版本号为 20。

- **serial: 68:3e:26:0e:6e:74：** 设备的序列号，用于唯一标识设备。

- **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。

- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。

- **capabilities: bus_master cap_list ethernet physical wireless：** 设备的功能列表，包括总线主控、以太网、物理和无线功能。

- **configuration: broadcast=yes driver=iwlwifi driverversion=6.5.0-28-generic firmware=77.2df8986f.0 QuZ-a0-hr-b0-77.u ip=192.168.43.188 latency=0 link=yes multicast=yes wireless=IEEE 802.11：** 设备的配置信息，包括广播、驱动程序、固件版本、IP 地址、延迟、链接状态和多播状态等。

- **resources: irq:16 memory:55344000-55347fff：** 设备的资源信息，包括中断请求（IRQ）和内存地址范围。

这些信息描述了网络接口设备的基本特征，包括其产品、制造商、物理标识符、总线信息、逻辑名称、版本、序列号、功能列表、配置和资源等。

#### 串行总线控制器（Serial bus controller）

这段信息描述了串行总线控制器（Serial bus controller），下面是对每个字段的解释：

1. **Serial bus controller #0：**

   - **description: Serial bus controller：** 设备的描述，表示这是一个串行总线控制器。
   - **product: Tiger Lake-LP Serial IO I2C Controller #0：** 设备的产品名称，指明这是 Tiger Lake-LP 的串行 IO I2C 控制器 #0。
   - **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。
   - **physical id: 15：** 设备的物理标识符，用于唯一标识系统中的硬件设备。
   - **bus info: pci@0000:00:15.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:15.0`。
   - **version: 20：** 设备的版本信息，表示这个设备的版本号为 20。
   - **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。
   - **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。
   - **capabilities: bus_master cap_list：** 设备的功能列表，包括总线主控和容量列表。
   - **configuration: driver=intel-lpss latency=0：** 设备的配置信息，包括使用的驱动程序和延迟。
   - **resources: irq:27 memory:3f400000-3f400fff：** 设备的资源信息，包括中断请求（IRQ）和内存地址范围。

#### 通信控制器（Communication controller）

这段信息描述了一个通信控制器（Communication controller），下面是对每个字段的解释：

- **description: Communication controller：** 设备的描述，表示这是一个通信控制器。

- **product: Tiger Lake-LP Management Engine Interface：** 设备的产品名称，指明这是 Tiger Lake-LP 的管理引擎接口。

- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。

- **physical id: 16：** 设备的物理标识符，用于唯一标识系统中的硬件设备。

- **bus info: pci@0000:00:16.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:16.0`。

- **version: 20：** 设备的版本信息，表示这个设备的版本号为 20。

- **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。

- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。

- **capabilities: bus_master cap_list：** 设备的功能列表，包括总线主控和容量列表。

- **configuration: driver=mei_me latency=0：** 设备的配置信息，包括使用的驱动程序和延迟。

- **resources: irq:156 memory:55350000-55350fff：** 设备的资源信息，包括中断请求（IRQ）和内存地址范围。

这些信息描述了通信控制器设备的基本特征，包括其产品、制造商、物理标识符、总线信息、版本、功能列表、配置和资源等。

PCI 桥接器（PCI bridge）

**PCI bridge：**

- **description: PCI bridge：** 设备的描述，表示这是一个 PCI 桥接器。
- **product: Intel Corporation：** 设备的产品名称，指明这是 Intel 公司的产品。
- **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。
- **physical id: 1c：** 设备的物理标识符，用于唯一标识系统中的硬件设备。
- **bus info: pci@0000:00:1c.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:1c.0`。
- **version: 20：** 设备的版本信息，表示这个设备的版本号为 20。
- **width: 32 bits：** 设备的数据传输宽度，表示这个设备支持 32 位数据传输。
- **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。
- **capabilities: pci normal_decode bus_master cap_list：** 设备的功能列表，包括 PCI 编码、总线主控和容量列表。
- **configuration: driver=pcieport：** 设备的配置信息，包括使用的驱动程序。
- **resources: irq:122 memory:55200000-552fffff：** 设备的资源信息，包括中断请求（IRQ）和内存地址范围。

#### ISA 桥接器（ISA bridge）and PnP 设备（Plug and Play devices）

这段信息描述了一个 ISA 桥接器（ISA bridge）和一系列 PnP 设备（Plug and Play devices），下面是对每个字段的解释：

- **ISA bridge：**
  - **description: ISA bridge：** 设备的描述，表示这是一个 ISA 桥接器。
  - **product: Tiger Lake-LP LPC Controller：** 设备的产品名称，指明这是 Tiger Lake-LP 的 LPC 控制器。
  - **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。
  - **physical id: 1f：** 设备的物理标识符，用于唯一标识系统中的硬件设备。
  - **bus info: pci@0000:00:1f.0：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:1f.0`。
  - **version: 20：** 设备的版本信息，表示这个设备的版本号为 20。
  - **width: 32 bits：** 设备的数据传输宽度，表示这个设备支持 32 位数据传输。
  - **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。
  - **capabilities: isa bus_master：** 设备的功能列表，包括 ISA 总线主控。
  - **configuration: latency=0：** 设备的配置信息，包括延迟。

- **PnP devices：**
  - **product: PnP device PNP0c02：** 设备的产品名称，表示这是一个 PnP 设备。
  - **physical id: [编号]：** 设备的物理标识符，用于唯一标识系统中的硬件设备。
  - **capabilities: pnp：** 设备的功能列表，表示这是一个 PnP 设备。
  - **configuration: driver=[驱动程序]：** 设备的配置信息，包括使用的驱动程序。

这些信息描述了一个 ISA 桥接器和一系列 PnP 设备的基本特征，包括其产品、制造商、物理标识符、总线信息、版本、功能列表和配置等。

#### 多媒体音频控制器（Multimedia audio controller）

这段信息描述了一个多媒体音频控制器（Multimedia audio controller），下面是对每个字段的解释：

- **Multimedia audio controller：**
  - **description: Multimedia audio controller：** 设备的描述，表示这是一个多媒体音频控制器。
  - **product: Tiger Lake-LP Smart Sound Technology Audio Controller：** 设备的产品名称，指明这是 Tiger Lake-LP 的智能声音技术音频控制器。
  - **vendor: Intel Corporation：** 设备的制造商，表示这个设备由 Intel 公司制造。
  - **physical id: 1f.3：** 设备的物理标识符，用于唯一标识系统中的硬件设备。
  - **bus info: pci@0000:00:1f.3：** 设备的总线信息，说明这个设备连接在 PCI 总线上，地址为 `0000:00:1f.3`。
  - **logical name: card0, /dev/snd/controlC0, /dev/snd/hwC0D0, /dev/snd/hwC0D2, ...：** 设备的逻辑名称，表示这个设备在系统中的逻辑标识符，包括声卡控制、硬件设备等。
  - **version: 20：** 设备的版本信息，表示这个设备的版本号为 20。
  - **width: 64 bits：** 设备的数据传输宽度，表示这个设备支持 64 位数据传输。
  - **clock: 33MHz：** 设备的时钟频率，表示设备的工作时钟频率为 33MHz。
  - **capabilities: bus_master cap_list：** 设备的功能列表，包括总线主控和能力列表。
  - **configuration: driver=sof-audio-pci-intel-tgl latency=32：** 设备的配置信息，包括使用的驱动程序和延迟。
  - **resources: irq:168 memory:55348000-5534bfff memory:55100000-551fffff：** 设备的资源信息，包括中断请求（IRQ）和内存地址范围。

## [unicode编码方式](https://home.unicode.org/)

## w3c网页标准

### [校验网页](https://validator.w3.org/#validate_by_upload+with_options)

<a name="media"> </a>

# media

## video

### mini video

## picture

### [gimp](#gimp)

<a name="uniapp"> </a>

# uniapp

## hbuider安装

- 首先去官网下载安装包
- 然后解压（这时注意，可以直接解压到program file文件夹下面，一般在Download下面可能后来会移动，会比较麻烦）
- 下载相关引擎，由于是在program file文件下下载，所以要开启管理员才可以



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
