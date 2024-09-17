# javascript

Object
------

在你提供的代码片段中，`Object` 并不是用来创建对象的关键字，而是作为一个全局对象的构造函数被使用。让我来解释这段代码，特别是关于 `Object` 的用法和上下文。

### 分析代码段：

```javascript
x = function() {
    var e = Object(n.a)((function*(e) {
        return (yield Object(w.a)({
            url: "/sign_up_block/check_user",
            method: "POST",
            data: {
                googleRecaptchaTokenV3: e
            }
        })).data
    }));
};
```

在这段代码中：

1. `Object(n.a)`：这里的 `Object` 是 JavaScript 的全局对象构造函数。它通常用于创建一个新的对象。但在这里，它不是在创建一个新对象，而是在调用一个可能由 `n.a` 提供的函数或者值。这种用法可能是为了确保 `n.a` 返回的是一个对象，或者通过某种方式处理 `n.a` 返回的值。

2. `Object(w.a)`：同样地，这里也是使用 `Object` 构造函数来调用一个可能由 `w.a` 提供的函数或者值。这种用法可能是在处理异步请求的过程中，确保返回的是一个对象。

### Object 构造函数的一般用法：

- **创建对象**：最常见的用法是通过对象字面量 `{}` 或者 `new Object()` 来创建一个空对象或者具有初始属性的对象。

  ```javascript
  let obj1 = {};  // 使用对象字面量创建空对象
  let obj2 = new Object();  // 使用 Object 构造函数创建空对象
  ```

- **包装非对象值**：当传入一个非对象值时，`Object` 构造函数会将其包装成相应的对象。

  ```javascript
  let num = 10;
  let numObj = Object(num);  // 包装数字值为 Number 对象
  ```

- **调用对象的构造函数**：在某些情况下，可以使用 `Object` 构造函数来调用其他对象的构造函数。

  ```javascript
  function Person(name) {
      this.name = name;
  }
  
  let alice = Object(Person)("Alice");
  console.log(alice);  // 输出: Person { name: 'Alice' }
  ```

- **全局对象**：`Object` 是 JavaScript 的全局对象之一，在浏览器环境下可以直接访问。

### 总结：

在你提供的代码片段中，`Object(n.a)` 和 `Object(w.a)` 的用法不是典型的对象创建方式，而是可能在处理异步操作或确保返回对象的情况下使用。这种用法需要查看 `n.a` 和 `w.a` 的具体实现和用途，以理解它们返回值的处理逻辑。

匿名函数
--------

当谈论匿名函数时，通常指的是没有明确名称的函数，可以直接赋值给变量或者作为参数传递给其他函数。在 JavaScript 中，最常见的匿名函数形式是使用函数表达式或者箭头函数。

### 函数表达式的匿名函数例子：

1. **普通函数表达式**：

```javascript
let greet = function(name) {
    return `Hello, ${name}!`;
};

console.log(greet("John"));  // 输出: Hello, John!
```

在上述例子中，`greet` 是一个变量，它存储了一个匿名的普通函数，这个函数可以接收一个 `name` 参数并返回相应的问候语。

2. **箭头函数**：

```javascript
let multiply = (a, b) => a * b;

console.log(multiply(5, 3));  // 输出: 15
```

在这个例子中，`multiply` 是一个变量，存储了一个匿名的箭头函数，它接收两个参数 `a` 和 `b`，并返回它们的乘积。

### 匿名函数作为参数传递的例子：

匿名函数经常用作回调函数传递给其他函数，例如 `Array.prototype.map()` 或 `setTimeout()` 等函数。

1. **使用 `Array.prototype.map()`**：

```javascript
let numbers = [1, 2, 3, 4, 5];

let doubled = numbers.map(function(x) {
    return x * 2;
});

console.log(doubled);  // 输出: [2, 4, 6, 8, 10]
```

在这个例子中，匿名函数 `function(x) { return x * 2; }` 被传递给 `map` 方法作为映射函数，用来将数组 `numbers` 中的每个元素都乘以 2。

2. **使用 `setTimeout()`**：

