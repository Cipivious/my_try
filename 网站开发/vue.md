# vue

[官方教程](https://cn.vuejs.org/tutorial/#step-2)

[官方文档](https://cn.vuejs.org/guide/introduction.html#api-styles)

[babeljs](https://babeljs.io/docs/learn)

[Vue3开发实战经验](https://www.zhihu.com/question/461860114/answer/3198958961?utm_psn=1776191174413750274)

## 新建一个vue项目

![新建一个vue项目](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240518101052956.png)

## npm使用

### 基本指令

1. **npm install**: 安装依赖包，可以使用 `npm install package_name` 安装特定包，或者 `npm install` 安装 package.json 文件中指定的所有依赖项。
2. **npm uninstall**: 卸载已安装的包，可以使用 `npm uninstall package_name` 卸载特定包。
3. **npm update**: 更新依赖包，可以使用 `npm update package_name` 更新特定包，或者 `npm update` 更新 package.json 文件中的所有依赖项。
4. **npm init**: 初始化新的 npm 项目，创建 package.json 文件。
5. **npm search**: 搜索 npm 上的包，可以使用 `npm search package_name` 搜索特定包。
6. **npm run**: 运行 package.json 文件中指定的脚本命令。
7. **npm version**: 更新项目版本号。
8. **npm publish**: 将包发布到 npm 仓库。
9. **npm link**: 在全局环境中链接本地包进行测试。
10. **npm cache**: 管理 npm 缓存，如清除缓存等操作。
11. npm list:列出当前加载的包。

### package.json

npm需要用到项目里的package.json文件，下面是一个例子

```bash
(base) yang@yang-HP-Pavilion-Laptop-14-dv0xxx:~/code/vue/vue-project$ cat package.json 
{
  "name": "vue-project",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.4.21"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.0.4",
    "vite": "^5.2.8"
  }
}
 #运行npm install 会安装文件中使用的依赖包
 #运行npm run 会执行上面scripts里面对应的内容
 #比如运行npm run dev 会执行vite
 #运行npm run build 会执行vite build
```

## npm和pnpm的异同

`pnpm` 和 `npm` 都是 JavaScript 的包管理器，用于管理和安装 JavaScript 项目的依赖。它们之间的主要异同如下：

**相同点：**

1. **包管理：** 两者都用于安装、管理和卸载 JavaScript 包。
2. **命令行工具：** 都提供了命令行工具，使用户可以在终端中执行各种操作，如安装依赖、运行脚本等。
3. **配置文件：** 都有类似的配置文件，如 `package.json` 或 `pnpmfile.js`，用于配置项目的依赖和脚本。

**不同点：**

1. **依赖管理方式：**

   - **npm：** 默认情况下，`npm` 在项目的 `node_modules` 文件夹中为每个包创建一个软链接，这意味着相同的包在不同的项目中可能会重复下载，占用更多的磁盘空间。

   - **pnpm：** `pnpm` 使用一种称为“硬链接”的技术，将依赖安装到单个全局存储库中，并在项目之间共享它们。这样可以减少重复下载，节省磁盘空间。具体来说，`pnpm` 的全局存储库通常位于用户的主目录下的 `.pnpm-store` 文件夹中。如果你在安装 `pnpm` 时没有指定其他位置，它将会在这里创建。

     当你在一个项目中安装依赖时，`pnpm` 会将这些依赖下载到全局存储库，并在项目的 `node_modules` 文件夹中创建符号链接，指向全局存储库中的相应依赖。这样，多个项目可以共享同一依赖，节省磁盘空间。

2. **性能：**

   - **pnpm：** 由于共享依赖，`pnpm` 在安装和更新依赖时通常比 `npm` 更快。
   - **npm：** `npm` 在管理依赖时可能会较慢，特别是对于大型项目或有大量依赖的项目。

3. **生态系统：**

   - **npm：** `npm` 是 Node.js 社区最常用的包管理器之一，拥有庞大的生态系统和丰富的资源。
   - **pnpm：** 相对而言，`pnpm` 的生态系统相对较小，但正在逐渐增长。

总的来说，`pnpm` 在大多数情况下都是 `npm` 的替代选择，特别是在需要更快的安装和更少磁盘空间占用的情况下。

## npx

`npx` 是 Node.js 提供的一个工具，用于在当前项目的上下文中执行 npm 包。它的作用是在不全局安装包的情况下，临时执行 npm 包中的命令。当你需要执行一个不常用的命令，或者你不想将其添加到项目的依赖中时，可以使用 `npx`。

具体来说，`npx` 会在执行命令时，查找当前目录下的 `node_modules/.bin` 目录，如果该目录下有要执行的命令，就直接执行；如果没有，它会在全局的 npm 包中查找并执行。这样做的好处是可以避免全局安装很多不必要的 npm 包，同时确保在不同的项目中使用不同版本的工具。

## vue-devtools

[Vue DevTools 使用指南 - 如何安装和使用 Vue DevTools 调试 Vue 组件](https://juejin.cn/post/7081703827367264263)

[官方安装相关问题解答](https://devtools.vuejs.org/guide/faq.html)

## 快速入门vue

### 推荐使用CDN的方式

CDN方式引用vue，能够让你对vue有一个整体的把握，如果一开始就陷入到复杂的vue应用模块里，你很可能会无法知道vue到底是什么，以及想要开始最初的实践会很麻烦。如果你这样做，你会惊奇的发现原来vue也只是一个javascript脚本，并没有那么玄之又玄。不过后续如果想要使用vue的单文件组件的语法，可以再深入了解vue的框架。

可以借助 script 标签直接通过 CDN 来使用 Vue：

```
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
```

这里使用了 [unpkg](https://unpkg.com/)，但你也可以使用任何提供 npm 包服务的 CDN，例如 [jsdelivr](https://www.jsdelivr.com/package/npm/vue) 或 [cdnjs](https://cdnjs.com/libraries/vue)。当然，你也可以下载此文件并自行提供服务。

通过 CDN 使用 Vue 时，不涉及“构建步骤”。这使得设置更加简单，并且可以用于增强静态的 HTML 或与后端框架集成。但是，你将无法使用单文件组件 (SFC) 语法。

## vue版本

vue已经推出了三个版本，他们之间的api写法略有区别，开始学的时候可能会遇到加载的vue版本不对，导致加载不出来的情况

```html
//这是一个支持vue2的文件，我最开始的时候加载的是vue3的js脚本，导致运行不出来。
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vue Example</title>
  <!-- 引入 Vue.js 库 -->
  <script src="vue2.js"></script>
</head>
<body>

<div id="app">
  <!-- 在 Vue 实例中绑定数据和事件 -->
  <p>{{ message }}</p>
  <button @click="reverseMessage">Reverse Message</button>
</div>

<script>
// 创建一个 Vue 实例
new Vue({
  el: '#app', // 指定挂载点
  data: {
    message: 'Hello Vue!' // 初始化数据
  },
  methods: {
    // 定义一个方法用于反转消息字符串
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('');
    }
  }
})
</script>

</body>
</html>
```

```html
//这个是vue3的版本，在vue3当中，所有的接口都被整合在了Vue,这个大接口的下面
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vue Example</title>
  <!-- 引入 Vue.js 库 -->
  <script src="vue.global.js"></script>
</head>
<body>

<div id="app">
  <!-- 在 Vue 实例中绑定数据和事件 -->
  <p>{{ message }}</p>
  <button @click="reverseMessage">Reverse Message</button>
</div>

<script>
// 创建一个 Vue 实例
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello Vue!'
    }
  },
  methods: {
    // 定义一个方法用于反转消息字符串
    reverseMessage() {
      this.message = this.message.split('').reverse().join('');
    }
  }
});

// 挂载 Vue 实例到 DOM 元素上
app.mount('#app');
</script>

</body>
</html>
```

## 创建vue应用的两种方法

```html
//其实vue应用的创建方法只有一种，就是Vue.createApp(const aconst)
//在创建好以后就挂载到对应的id上面
<script>
      const AttributeBinding = {
        data() {
          return {
            message: 'You loaded this page on ' + new Date().toLocaleString()
          }
        }
      }
      Vue.createApp(AttributeBinding).mount('#bind-attribute')

      const Counter = Vue.createApp({
        data() {
          return {
            counter: 0
          }
        },
        methods: {
          add() {
            this.counter++;
          }
        }
      });

      Counter.mount('#counter');
    </script>
```

## js定义常量对象

```js
const myObject = {
  data() {
    return {
      counter: 0
    }
  },
  methods: {
    add() {
      this.counter++;
    }
  }
};
在这个示例中：
myObject 是一个常量引用，它指向一个对象，该对象包含两个部分：data 方法和 methods 对象。
data 是一个方法，它返回一个对象，这个对象包含一个键值对 counter: 0。
methods 对象中包含一个方法 add，该方法将 counter 的值加 1。
尽管 myObject 本身是常量，但可以修改它所引用对象的属性和方法。
```

## vue中常见的指令和特性绑定

在 Vue.js 中，有许多指令和特性绑定，用于在模板中实现各种功能。以下是一些常见的 Vue 指令及其用法总结：

### v-bind

`v-bind` 是用于绑定 HTML 属性、class 和 style 的指令。

**语法**:

```html
<!-- 动态属性绑定 -->
<a v-bind:href="url">Link</a>
<!-- 缩写形式 -->
<a :href="url">Link</a>
```

**绑定 class 和 style**:

```html
<!-- 绑定 class -->
<div :class="{ active: isActive }"></div>

<!-- 绑定 style -->
<div :style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```

### v-on

`v-on` 用于监听 DOM 事件。

**语法**:

```html
<!-- 监听事件 -->
<button v-on:click="doSomething">Click me</button>
<!-- 缩写形式 -->
<button @click="doSomething">Click me</button>
```

### v-model

`v-model` 用于双向数据绑定，常用于表单元素。

**语法**:

```html
<!-- 双向绑定 input 框的值 -->
<input v-model="message" placeholder="edit me">

<!-- 用于复选框 -->
<input type="checkbox" v-model="checked">

<!-- 用于单选按钮 -->
<input type="radio" v-model="picked" value="a">
<input type="radio" v-model="picked" value="b">

<!-- 用于选择框 -->
<select v-model="selected">
  <option disabled value="">Please select one</option>
  <option>A</option>
  <option>B</option>
  <option>C</option>
</select>
```

### v-for

`v-for` 用于循环渲染元素列表。

**语法**:

```html
<!-- 遍历数组 -->
<li v-for="item in items" :key="item.id">{{ item.text }}</li>

<!-- 遍历对象 -->
<div v-for="(value, key) in object" :key="key">
  {{ key }}: {{ value }}
</div>

<!-- 遍历带有索引的数组 -->
<li v-for="(item, index) in items" :key="index">{{ item.text }}</li>
```

### v-if, v-else-if, v-else

用于条件渲染。

**语法**:

```html
<!-- 条件渲染 -->
<div v-if="awesome">Vue is awesome!</div>
<div v-else>Oh no 😢</div>

<!-- 结合 v-else-if 和 v-else 使用 -->
<div v-if="type === 'A'">A</div>
<div v-else-if="type === 'B'">B</div>
<div v-else-if="type === 'C'">C</div>
<div v-else>Not A/B/C</div>
```

### v-show

用于切换元素的显示和隐藏。

**语法**:

```html
<div v-show="isVisible">This is visible</div>
```

### v-text

更新元素的 `textContent`。

**语法**:

```html
<span v-text="message"></span>
```

### v-html

更新元素的 `innerHTML`，允许渲染 HTML 内容。

**语法**:

```html
<div v-html="htmlContent"></div>
```

### v-cloak

用于防止闪烁效果，在 Vue 完全编译之后，`v-cloak` 属性将被移除。

**语法**:

```html
<div v-cloak>{{ message }}</div>
```

### v-pre

跳过这个元素和它的子元素的编译过程。用于显示原始的 Mustache 标签。

**语法**:

```html
<span v-pre>{{ this will not be compiled }}</span>
```

### v-once

只渲染元素和组件一次。以后数据变化时不会重新渲染。

**语法**:

```html
<span v-once>{{ message }}</span>
```

### 自定义指令

除了内置指令，你还可以创建自定义指令。

**创建自定义指令**:

```javascript
Vue.directive('focus', {
  inserted: function (el) {
    el.focus()
  }
})
```

**使用自定义指令**:

```html
<input v-focus>
```

这些是 Vue.js 中最常用的一些指令和特性绑定。了解这些指令将帮助你在 Vue.js 开发中更高效地处理模板和数据。

## 特性缩写

v-前缀作为一种视觉提示,用来识别模板中 Vue 特定的 attribute。当你在使用 Vue.js 为现有标签添加动态行为 (dynamic behavior) 时,v- 前缀很有帮助,然而,对于一些频繁用到的指令来说,就会感到使用繁琐。同时,在构建由 Vue 管理所有模板的单页面应用程序 (SPA -single-page application) (opens new window) 时, v- 前缀也变得没那么重要了。因此,Vue 为 v-bind 和 v-on 这两个最常用的指令,提供了特定简写

```
v-vind:herf='urf' <==> :herf='urf'
v-on:click='change' <==> @click='change'
```

## 键名大小写

在 DOM 中使用模板时 (直接在一个 HTML 文件里撰写模板),还需要避免使用大写字符来命名键名,因为浏览器会把 attribute 名全部强制转为小写

## v-if vs v-show

v-if 是“真正”的条件渲染,因为它会确保在切换过程中条件块内的事件监听器和子组件适当地被销毁和重建。v-if 也是惰性的:如果在初始渲染时条件为假,则什么也不做——直到条件第一次变为真时,才会开始渲染条件块。相比之下, v-show 就简单得多——不管初始条件是什么,元素总是会被渲染,并且只是简单地基于CSS 进行切换。一般来说, v-if 有更高的切换开销,而 v-show 有更高的初始渲染开销。因此,如果需要非常频繁地切换,则使用 v-show 较好;如果在运行时条件很少改变,则使用 v-if 较好。

## .parent

`.prevent` 修饰符是 Vue.js 中用于事件处理的一个修饰符，它用于在事件处理程序中阻止事件的默认行为。在这个特定的例子中，`.prevent` 修饰符与 `v-on:submit` 指令一起使用，以防止表单的默认提交行为。

默认情况下，当用户在表单中按下回车键或点击提交按钮时，浏览器会尝试提交表单。表单提交时，页面会重新加载或跳转到指定的 URL，这是浏览器的默认行为。在某些情况下，我们可能希望在提交表单时执行自定义的 JavaScript 逻辑，而不希望页面重新加载或跳转。这时就需要阻止表单的默认提交行为。

`.prevent` 修饰符会告诉 Vue.js 在触发事件时调用事件处理程序，并且在处理程序执行时，使用 JavaScript 的 `event.preventDefault()` 方法来阻止事件的默认行为，即阻止表单提交。

## button

在 HTML 中，`<button>` 元素默认是一个提交按钮，特别是当它位于 `<form>` 元素内时。如果没有指定 `type` 属性，它的默认 `type` 是 `"submit"`。因此，当用户点击这个按钮时，它会触发表单的 `submit` 事件。

## 组件基础

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue Example</title>
    <!-- 引入 Vue.js 库 -->
    <script src="vue.global.js"></script>
  </head>
  <body>
    <div id="components-demo">
      <button-counter></button-counter>
      <button-counter></button-counter>
      <button-counter></button-counter>
    </div>
    <script>
      const app = Vue.createApp({});
      app.component('button-counter', {
        data() {
          return {
            count: 0
          }
        },
        template: `
          <button @click='count++'>
          you clicked me {{count}} times.
          </button>
          `
      });
      app.mount("#components-demo");
    </script>
  </body>
</html>
```

## prop数据传递

```html
//第一种是直接传递 比如直接用title
//第二种是在引用的时候传递
//在props里面的参数也有形式变量的意思，并不一定就是真正的使用的时候的名字
//上面的理解有问题，其实props里面绑定的名字一定是要用的，可以通过v-bind来进行绑定
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue Example</title>
    <!-- 引入 Vue.js 库 -->
    <script src="vue.global.js"></script>
  </head>
  <body>
 <div id="blog-post-demo" class="demo">
 <blog-post title="My journey with Vue"></blog-post>
 <blog-post title="Blogging with Vue"></blog-post>
 <blog-post title="Why Vue is so fun"></blog-post>
 </div>
 <div id="blog-post-demo2" class="demo">
   <blog-post
     v-for="post in posts"
     :key="post.id"
     :title="post.title"
     ></blog-post>
 </div>
 <script>
   const App = {
     data() {
       return {
         posts: [
           {id: 1, title: 'My journey with Vue'},
           {id: 2, title: 'Blogging with Vue'},
           {id: 3, title: 'Why Vue is so fun'}
         ]
       }
     }
   };
   const app2 = Vue.createApp(App);
   app2.component('blog-post', {
     props: ['title'],
     template: `<h4>{{title}}</h4>`
   });
   app2.mount('#blog-post-demo2');

   const app = Vue.createApp({});
   app.component('blog-post', {
     props: ['title'],
     template: `<h4>{{title}}</h4>`
   });
   app.mount('#blog-post-demo');
    </script>
  </body>
</html>
```

## ref响应式引用

`ref` 是 Vue 3 Composition API 中用于创建响应式数据的一个函数。通过使用 `ref`，你可以将基本的数据类型（如字符串、数字、布尔值等）或者对象包装成响应式引用。这意味着，当 `ref` 包装的数据发生变化时，依赖于这些数据的 Vue 组件会自动更新。

## ref 的基本用法

```javascript
import { ref } from 'vue'

export default {
  setup() {
    const counter = ref(0) // 创建一个初始值为 0 的响应式引用

    function increment() {
      counter.value++ // 修改响应式引用的值
    }

    return { counter, increment }
  }
}
```

## 详细解释

1. **创建响应式引用**

```javascript
const counter = ref(0)
```

- `ref` 函数接受一个参数，作为其初始值。这里 `counter` 的初始值是 `0`。
- `counter` 是一个响应式引用对象，它有一个 `.value` 属性来存储实际值。这个 `.value` 属性是响应式的，当它改变时，所有依赖于它的组件都会重新渲染。

2. **修改响应式引用的值**

```javascript
counter.value++
```

- 通过修改 `counter.value`，可以更新响应式引用的值。
- 当 `counter.value` 发生变化时，依赖于 `counter` 的模板会自动更新。

3. **在模板中使用**

```html
<template>
  <div>
    <p>{{ counter }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    const counter = ref(0)

    function increment() {
      counter.value++
    }

    return { counter, increment }
  }
}
</script>
```

- 在模板中可以直接使用 `counter`，Vue 会自动解包 `.value` 属性并进行渲染。

## 为什么需要 ref

在 Vue 3 中，响应式系统是基于 `Proxy` 实现的。对于对象类型的数据，Vue 3 可以直接使用 `reactive` 函数使其响应式。然而，对于基本类型的数据（如字符串、数字、布尔值等），需要使用 `ref` 函数来创建响应式引用。这是因为 `Proxy` 无法直接代理基本类型的数据。

## ref 的更多用法

### 响应式数组和对象

尽管 `ref` 通常用于基本类型，但它也可以用于复杂类型：

```javascript
const state = ref({
  count: 0,
  items: []
})
```

### 深度响应式

对于复杂对象，如果需要深度响应式，可以结合 `reactive` 使用：

```javascript
import { ref, reactive } from 'vue'

const state = reactive({
  user: ref({ name: 'John', age: 30 }),
  settings: {
    theme: 'dark',
    notifications: ref(true)
  }
})
```

### 响应式函数

在 Vue 3 中，响应式函数是指当其依赖的响应式数据改变时，会自动更新的函数。`ref` 和 `reactive` 都是响应式函数的一部分，它们让你能够轻松地创建和管理响应式数据。

### 综合示例

```html
<template>
  <div>
    <p>Counter: {{ counter }}</p>
    <button @click="increment">Increment</button>
    <p>Message: {{ message }}</p>
    <button @click="updateMessage">Update Message</button>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    const counter = ref(0)
    const message = ref('Hello, Vue 3!')

    function increment() {
      counter.value++
    }

    function updateMessage() {
      message.value = 'Updated Message!'
    }

    return { counter, increment, message, updateMessage }
  }
}
</script>
```

在这个示例中，我们创建了两个响应式引用 `counter` 和 `message`，并定义了两个方法 `increment` 和 `updateMessage` 来更新它们的值。模板会自动根据引用值的变化进行更新。

## setup与data(),method(),computed()等对应

在 Vue 3 的单文件组件中，`setup` 函数是用来替代 Vue 2 中的 `data`、`methods`、`computed` 等选项的。`setup` 函数接收两个参数：props 和 context。在 `setup` 函数中，你可以返回一个包含响应式数据、方法等的对象，这些数据和方法可以在组件的模板中直接使用。

以下是 `setup` 函数中的一般内容与 Vue 2 中的对应关系：

1. **响应式数据 (data)**：
   在 `setup` 函数中，可以使用 `ref`、`reactive` 等函数创建响应式数据。这些数据将直接暴露给组件的模板。

   ```javascript
   import { ref } from 'vue'
   
   export default {
     setup() {
       // 创建响应式数据
       const count = ref(0)
   
       return {
         count // 暴露给模板
       }
     }
   }
   ```

2. **方法 (methods)**：
   在 `setup` 函数中，可以直接定义方法，并将其返回，从而在组件的模板中使用。

   ```javascript
   export default {
     setup() {
       // 定义方法
       const increment = () => {
         count.value++
       }
   
       return {
         increment // 暴露给模板
       }
     }
   }
   ```

3. **计算属性 (computed)**：
   在 `setup` 函数中，可以使用 `computed` 函数创建计算属性，并将其返回。

   ```javascript
   import { ref, computed } from 'vue'
   
   export default {
     setup() {
       const count = ref(0)
   
       // 创建计算属性
       const doubleCount = computed(() => count.value * 2)
   
       return {
         count,
         doubleCount // 暴露给模板
       }
     }
   }
   ```

4. **生命周期钩子 (lifecycle hooks)**：
   在 `setup` 函数中，可以通过 `onMounted`、`onUpdated`、`onUnmounted` 等函数定义生命周期钩子。

   ```javascript
   import { onMounted } from 'vue'
   
   export default {
     setup() {
       // 在组件挂载后执行
       onMounted(() => {
         console.log('Component mounted')
       })
     }
   }
   ```

需要注意的是，`setup` 函数中返回的对象会直接与模板中的数据、方法进行对应，因此可以直接在模板中使用返回的对象。例如，在模板中使用 `count`、`increment`、`doubleCount` 等变量和方法。

## vue2选项与vue3setup中函数的对应

|          Vue 2 选项          |                  Vue 3 setup 函数中的对应项                  |
| :--------------------------: | :----------------------------------------------------------: |
|            `data`            |           使用 `ref` 或 `reactive` 创建响应式状态            |
|          `methods`           |                 在 setup 函数中直接定义方法                  |
|          `computed`          |               使用 `computed` 函数创建计算属性               |
|           `watch`            |     使用 `watch` 或 `watchEffect` 函数进行响应式数据监听     |
|  `watchEffect` (Vue 3 新增)  | 在 Vue 3 中使用 `watchEffect` 进行自动依赖收集的响应式数据监听 |
| `computed` 的 getter/setter  | 在 Vue 3 中，`computed` 同样支持 getter/setter，但通常使用 `ref` 和 `computed` 结合实现 |
|    `mounted` 生命周期钩子    |     在 setup 函数中，你可以使用 `onMounted` 生命周期钩子     |
|    `updated` 生命周期钩子    |     在 setup 函数中，你可以使用 `onUpdated` 生命周期钩子     |
| `beforeDestroy` 生命周期钩子 |           在 Vue 3 中，使用 `onBeforeUnmount` 替代           |
|   `destroyed` 生命周期钩子   |             在 Vue 3 中，使用 `onUnmounted` 替代             |
|           `props`            | 通过 `props` 选项定义，在 setup 函数中通过 `props` 参数访问  |
|           `emits`            | 通过 `emits` 选项定义，在 setup 函数中通过 `context.emit` 方法触发事件 |
|      `provide`/`inject`      | 在 Vue 3 中，你可以继续在 setup 函数中使用 `provide` 和 `inject` 来进行依赖注入 |
|           `mixins`           | Vue 3 中推荐使用 Composition API 替代 Mixins，但 Mixins 仍然可用 |
|          `filters`           |   Vue 3 移除了 filters，建议使用 methods 或 computed 替代    |
|          自定义指令          | 自定义指令在 Vue 2 和 Vue 3 中的使用方式相似，但需要在 Vue 3 的 setup 函数中使用 `app.directive()` 或 `directive` 选项进行注册 |