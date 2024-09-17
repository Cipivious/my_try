# html-and-css

## 学习工具

### [headfirst html](file:///home/yang/ebooks/web/Head%20First%20HTML%E4%B8%8ECSS%E4%B8%AD%E6%96%87%E7%89%88.pdf)

### [tools](#use emacs to write html)

### [Documenting web technologies, including CSS, HTML, and JavaScript, since 2005.](https://developer.mozilla.org/en-US/)

### [Web 开发技术MDN中文网页](https://developer.mozilla.org/zh-CN/docs/Web)

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

## 基础学习笔记

### html元素的种类

[HTML 元素参考](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element)

### cursor样式

在CSS中，`cursor` 属性定义了鼠标指针在元素上悬停时的外观。除了 `pointer`（通常表示链接或可点击的元素）之外，还有许多其他的 `cursor` 值。以下是一些常见的 `cursor` 样式：

1. **default**：默认光标（通常是一个箭头）。
2. **none**：不显示光标。
3. **context-menu**：显示上下文菜单的光标。通常显示为带有箭头的菜单图标。
4. **help**：显示帮助信息的光标。通常是一个带有问号的圆圈或箭头。
5. **progress**：表示程序正忙的光标。通常是旋转的圆圈或沙漏形状。
6. **wait**：与 `progress` 类似，但不太常见。
7. **text**：表示文本选择的光标（通常是I形光标）。
8. **crosshair**：十字线光标，用于精确选择。
9. **move**：表示对象可以移动的光标（通常是四个方向的箭头）。
10. **e-resize, ne-resize, n-resize, nw-resize, w-resize, sw-resize, s-resize, se-resize**：这些值表示光标指向的方向，并指示对象可以在该方向上调整大小。
11. **vertical-text**：表示垂直文本选择的光标。
12. **alias**：通常是一个小的带有箭头的圆圈，表示该对象可能有别名。
13. **cell**：表示单元格边界的光标。
14. **copy**：表示复制操作的光标，通常是一个带有加号的箭头。
15. **no-drop**：表示该元素不能接受放置操作的光标（例如，防止拖放操作）。
16. **grab, grabbing**：这些值用于表示拖动操作。`grab` 是未拖动时的光标，而 `grabbing` 是正在拖动时的光标。
17. **zoom-in, zoom-out**：表示放大或缩小的光标。

### 块元素与内联元素

在HTML中，元素可以分为块级元素（block-level elements）和内联元素（inline elements），它们在文档中的布局和显示行为有所不同。

**块级元素**：

1. 块级元素会在页面上以独立的块状区域显示，即元素会占据一整行或者一整个父容器的宽度。
2. 块级元素可以包含其他块级元素或者内联元素。
3. 常见的块级元素包括 `<div>`、`<p>`、`<h1>` - `<h6>`、`<ul>`、`<ol>`、`<li>`、`<blockquote>` 等。

**内联元素**：

1. 内联元素通常在行内显示，即它们不会独占一行，而是在同一行内随文本流动。
2. 内联元素只能容纳文本或者其他内联元素，不能包含块级元素。
3. 常见的内联元素包括 `<span>`、`<a>`、`<strong>`、`<em>`、`<img>`、`<br>`、`<input>` 等。

### css样式大全