```javascript
setTimeout(function() {
    console.log("Hello, World!");
}, 1000);
```

在这个例子中，匿名函数 `function() { console.log("Hello, World!"); }` 被传递给 `setTimeout` 函数，作为延迟执行的回调函数，它在 1000 毫秒后输出 "Hello, World!"。

### 匿名函数的使用场景：

- 当函数只在一个地方使用，没有必要定义具名函数。
- 作为函数参数传递，简化代码逻辑。
- 使用箭头函数可以更加简洁地表达函数逻辑。

总之，匿名函数在 JavaScript 中非常常见和实用，用于各种场景，从简单的数据转换到复杂的异步操作。

## 学习笔记

### [d3.js](https://d3js.org/d3-fetch#svg)

D3是一个用于数据可视化的强大工具，它能够加载很多种不同格式的内容，比如db数据库，svg格式图片，csv格式数据，json格式数据。它也能用很多种不同的格式进行展示，比如表格，图像，坐标轴图像。	

下面是使用它展示svg图像的一个示例：

```html
<body>
  <div id="svg-container"></div>
  <script>
    // Load the SVG file
    d3.xml("mode.svg").then(data => {
      // Append the loaded SVG to the container
      document.getElementById("svg-container").appendChild(data.documentElement);

      // Select the SVG
      const svg = d3.select("#svg-container svg");

      // Add click event to nodes to toggle visibility
      svg.selectAll("g").on("click", function(event) {
        const node = d3.select(this);
        const childNodes = node.selectAll("g");

        // Toggle visibility
        childNodes.classed("hidden", !childNodes.classed("hidden"));
      });
    }).catch(error => {
      console.error("Error loading the SVG:", error);
    });
  </script>
</body>
```



### 改变节点文本步骤

![改变节点文本步骤](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240505104158483.png)

![例子](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240505104514586.png)

### javascript新建一个网页对象

使用jsdom虽然有好处，但对于初学者来说有点复杂，不太建议尝试，建议使用浏览器的环境来学习js，可以先创建一个标准的html模板，比如

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Validation Example</title>
</head>
<body>
    <input type="text" id="inputField">
    <span id="helpText"></span>

    <script>
		//在此处引用你的脚本，用来测试js的效果
    </script>
</body>
</html>
```



```js
const http = require('http');
const { JSDOM } = require('jsdom');

// 创建一个HTTP服务器
const server = http.createServer((req, res) => {
  // 创建一个虚拟的DOM
  const dom = new JSDOM(`<!DOCTYPE html><html><head><title>Node.js Generated Page</title></head><body></body></html>`);

  // 获取虚拟DOM中的document对象
  const document = dom.window.document;

  // 在虚拟DOM中添加HTML内容
  const heading = document.createElement('h1');
  heading.textContent = 'Hello, world!';
  document.body.appendChild(heading);

  // 设置响应头
  res.writeHead(200, {'Content-Type': 'text/html'});

  // 发送HTML内容到浏览器
  res.end(dom.serialize());
});

