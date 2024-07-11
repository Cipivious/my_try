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