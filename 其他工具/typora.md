# typora

[设置自动编号](https://support.typora.io/Auto-Numbering/)
---------------------------------------------------------

[typora设置标题自动编号](https://blog.csdn.net/juluwangriyue/article/details/125467325)

1. 打开主题文件夹
2. 添加网页中的css内容
3. 重新打开即可

## 修改typora配置文件自定义快捷键

![修改配置文件](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240508124929616.png)

## 使用typora创作论文

### [typora-theme-essay_cn](https://github.com/du33169/typora-theme-essay_cn.git)

### [解决引用的问题](https://pandoc.org/chunkedhtml-demo/7.6-other-extensions.html#org-citations)

### [图片引用](https://github.com/tomduck/pandoc-fignos)

### [论文写作](https://zhuanlan.zhihu.com/p/395193554)

pandoc --citeproc --bibliography=myref.bib --number-sections  -M reference-section-title="Reference" --csl=chinese-gb7714-2005-numeric.csl  demo-figref.md -o demo-figref.docx

### 添加头部信息

```text
---
title:  'This is the title: it contains a colon'
author:
- Author One
- Author Two
keywords: [nothing, nothingness]
abstract: |
  This is the abstract.

  It consists of two paragraphs.
---
```

### css与csl

CSS（Cascading Style Sheets，层叠样式表）和CSL（Citation Style Language，引文样式语言）在定义、用途和上下文环境等方面存在显著的差异。

CSS是一种用于描述HTML或XML（包括如SVG、MathML等衍生技术）等文档样式的计算机语言。它的主要功能是通过对网页中元素样式的描述，包括布局、颜色、字体等，来美化网页的外观和排版。CSS的语法规则允许网页制作者选择特定的HTML元素，并为这些元素定义样式。CSS选择器用于确定哪些元素将应用特定的样式，而CSS声明则定义了这些样式的内容。

而CSL则是一种用于描述引文风格的XML文件。它定义了文内引用和参考文献列表的外观和格式，为引文管理器（如Zotero、Mendeley等）提供了如何渲染文内引用和文献列表的指令。CSL支持各种引文风格，如APA、MLA、Chicago等。CSL文件使用XML的语法规则，这是一种用于存储和传输数据的标记语言，通过标签来标识文档中的数据。

在联系方面，CSS和CSL都是计算机编程和网页设计中的一部分，但它们在各自的领域中发挥着不同的作用。CSS主要用于网页的美化和排版，而CSL则用于定义和格式化引文。虽然两者在语法上有所不同，但它们都遵循一定的规则和约定，以实现特定的功能。

总的来说，CSS和CSL在定义、用途和上下文环境等方面存在显著的差异，但在各自的领域中都具有重要的作用。

### [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref?tab=readme-ov-file)

pandoc-crossref is a pandoc filter for numbering figures, equations, tables and cross-references to them.

The input file (like [demo.md](https://raw.githubusercontent.com/lierdakil/pandoc-crossref/master/docs/demo/demo.md)) can be converted into [HTML](http://lierdakil.github.io/pandoc-crossref/demo/output.html), [LaTeX](http://lierdakil.github.io/pandoc-crossref/demo/output.latex), [PDF](http://lierdakil.github.io/pandoc-crossref/demo/output.pdf), [Markdown](http://lierdakil.github.io/pandoc-crossref/demo/output.md) or other formats.

### 示例代码

```bash
sudo apt install pandoc
cd Downloads(我在这里下载了pandoc-crossref插件)
tar -xf pandoc-crossref.tz(解压之后直接是一个可以直接执行的二进制文件)
sudo cp pandoc-crossref /usr/bin (将它添加到可执行文件的路径)
cd ~/typora/essay_sample
pandoc --from=markdown+raw_html --citeproc --bibliography=myref.bib --csl=chinese-gb7714-2005-numeric.csl --reference-doc ../typora-theme-essay_cn/templates/Word_style/word_ref.docx --pdf-engine=xelatex -F pandoc-crossref --metadata crossrefYaml=crossref_config.yaml   essay_sample.md -o essay_sample.docx
 这里面--citeproc选项处理的是引用
 billiography 是bib文件的路径
 csl 是描述引文风格的样式文件
 reference-doc 是样式的模板的路径
 pdf-engine 是转化pdf的可执行命令
 -F 是插件的描述
 metadata 这里描述的是引文的风格 
```



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

## 插件

### [增强插件](https://www.zhihu.com/question/22504694/answer/3471318059?utm_psn=1774719289515671553)

#### [安装教程](https://madmaxchow.github.io/VLOOK/index.html)

#### 说明

其实它只是一个主题样式，类似一个css文件，但是它在导出的时候分别在body和head里添加了一部分内容，使得排版完成。