// 监听端口
const port = 3000;
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
```



### 元素及其方法

[Element](https://developer.mozilla.org/zh-CN/docs/Web/API/Element)

**`Element`** 是最通用的基类，[`Document`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document) 中的所有元素对象（即表示元素的对象）都继承自它。它只具有各种元素共有的方法和属性。更具体的类则继承自 `Element`。

例如，[`HTMLElement`](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLElement) 接口是所有 HTML 元素的基本接口。同样，[`SVGElement`](https://developer.mozilla.org/zh-CN/docs/Web/API/SVGElement) 接口是所有 SVG 元素的基本接口，而 [`MathMLElement`](https://developer.mozilla.org/zh-CN/docs/Web/API/MathMLElement) 接口则是 MathML 元素的基础接口。大多数功能是在这个类的更深层级的接口中被进一步制定的。

在 Web 平台的领域以外的语言，比如 XUL，通过 `XULElement` 接口，同样也实现了 `Element` 接口。

### 获取元素的方法

除了 `getElementById` 外，还有其他一些获取 HTML 中指定元素的方法，其中一些常见的方法包括：

1. **querySelector**：通过 CSS 选择器选择匹配的第一个元素。

   ```javascript
   var element = document.querySelector(".className"); // 通过类名选择
   var element = document.querySelector("#idName"); // 通过 id 选择
   var element = document.querySelector("tag"); // 通过标签名选择
   ```

2. **querySelectorAll**：通过 CSS 选择器选择匹配的所有元素，返回一个 NodeList 对象。

   ```javascript
   var elements = document.querySelectorAll(".className"); // 通过类名选择所有匹配元素
   var elements = document.querySelectorAll("tag"); // 通过标签名选择所有匹配元素
   ```

3. **getElementsByClassName**：通过类名获取所有匹配的元素，返回一个 HTMLCollection 对象。

   ```javascript
   var elements = document.getElementsByClassName("className"); // 通过类名获取所有匹配元素
   ```

4. **getElementsByTagName**：通过标签名获取所有匹配的元素，返回一个 HTMLCollection 对象。

   ```javascript
   var elements = document.getElementsByTagName("tag"); // 通过标签名获取所有匹配元素
   ```

5. **getElementsByName**：通过元素的 name 属性获取所有匹配的元素，返回一个 NodeList 对象。

   ```javascript
   var elements = document.getElementsByName("nameValue"); // 通过 name 属性获取所有匹配元素
   ```

这些方法各有不同的用途，可以根据需要选择适合的方法来获取 HTML 中的元素。

### 事件类型

以下是一些常见的事件类型：

1. **点击事件（click）**：当用户单击元素时触发。
2. **双击事件（dblclick）**：当用户双击元素时触发。
3. **鼠标按下事件（mousedown）**：当鼠标按钮被按下时触发。
4. **鼠标松开事件（mouseup）**：当鼠标按钮被释放时触发。
5. **鼠标移动事件（mousemove）**：当鼠标指针在元素上移动时触发。
6. **鼠标滚轮事件（wheel）**：当鼠标滚轮滚动时触发。
7. **元素获取焦点事件（focus）**：当元素获得焦点时触发。
8. **元素失去焦点事件（blur）**：当元素失去焦点时触发。
9. **元素的值改变事件（change）**：当元素的值发生改变时触发。
10. **元素内容变化事件（input）**：当元素的内容发生变化时触发。
11. **鼠标右键菜单事件（contextmenu）**：当用户右键点击元素时触发。
12. **元素加载事件（load）**：当元素加载完成时触发，例如图片加载完成或页面加载完成。
13. **元素卸载事件（unload）**：当元素被卸载（例如页面被关闭或刷新）时触发。
14. **触摸事件（touchstart/touchend/touchmove）**：当触摸屏设备上的用户触摸元素时触发。
15. **错误事件（error）**：当元素加载过程中发生错误时触发，例如图片加载失败或脚本加载失败。
16. **键盘按下事件（keydown）**：当用户按下键盘上的任意键时触发。
17. **键盘松开事件（keyup）**：当用户释放键盘上的任意键时触发。
18. **键盘按下并松开事件（keypress）**：当用户按下并松开键盘上的任意键时触发。
19. **滚动事件（scroll）**：当元素的滚动条滚动时触发。
20. **窗口大小变化事件（resize）**：当窗口大小发生变化时触发。
21. **表单提交事件（submit）**：当表单提交时触发。
22. **拖拽事件（drag）**：当元素被拖动时触发。
23. **播放事件（play）**：当音频或视频播放时触发。
24. **动画开始/结束事件（animationstart/animationend）**：当 CSS 动画开始或结束时触发。
25. **过渡开始/结束事件（transitionstart/transitionend）**：当 CSS 过渡效果开始或结束时触发。

这只是一小部分可用事件类型的示例。通过 `addEventListener` 方法，你可以为任何支持的事件类型添加事件监听器，以响应用户的交互和页面的变化。

在创建 input 元素并添加事件监听器时，应该先将 input 元素添加到 DOM 中，然后再添加事件监听器。这样才能确保 input 元素已经存在于 DOM 中，事件监听器才能正常工作。

### addEventListener

`addEventListener` 是 JavaScript 中用于向 HTML 元素添加事件监听器的方法。通过 `addEventListener` 方法，你可以指定当特定事件发生时，要执行的 JavaScript 函数。

语法格式如下：

```
element.addEventListener(event, function, useCapture);
```

- `element`：要添加事件监听器的 HTML 元素。
- `event`：要监听的事件的名称，比如 "click"、"mouseover"、"keydown" 等。
- `function`：当事件发生时要执行的 JavaScript 函数。
- `useCapture`：一个可选的布尔值参数，表示事件是否在捕获阶段触发。默认为 false，即在冒泡阶段触发事件。

### innerHTML

`innerHTML` 是 JavaScript 中用于获取或设置 HTML 元素内容的属性。它是 DOM（文档对象模型）中的一个属性，可以用于操作 HTML 元素的内容。

- 当你使用 `element.innerHTML` 时，它会返回指定元素内部的 HTML 标记和文本内容。
- 当你设置 `element.innerHTML = "some HTML content"` 时，它会将指定元素内部的 HTML 内容替换为新的 HTML 内容。

例如，在以下示例中：

```
<div id="example">This is some text.</div>
```

如果你使用 JavaScript 来获取 `example` 元素的 `innerHTML` 属性：

```
var content = document.getElementById("example").innerHTML;
console.log(content); // 输出: This is some text.
```

而如果你将 `example` 元素的 `innerHTML` 属性设置为新的 HTML 内容：

```
document.getElementById("example").innerHTML = "<p>This is new content.</p>";
```

那么 `example` 元素的内容将被替换为新的 HTML 内容 `<p>This is new content.</p>`。

### 段落内部内容读写

```html
<!DOCTYPE html>
<html>
<head>
    <title>Adjusting content inside <p> tag</title>
    <script>
        // 获取 <p> 标签内的内容并调整
        function adjustParagraphContent() {
            // 获取 <p> 元素
            var paragraph = document.getElementById("paragraph");

            // 获取 <p> 元素内的文本内容
            var paragraphContent = paragraph.textContent;
    
            // 在控制台输出原始内容
            console.log("原始内容：" + paragraphContent);
    
            // 在这里进行你想要的操作，比如替换文本、添加内容等
            // 这里只是一个简单的示例，将文本内容转换为大写
            paragraph.textContent = paragraphContent.toUpperCase();
       	    alert("paragraph.textContent is "+paragraph.textContent+".");
        }
    </script>