[CSS的常用套路(附demo的效果实现与源码)](https://zhuanlan.zhihu.com/p/107741668?utm_psn=1773115017446977536)

[css样式](file:///home/yang/ebooks/web/css.pdf)

[这是google默认的字体css](https://fonts.googleapis.com/css?family=Open+Sans:400italic,700italic,700,400&subset=latin,latin-ext)

### 使用浏览器的开发者工具

浏览器的开发者工具具有非常强大的功能

- 增加或者取消css样式
- 查看样式的具体数值
- 获得具体的样式内容

<img src="https://raw.githubusercontent.com/Cipivious/my_try/main/image/截图 2024-04-23 19-35-05.png" alt="开发者工具" style="zoom: 33%;" />

### [在线颜色表](https://tool.oschina.net/commons?type=3)

## 加载html速度

### 提高性能

如果你的 HTML 文件太大导致加载缓慢，可以尝试以下几种方法来优化页面加载性能：

1. **压缩文件大小：** 使用压缩工具（如 Gzip）对 HTML 文件进行压缩，减小文件大小，从而加快加载速度。
2. **优化图片大小：** 如果 HTML 文件中包含大量的图片，请确保图片经过压缩和优化，以减小文件大小。你可以使用工具（如 Photoshop、TinyPNG）来优化图片。
3. **延迟加载：** 使用延迟加载技术（如懒加载或按需加载）来延迟加载 HTML 文件中的部分内容，只有当用户需要时才加载，而不是一次性加载所有内容。
4. **分页加载：** 如果可能的话，将大文件拆分成多个小文件，并使用分页加载技术来分批加载内容，从而减少单个页面的加载时间。
5. **异步加载：** 使用 JavaScript 来异步加载页面中的部分内容，例如使用 AJAX 技术加载动态内容或者使用模块化加载器加载模块化的 JavaScript 脚本。
6. **CDN 加速：** 将静态资源（如图片、样式表、脚本）部署到 CDN（内容分发网络）上，加速文件的下载速度。
7. **缓存优化：** 使用合适的缓存策略来优化页面的缓存效果，减少重复加载相同内容的次数，例如设置合适的缓存控制头和 ETag。
8. **优化网络请求：** 减少页面中的网络请求次数，合并和压缩文件，减小文件大小，优化 HTTP 请求。

### 形成缓存

通过结合以上多种优化方法，可以有效地提高页面加载性能，减少页面加载时间。

可以通过使用浏览器的缓存机制来实现让用户在第一次加载页面后形成缓存，从而在下次访问时快速加载页面。常用的缓存策略包括：

1. **HTTP 缓存控制头：** 使用合适的 HTTP 缓存控制头来指示浏览器如何缓存页面内容。常用的缓存控制头包括 `Cache-Control` 和 `Expires`。
2. **ETag：** 使用 ETag（实体标签）来标识页面内容的版本，当页面内容发生变化时，ETag 也会发生变化，浏览器可以通过比较 ETag 来确定是否需要重新加载页面内容。
3. **Service Worker：** 使用 Service Worker 技术来在浏览器中实现自定义的缓存策略，可以缓存页面内容、资源文件等，并在网络不可用时提供离线访问功能。
4. **LocalStorage 和 SessionStorage：** 使用浏览器的本地存储功能（如 LocalStorage 和 SessionStorage）来缓存页面数据，可以在用户关闭浏览器后仍然保存缓存数据，下次访问时直接加载。
5. **IndexedDB：** 使用浏览器的 IndexedDB API 来创建客户端的数据库，可以存储大量数据并提供高性能的读写操作，适用于需要持久化存储的数据。

通过结合以上多种缓存策略，可以实现在用户第一次加载页面时形成缓存，并在下次访问时快速加载页面内容。需要根据页面特点和需求选择合适的缓存策略，并进行相应的实现和配置。

## 页面宽度调整

[HTML适应手机浏览器宽度](https://blog.csdn.net/wusuopuBUPT/article/details/21941343)

## Chrome查看手机端样式

要使用 Google Chrome 的开发者工具查看网页在手机上的效果，可以按照以下步骤操作：

1. 打开 Google Chrome 浏览器，并进入你想要查看的网页。
2. 打开开发者工具：
   - 在 Windows 或 Linux 上，按下 `F12` 键或者 `Ctrl + Shift + I` 组合键。
   - 在 macOS 上，按下 `Cmd + Opt + I` 组合键。
3. 进入移动设备模拟器模式：
   - 在开发者工具的顶部菜单栏中，点击 Toggle Device Toolbar 图标（或者按下 `Ctrl + Shift + M`），即可进入移动设备模拟器模式。
4. 选择要模拟的设备类型：
   - 在工具栏的左上角，点击下拉菜单按钮，选择你想要模拟的移动设备类型，如 iPhone、iPad 等。
   - 或者点击 Responsive 按钮，手动调整视口大小和缩放比例。
5. 查看网页效果：
   - 此时，你会看到网页以模拟设备的尺寸和分辨率显示在开发者工具中。
   - 你可以在模拟器中与网页进行交互，查看在不同设备上的显示效果，并且可以检查调试网页中的元素和样式。