</head>
<body>
    <!-- 点击按钮调用 adjustParagraphContent 函数 -->
    <button onclick="adjustParagraphContent()">调整内容</button>

    <!-- 包含内容的 <p> 标签 -->
    <p id="paragraph">lsfjlsdjf。</p>
</body>
</html>
```

### document.createElement

`document.createElement()` 是 JavaScript 中的一个 DOM 方法，用于在文档中动态创建新的 HTML 元素。它的语法如下：

```javascript
document.createElement(tagName)
```

其中 `tagName` 是要创建的元素的标签名，比如 `"div"`、`"p"`、`"img"` 等。

使用 `document.createElement()` 方法可以在 JavaScript 中创建新的 HTML 元素，然后可以通过其他 DOM 方法和属性对其进行操作和设置。一般的步骤包括：

1. 调用 `document.createElement(tagName)` 创建一个新的元素节点。
2. 可以使用其他 DOM 方法（比如 `setAttribute()`）来设置元素的属性，比如 `id`、`class`、`src` 等。
3. 将创建的元素添加到文档中的某个位置，可以是文档的某个容器元素内部，或者是其他元素的子元素。

以下是一个简单的例子，演示如何使用 `document.createElement()` 创建一个新的 `<div>` 元素，并将其添加到文档中：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Element Example</title>
</head>
<body>
    <!-- HTML 中的一个容器元素 -->
    <div id="container"></div>

    <script>
        // 创建一个新的 div 元素
        var newDiv = document.createElement("div");

        // 设置新元素的一些属性
        newDiv.id = "newElement";
        newDiv.textContent = "This is a new element!";

        // 获取容器元素
        var container = document.getElementById("container");

        // 将新元素添加到容器中
        container.appendChild(newDiv);
    </script>
</body>
</html>
```

在这个例子中，JavaScript 创建了一个新的 `<div>` 元素，设置了它的 `id` 和文本内容，然后将其添加到文档中的一个容器元素内部。

### 产生4行7列的伪随机数

```js
arr = Array.from({ length:4}, () => Array.from({length:7}, ()=>(Math.random() >= 0.5)))
```



### 选择

#### if else

```js
if (curScene ==0) {
	    curScene = 1;
	    message = "Your journey begins at a fork in the road.";
	}
	else if (curScene == 3) {
	    if (option == 1) {
		curScene = 6;
		message = "Sorry, a troll lives on the other side of the bridge and you just became his lunch.";
	    }
	    else if {
		curScene = 7;
		message = "Your stare is interrupted by the arrival of a huge troll.";
	    }
	}
```



#### switch

```js
	  switch (curScene) {
	  case 0:
	      curScene = 1;
	      message = "Your journey begins at a fork in the end.";
	      break;
	  case 1:
	      if (decision == 1) {
		  curScene = 2;
		  message = "Take the path.";
	      }
	      else {
		  curScene = 3;
		  message = "Take the bridge";
	      }
	      break;
      }
```

### 循环

#### for循环

```js
for (let i = 0; i < showTime.length; i++) {
	console.log("The time is " + showTime[i] + " now.")
}
```

#### while循环

```js
var count = 10;
while (count > 0) {
    count--;
    console.log("you are stupid.")
}
console.log("sorry, you are smart!")
```



### 正则表达式

```js
> regex = /^[0-9a-zA-Z]{2}\/\d{2}\/\d{2,4}$/
> regex.test("kj/37/2389")
true

//^ 表示开头
//$ 表示结尾
//\d 表示数字
//\w 表示字母和数字
//[0-9a-zA-Z] 表示匹配符合条件的任何一个
//{min,max} 表示匹配的个数范围
//. 表示匹配任意一个除了"\n"的字符
//* 表示模式是可选的，可以出现一次或任意多次，也可以不出现
//()? 括号内的内容可以出现，也可以不出现
//()+ 表示括号内容可以出现一次或者多次
//(A|B) 表示出现A或者出现B

//组合拳
// /.+/ 匹配任意字符，但需要超过一次以上，也就是匹配非空
// /\w*/ 匹配空和任意字母数字
```





### 引入其他文件的内容

果您希望在 `myjs.js` 文件中定义的变量在其他文件中可用，您需要将它们导出。在 `myjs.js` 文件中，您可以使用 `module.exports` 导出 `showTime` 变量，使其在其他文件中可用。

下面是一个示例 `myjs.js` 文件如何导出 `showTime` 变量：

```
// myjs.js
let showTime = ["12:30", "2:45", "5:00", "7:15", "9:30"];
module.exports = showTime;
```

要在 Node.js 交互式命令行中使用您在 `myjs.js` 文件中定义的变量，您需要通过 `require` 函数将该文件导入到 Node.js 中。然后，您就可以在交互式命令行中使用该文件中定义的变量了。

`let myVar = require('./myjs.js');`

### 声明变量

在 JavaScript 中，`let`、`var` 和 `const` 是用于声明变量的关键字，它们有一些区别：

1. **var**:

   - 在旧版 JavaScript 中是声明变量的唯一方式。
   - 它是函数作用域的，而不是块级作用域。这意味着变量在声明它们的函数内部是可见的，而不管它们是在哪里声明的。如果在函数外部声明的变量，它们会成为全局变量。
   - 通过 `var` 声明的变量可以被多次声明而不会引发错误。

2. **let**:

   - 是 ES6（ECMAScript 2015）引入的新特性，用于声明块级作用域的变量。
   - `let` 声明的变量只在其声明的块或子块中可用，并且不会被提升到块的顶部。
   - 不能重复声明同一个变量。

3. **const**:

   - 也是 ES6 引入的，用于声明常量，其值在声明后不能再被修改。
   - 声明的变量也是块级作用域的。
   - 必须在声明时进行初始化，并且尝试重新分配常量会引发错误。

### 作用域

块级作用域和函数作用域是 JavaScript 中的两种作用域类型，它们决定了变量的可见性和生命周期。

1. 块级作用域
   - 在块级作用域中声明的变量只在当前块（由 `{}` 包围的代码段）中可见。
   - 块级作用域通常与 `let` 和 `const` 一起使用，因为它们会创建块级作用域的变量。
   - ES6 引入了块级作用域的概念，之前 JavaScript 中只有函数作用域。
   - 例如，在 `if` 语句、`for` 循环、`while` 循环、`switch` 语句等代码块内声明的变量只在该代码块内部可见。

```
{
    let x = 10; // 在块级作用域内声明的变量
    console.log(x); // 输出 10
}
console.log(x); // ReferenceError: x is not defined，因为 x 只在块级作用域内可见
```

1. 函数作用域
   - 在函数作用域中声明的变量只在函数内部可见。
   - 在 JavaScript 中，`var` 关键字声明的变量具有函数作用域，而不是块级作用域。
   - 在函数内部声明的变量会被提升到函数的顶部（变量提升）。
   - 例如，在函数内部声明的变量可以在整个函数范围内使用，而不管它们是在函数中的哪个位置声明的。

```
function myFunction() {
    var y = 20; // 在函数作用域内声明的变量
    console.log(y); // 输出 20
}

myFunction();
console.log(y); // ReferenceError: y is not defined，因为 y 只在函数作用域内可见
```

总的来说，块级作用域使得 JavaScript 中的作用域规则更加清晰和灵活，可以更好地控制变量的可见性和生命周期。

## 跨域问题的解决

要解决这个问题，可以采取以下措施：

1. **使用 HTTP 服务器**：不要直接打开 HTML 文件，而是通过 HTTP 服务器访问它。您可以使用本地服务器软件，如 Apache、Nginx 或 PHP 的内置服务器。
2. **修改浏览器设置**：对于开发目的，您可以在浏览器中禁用 CORS 策略，但这并不推荐，因为它会引入安全风险，并且不应该在生产环境中使用。
3. **配置服务器的 CORS 设置**：如果您控制服务器，可以配置服务器以允许来自特定来源的跨源请求。这通常涉及到设置 HTTP 响应头 `Access-Control-Allow-Origin`。
4. **使用代理服务器**：如果您的前端和后端在不同的域上运行，您可以使用代理服务器来绕过 CORS 限制。
5. **后端设置 CORS 头部**：如果您的后端服务器支持 CORS，您可以在服务器的响应中设置适当的 CORS 头部，以允许前端应用进行跨域请求。

## 排查错误

### 命名方式

小驼峰法命名，getElementById 不是 getElementByid

## 运行环境

### [nodejs官方文档](https://nodejs.org/docs/latest/api/documentation.html)

|                                               | python       | javascript   |
| --------------------------------------------- | ------------ | ------------ |
| 脚本                                          | py脚本       | js脚本       |
| 运行环境                                      | python解释器 | nodejs解释器 |
| 包管理器（使用npm可以安装nodejs运行时的依赖） | pip          | npm          |
| 版本管理器（使用nvm可以安装不同版本的npm）    | conda        | nvm          |

#### nodejs包

##### [core-js](https://github.com/zloirock/core-js/tree/master)

core-js是node-js的底层包之一，几乎所有的网站都会或多或少使用它

##### [wiki.js](https://zhuanlan.zhihu.com/p/455020805?utm_psn=1772890047756402688)

帮助写wiki以及发布的工具

##### [jsdom](https://github.com/jsdom/jsdom)

jsdom 是许多 Web 标准的纯 JavaScript 实现，特别是 WHATWG DOM 和 HTML 标准，用于Node.js。一般来说，该项目的目标是模拟足够多的 Web 浏览器子集，以便用于测试和抓取真实世界的 Web 应用程序。

##### vue.js

[一些vue的好用的组件](https://www.zhihu.com/question/504009271/answer/3374441308?utm_psn=1771049127276851200)

[尤雨溪自述维护vue感触](https://www.zhihu.com/question/36292298?utm_psn=1771067488010493952)

##### [leaflet](https://www.zhihu.com/pin/1770509062184140800?native=1&scene=share&utm_psn=1770712848286924800)

最流行 js 映射库之—-leaflet | Leaflet 仅仅用重约 39KB 的 JS，实现了大多数开发者所需要的所有地图功能。它能够在桌面和移动端上高效地工作，并且能够通过大量的插件进行扩展，而且其源代码非常简单易读。有创建地图需要的可以考虑一下该 js 库。	

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
##########################################################.0%
Computing checksum with sha256sum
Checksums matched!
Now using node v22.0.0 (npm v10.5.1)
Creating default alias: default -> node (-> v22.0.0)

```



js逆向
======

问题
----

关于JS逆向马蜂窝网站的问题，可以从多个角度进行罗列，以便在课堂上进行深入探讨。以下是一些可能的问题：

### 一、基础与背景问题

1. 马蜂窝网站采用JS逆向技术的目的是什么？
   - 提问目的：了解JS逆向技术在网站防护中的应用背景。
2. 马蜂窝网站的JS逆向主要影响哪些类型的用户或行为？
   - 提问目的：探讨JS逆向对普通用户、爬虫开发者及数据分析师等群体的影响。

### 二、技术实现问题

1. 马蜂窝网站是如何通过JS逆向技术生成加密的Cookie的？
   - 提问目的：深入了解Cookie加密的具体实现过程，包括加密算法、密钥管理等。
2. 在马蜂窝网站的JS逆向过程中，为什么需要进行多次请求（如三次请求）才能成功获取数据？
   - 提问目的：探讨多次请求背后的技术逻辑和防护机制。
3. 如何识别和分析马蜂窝网站中用于生成Cookie的JS代码？
   - 提问目的：教授如何使用工具（如Fiddler、Charles等）和技巧来定位和解析JS代码。
4. 马蜂窝网站中的JS代码是否使用了混淆技术？这对逆向分析有何影响？
   - 提问目的：讨论混淆技术的目的、类型及其对逆向分析难度的影响。

### 三、应对与解决方案

1. 面对马蜂窝网站的JS逆向防护，爬虫开发者有哪些应对策略？
   - 提问目的：探讨爬虫开发者如何通过模拟浏览器行为、解析JS代码等方式绕过防护机制。
2. 如何有效地调试和分析马蜂窝网站中的JS代码，以便逆向获取所需数据？
   - 提问目的：教授调试技巧，如设置断点、观察变量变化等，以及如何利用开发者工具进行高效分析。
3. 是否存在通用的工具或库可以简化马蜂窝网站JS逆向的过程？
   - 提问目的：探讨现有工具或库在JS逆向中的应用及其局限性。

### 四、安全与伦理问题

1. 马蜂窝网站采用JS逆向技术是否存在安全风险？如何评估这些风险？
   - 提问目的：讨论JS逆向技术可能带来的安全风险，如数据泄露、DDoS攻击等，并探讨评估风险的方法。
2. 在进行马蜂窝网站JS逆向分析时，如何确保行为符合法律法规和伦理规范？
   - 提问目的：强调在逆向分析过程中遵守法律法规和伦理规范的重要性，并探讨如何确保合规性。

这些问题涵盖了马蜂窝网站JS逆向技术的多个方面，旨在引导学生深入理解该技术的工作原理、应用场景、挑战及解决方案。通过这些问题，学生可以更好地掌握JS逆向技术的相关知识，并在实践中加以应用。



模拟请求，如果有就直接提取

没有，

1. 添加请求头
2. 没有，并且数据返回一串数字或者字母形式，通过js密钥加密
3. 请求头加密

pyexecjs



