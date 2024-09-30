# emacs

[emacs-china](https://emacs-china.org/)

[emacs-eaf](https://github.com/emacs-eaf/)

[步步为营精通 emacs](https://github.com/AbstProcDo/Master-Emacs-From-Scratch-with-Solid-Procedures)

## mu4e

[mu4e 是一个 emacs 中的邮箱客户端，和 emacs 集成良好，功能十分强大](https://github.com/djcb/mu)

### 安装配置

1. 先按照上面官网的内容安装 mu4e,安装过程中需要自己再安装一些编译需要的依赖和库
2. 写对应的配置文件

   ```lisp
   ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
   ; 这个文件是emacs邮箱，mu4e的配置文件 ;
   ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
   (add-to-list 'load-path "/usr/local/share/emacs/site-lisp/mu4e")
   (require 'mu4e)

   ;; mu4e 基本配置
   (setq mu4e-maildir "~/Maildir")
   (setq mu4e-get-mail-command "mbsync -a")

   ;; 文件夹配置
   (setq mu4e-drafts-folder "/Drafts")
   (setq mu4e-sent-folder   "/Sent Messages")
   (setq mu4e-trash-folder  "/Trash")
   (setq mu4e-refile-folder "/Archive")

   ;; 配置邮件地址和签名
   (setq user-mail-address "myqqhao@qq.com")
   (setq user-full-name "Your Name")
   (setq mu4e-compose-signature "Your Signature")

   ;; SMTP 配置
   (setq message-send-mail-function 'smtpmail-send-it)
   (setq smtpmail-smtp-server "smtp.qq.com")
   (setq smtpmail-smtp-service 587)
   (setq smtpmail-stream-type 'starttls)
   (setq smtpmail-auth-credentials (expand-file-name "~/.authinfo"))

   ;; 设定为html格式显示邮件
   (setq mu4e-view-prefer-html t)

   ;; 设置收件箱
   (setq mu4e-maildir-shortcuts
         '( ("/INBOX" . ?i)
           ("/Sent Messages" . ?s)
           ("/Drafts" . ?d)
           ("/Trash" . ?t)))

   ;; 设置缓存邮件
   (setq mu4e-headers-auto-update t)

   (provide 'init-mu4e)
   ```

3. 启动 mu4e

![image](<https://raw.githubusercontent.com/Cipivious/my_try/main/image/截图> 2024-06-11 19-51-04.png)

### [使用方法](https://junahan.netlify.app/post/emacs-mu4e/)

| 快捷键 | 命令                                     | 说明                                                                    |
| ------ | ---------------------------------------- | ----------------------------------------------------------------------- |
| R      | 回复邮件 (Reply)                         | 用于在 `headers` / `message` view 执行回复邮件动作                      |
| F      | 转发邮件 (Forward)                       |                                                                         |
| C      | 写邮件 (Compose)                         |                                                                         |
| E      | 编辑邮件 (Edit)                          |                                                                         |
| s      | 搜索邮件 (search)                        | 执行 `mu find` 命令搜索邮件                                             |
| j      | 跳转到 maildir (jump-to-maildir)         | 在 `maildir` 之间跳转                                                   |
| b      | 书签搜索 (bookmark-search)               | 为经常使用的搜索配置书签，以快速执行邮件搜索动作                        |
| B      | 修改书签索引 (edit bookmark-search)      |                                                                         |
| .      | 切换显示原始消息视图 (raw view (toggle)) |                                                                         |
| q      | 退出                                     | 可作用于 `main` / `headers` / `messages` / `raw` 等视图用于退出当前视图 |

![img](https://raw.githubusercontent.com/Cipivious/my_try/main/image/view-diagram.png)

## zeal 集成

[zeal-at-point](https://github.com/jinzhu/zeal-at-point)

Search the word at point with Zeal

[Zeal](http://zealdocs.org/) is a simple offline API documentation browser inspired by Dash (OS X app), available for Linux and Windows.

## 设置字体样式

### [cnfonts](https://github.com/tumashu/cnfonts)

cnfonts 原来叫: chinese-fonts-setup, 是一个 Emacs 中英文字体配置工 具。可以比较方便地实现中文字体和英文字体等宽（也就是大家常说的中英 文对齐）。

| 命令                      | 功能         |
| ------------------------- | ------------ |
| cnfonts-edit-profile      | 调整字体设置 |
| cnfonts-increase-fontsize | 增大字号     |
| cnfonts-decrease-fontsize | 减小字号     |

### [快速调整字体大小-Emacs-China](https://emacs-china.org/t/emacs/22135)

## company

### 开始补全的字符数

```lisp
(setq company-minimum-prefix-length 1)
```

### 配置后端

```lisp
;;yasnippet是一个很有用的后端，它可以加载代码块
;;clang是一个一般的补充c的后端
;;company-dabbrev-code 是分析当前所有buffer的内容，从代码的角度
;;company-keyword提供了各种变成语言的关键词，可以自己在里面添加自己需要的编程语言的关键词，也可以禁用一些编程语言的关键词
(setq company-clang-executable "/usr/bin/clang")
(add-hook 'c++-mode-hook
          (lambda ()
            (set (make-local-variable 'company-backends)
                 '((company-clang
                    company-files
                    company-keywords
                    company-yasnippet
                    company-capf
                    company-dabbrev-code
                    company-gtags
                    company-etags
                    company-semantic)
                   (company-dabbrev))))
```

### 自己添加一个 company 的后端

除了 company 以外,corfu 也是一个自动补全的框架。

可以将补全候选词列表单独定义，然后在补全后端中调用。这样可以使代码更清晰，并便于维护和扩展。

1. #### **定义补全候选词列表：**

   ```elisp
   (defvar my-custom-completions
     '("example" "completion" "backend" "custom" "words")
     "List of words for custom completions.")
   ```

2. #### **定义补全后端并调用候选词列表：**

   ```elisp
   (defun my-company-backend (command &optional arg &rest ignored)
     "A simple Company backend for custom word completion."
     (interactive (list 'interactive))
     (cl-case command
       (interactive (company-begin-backend 'my-company-backend))
       (prefix (and (eq major-mode 'text-mode) ;; 在特定模式下启用，如 text-mode
                   (company-grab-word)))
       (candidates
       (cl-remove-if-not
         (lambda (c) (string-prefix-p arg c))
         my-custom-completions))))
   ```

3. #### **添加补全后端到 Company 模式：**

```elisp
(add-to-list 'company-backends 'my-company-backend
```

## emacs 中调用外部命令

在 emacs 中，有很多地方都会集成外部命令，比如在 plantuml-mode 当中使用了外部的 plantuml，在 clang-company 中使用了外部的 clang，mathematica-mode 当中使用了外部的 wolframscript，以下是一个示例。

```lisp
;;这段代码的思路是先在"/tmp"区域创建一个wls文件，然后调用wolframscript来执行这个生成的文件，再将结果返回到名为”*Wolfrm output*“的buffer。
(defun xah-wolfram-eval-region (Xbegin Xend)
  "Eval code in text selection with WolframScript.
Version: 2024-03-21"
  (interactive "r")
  (let ((xcode (buffer-substring-no-properties Xbegin Xend))
        (xrandfilename
         (concat
          (if xah-wolfram-temp-dir-path
              xah-wolfram-temp-dir-path
            temporary-file-directory
            )
          (format "wolfram_%s_%x.wls" (format-time-string "%Y%m%d%-H%M%S") (random #xfffff))))
        (xoutBuf "*Wolfram output*")
        xcmdStr
        )
    (setq xcmdStr (format  "wolframscript -print all -file %s &" xrandfilename))
    (with-temp-file xrandfilename
      (insert xcode))
    (message "Running 「%s」" xcmdStr)
    (shell-command xcmdStr xoutBuf)
    (display-buffer xoutBuf)))
```

## [wolfram-mode](https://github.com/xahlee/xah-wolfram-mode?tab=readme-ov-file)

这是一个在 emacs 中写 mathematica 代码的方法，可以像运行 python 脚本一样，直接在 emacs 里面执行 mathematica 的代码，感觉非常的方便，参考下面的界面。

![mathematica-mode](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240603151049546.png)

## plantuml-mode

在 emacs 中有一个 plantuml-mode，这个模式可以直接预览 plantuml 对应的生成的内容，十分好用。

[plantuml](https://github.com/xuanye/plantuml-style-c4)的一个样式库，但是不好使用。

[这是另外一个样式库，我也没有用成功](https://github.com/bschwarz/puml-themes)

## org-mode

如果使用 org-mode，就不要过于依赖实时预览的功能，我感觉这个不是很好进行配置，我准备暂时放弃这个功能，就单纯的使用它最基本的文本编辑的功能。

## markdown-mode

之前一段时间，我琢磨了很久的 org-mode，但是没有研究明白，后来我又使用了 markdown，借助 typora 的可视化界面让我明白了这种文本标记语言，后来又借助 vscode 让我更加了解和熟练了 markdown 的语法，我觉得二者有很多的共同之处，主要的差于仅在于符号体系，不过现在我已经习惯使用 markdown 了，我也准备全面转向使用 markdown 了，我在 emacs 中也添加了 markdown-mode 来便于使用。

具体可以参考`https://jblevins.org/projects/markdown-mode/`这个网站来进行 markdown 的配置。

## org-roam

[参考手册](https://www.orgroam.com/manual.html)

- `org-roam-node-insert`: creates a node if it does not exist, and inserts a link to the node at point.
- `org-roam-node-find`: creates a node if it does not exist, and visits the node.
- `org-roam-capture`: creates a node if it does not exist, and restores the current window configuration upon completion.

## 内置浏览器

emacs 中内置的浏览器是 eww，这款是纯 html 浏览器，css 和 js 都很难进行设置，[Xwidgets](https://www.gnu.org/software/emacs/manual/html_node/elisp/Xwidgets.html)是一个很好的替代品，它在界面的展示方面，具有更强的优势。

## elisp

```lisp
;;; typora-mode.el --- A minor mode to emulate Typora keybindings for Org-mode

;; 定义键映射
(defvar typora-mode-map (make-sparse-keymap)
  "Keymap for `typora-mode`.")

(defun my-org-insert-heading (level)
  "根据前缀参数 LEVEL 插入相应级别的标题."
  (interactive "p")
  (beginning-of-line)
  (let ((stars-on-line (save-excursion
                         (beginning-of-line)
                         (when (looking-at "^\\*+ ")
                           ;; 匹配行首的 *，并去除空格
                           (match-string 0)))))
    (when stars-on-line
      (delete-region (line-beginning-position) (+ (line-beginning-position) (length stars-on-line)))))
  (insert (make-string level ?*) " ")
  (end-of-line))

;; 插入标题
(define-key typora-mode-map (kbd "C-1") (lambda () (interactive) (my-org-insert-heading 1)))
(define-key typora-mode-map (kbd "C-2") (lambda () (interactive) (my-org-insert-heading 2)))
(define-key typora-mode-map (kbd "C-3") (lambda () (interactive) (my-org-insert-heading 3)))
(define-key typora-mode-map (kbd "C-4") (lambda () (interactive) (my-org-insert-heading 4)))
(define-key typora-mode-map (kbd "C-5") (lambda () (interactive) (my-org-insert-heading 5)))
(define-key typora-mode-map (kbd "C-6") (lambda () (interactive) (my-org-insert-heading 6)))


;; 定义 minor mode
(define-minor-mode typora-mode
  "A minor mode to emulate Typora keybindings for Org-mode."
  :lighter " Typora"
  :keymap typora-mode-map
  :global nil
  (if typora-mode
      (message "typora-mode enabled")
    (message "typora-mode disabled")))

(provide 'typora-mode)
;;; typora-mode.el ends here
```

## org-agenda

### [Org as 地表最强的管理与计划的助手工具](https://emacs-china.org/t/05-org-as/12092)

### 设置 agenda 的文件路径

### 设置 capture 的模板和存储路径

### 定制 agenda 的查看格式

## 代码格式化工具

### python

#### 安装 black

Black 是一个高度可配置的 Python 代码格式化工具，它会自动调整代码的格式，使其符合 PEP 8 标准。你可以使用以下命令安装 Black：

```bash
pip install black
```

#### **使用 `blacken-mode` 集成 Black**

`blacken-mode` 是一个 Emacs 包，可以自动运行 Black 格式化 Python 代码。你可以在 Emacs 中安装 `blacken-mode`，并在编辑 Python 文件时自动运行 Black 来格式化代码。

### c

#### 安装 clangformat

ClangFormat 是由 Clang 提供的一个代码格式化工具，它能够根据预定义的样式或自定义的样式文件自动格式化 C 和 C++ 代码。你可以使用以下命令安装 ClangFormat：

```bash
sudo apt-get install clang-format
```

#### 安装对应插件

在 Emacs 中，你可以使用 `clang-format.el` 这个官方提供的包来与 ClangFormat 集成，类似于 `blacken-mode` 与 Black 的集成。`clang-format.el` 包含了一些函数和命令，可以方便地调用 ClangFormat 来格式化 C 和 C++ 代码。

## flymake 与 flycheck

### 意见

推荐使用 flycheck，flymake 因为年久失修，在使用过程中会存在各式各样的问题无法解决，导致体验的效果很差劲，我使用 flycheck 以后，这些问题就都迎刃而解了，flycheck 只需要配置一下环境当中的语法检查工具就可以了，比如 C 的话可以用 clang 或者 gcc，python 的话可以用 python-compile，python-flake8,python-pylint 等等，js 可以用 eslint，[具体可以参考这里](https://www.flycheck.org/en/latest/languages.html#syntax-checker-python-flake8)，总之这些都比较容易解决，然后就可以直接用了。

![image-20240601102542478](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240601102542478.png)

### flycheck 配置

(setq flycheck-check-syntax-automatically '(mode-enabled save))

## 添加环境中的路径变量

[exec-path-from-shell](https://github.com/purcell/exec-path-from-shell)

A GNU Emacs library to ensure environment variables inside Emacs look the same as in the user's shell.

## 我对 emacs 的需要

1. 语法高亮
2. 代码（块）补全
3. 调整缩进
4. 寻找位置（函数，变量，文件）
5. 保存工作区
6. 代码语法检查
7. 代码格式化工具

## [elpy](https://elpy.readthedocs.io/en/latest/quickstart.html)

elpy 是一个 python 的模式

- `C-c C-c (elpy-shell-send-region-or-buffer)`

  Evaluate the current script (or region if something is selected) in an interactive python shell. The python shell is automatically displayed aside of your script.

- `C-c C-d (elpy-doc)`

  Display documentation for the thing under cursor (function or module). The documentation will pop in a different buffer, that can be closed with q.

- `C-c C-f (elpy-find-file)`

  Find a file in the current project. This uses a search-as-you-type interface for all files under the project root.A prefix argument enables “do what I mean” mode. On an import statement, it will try to open the module imported. Elsewhere in a file, it will look for an associated test or implementation file, and if found, open that. If this fails, either way, it will fall back to the normal find file in project behavior.If the current file is called `foo.py`, then this will search for a `test_foo.py` in the same directory, or in a `test` or `tests` subdirectory. If the current file is already called `test_foo.py`, it will try and find a `foo.py` nearby.This command uses [projectile](https://github.com/bbatsov/projectile) or [find-file-in-project](https://github.com/technomancy/find-file-in-project) under the hood, so you need one of them to be installed.

- **M-. (elpy-goto-definition)**

  Go to the location where the identifier at point is defined. This is not always easy to make out, so the result can be wrong. Also, the backends can not always identify what kind of symbol is at point. Especially after a few indirections, they have basically no hope of guessing right, so they don’t.

- **M-\* (pop-tag-mark)**

  Go back to the last place where M-. was used, effectively turning M-. and M-\* into a forward and backward motion for definition lookups.

## add-hook

```lisp
;;add-hook就是给一定的模式后面添加钩子，执行一定的函数
;;许多的模式启动的时候，一般就是会执行hook后的绑定，比如添加快捷键绑定，启动一定的程序
(defun my-disable-elpy-company-backend ()
  "Disable elpy-company-backend in company-backends."
  (setq company-backends (remove 'elpy-company-backend company-backends)))

(add-hook 'elpy-mode-hook 'my-disable-elpy-company-backend)
```

## 移动光标

在 Emacs 中，如果你想将当前光标所在的行移动到屏幕的中间，你可以使用以下命令：

```txt
M-x recenter
```

或者，你可以使用快捷键 `C-l`，它的默认绑定是 `recenter-top-bottom`。这个命令循环执行三种行为：

1. 将当前行移动到屏幕中央。
2. 将当前行移动到屏幕顶部。
3. 将当前行移动到屏幕底部。

每次按 `C-l` 都会在这三种状态之间循环。

## 使用书签

好的，以下是关于 Emacs 书签功能的总结：

1. **设置书签：** 使用 `C-x r m` 快捷键在当前位置设置一个书签。你需要输入一个书签名称，并确认。

2. **列出所有书签：** 使用 `C-x r l` 快捷键列出当前文件中的所有书签。这将打开一个缓冲区，显示所有书签的列表。

3. **跳转到书签：** 使用 `C-x r b`在列出所有书签的缓冲区中，使用 `RET` 键选择一个书签，然后你将跳转到该书签所在的位置。

4. **删除书签：** 使用 `C-x r d` 快捷键删除当前文件中的书签。Emacs 会提示你选择要删除的书签，并删除选定的书签。

5. **书签标记：** 使用 `M-x bookmark-set` 命令为书签设置标记，以便在列出所有书签时快速定位特定的书签。

6. **保存和加载书签：** Emacs 会在会话结束时自动保存书签。你也可以手动保存和加载书签，使用 `M-x bookmark-save` 和 `M-x bookmark-load` 命令。

通过这些操作，你可以更方便地在文档中标记重要位置，并且快速地在书签之间跳转，提高编辑效率。

## nginx-mode

[nginx-mode](https://github.com/ajc/nginx-mode)

emacs 默认配置中没有编辑 nginx.conf 的模式，这是一个编辑 nginx.conf 的插件，效果还不错。

## 使用 emacs 连接服务器

[参考这篇文档](https://www.gnu.org/software/emacs/manual/html_node/emacs/Remote-Files.html)

```emacs
//其中method可以使用ssh，plink等等
/method:host:filename
/method:user@host:filename
/method:user@host#port:filename
```

## 打字训练

### [speed-type](https://github.com/dakra/speed-type)

speed-type-text 开始打字

customize-group speed-type 设置参数

## gtags

GNU Global（通常简称为 gtags）是一个源代码标签系统，它可以生成一个索引数据库以便于在源代码中进行快速跳转和查找定义。以下是使用 GNU Global 的基本步骤：

1. **安装 GNU Global**：

   首先，你需要安装 GNU Global。你可以在操作系统的包管理器中查找 GNU Global 的安装包。例如，在 Ubuntu 上，你可以使用以下命令安装：

   ```txt
   sudo apt install global
   ```

   或者你也可以从 GNU Global 的官方网站下载源代码并编译安装。

2. **生成标签文件**：

   在你的源代码目录中执行以下命令来生成标签文件：

   ```txt
   gtags
   ```

   这会在当前目录生成一个名为 `GTAGS` 的标签文件以及相关的索引文件。

3. **使用 Emacs 中的 gtags 插件**：

   如果你使用 Emacs，你可以安装并配置 gtags 插件来与 GNU Global 集成。Emacs 的 gtags 插件提供了一组命令和快捷键，可以让你在源代码中进行快速跳转和查找定义。

   你可以按照 gtags 插件的文档说明来配置 Emacs，并学习如何使用 gtags 插件提供的命令来浏览和跳转源代码。

4. **在 Emacs 中使用 GNU Global**：

   一旦在 Emacs 中配置了 gtags 插件，你就可以使用以下命令来进行标签跳转：

   - `M-.`（Meta + .）：跳转到定义处。
   - `M-,`（Meta + ,）：返回上一次跳转的位置。
   - `M-x gtags-find-tag`：手动输入标识符来查找定义。

   通过这些命令，你可以在 Emacs 中方便地浏览和导航源代码，并快速定位到感兴趣的函数或变量的定义位置。

通过这些步骤，你可以使用 GNU Global 来加速在源代码中进行跳转和查找定义的过程。

## 折叠和展开代码块

在 Emacs 中，有多个插件可以用来折叠代码。最通用和流行的插件是 `hs-minor-mode` 和 `outline-minor-mode`。此外，还有一些更强大的折叠插件，比如 `origami-mode` 和 `fold-this`.

### `hs-minor-mode`

`hs-minor-mode` 是 Emacs 自带的折叠插件，支持多种编程语言的代码块折叠。

#### 启用 `hs-minor-mode`

在特定编程模式下启用 `hs-minor-mode`，例如在 `python-mode` 中：

```emacs-lisp
(add-hook 'python-mode-hook 'hs-minor-mode)
```

#### 使用 `hs-minor-mode`

- `C-c @ C-h`: 折叠代码块
- `C-c @ C-s`: 展开代码块
- `C-c @ C-M-h`: 折叠所有代码块
- `C-c @ C-M-s`: 展开所有代码块

你可以通过 `M-x hs-minor-mode` 手动启用或禁用 `hs-minor-mode`.

### `outline-minor-mode`

`outline-minor-mode` 是 Emacs 的另一种内置折叠模式，适用于大纲样式的文本和代码。

#### 启用 `outline-minor-mode`

```emacs-lisp
(add-hook 'prog-mode-hook 'outline-minor-mode)
```

#### 使用 `outline-minor-mode`

- `C-c @ C-t`: 切换折叠/展开
- `C-c @ C-a`: 展开所有内容
- `C-c @ C-l`: 折叠所有内容
- `C-c @ C-c`: 折叠/展开当前节点

### origami-mode`

`origami-mode` 是一个强大的折叠插件，支持多种语言和嵌套折叠。

#### 安装 `origami-mode`

使用 `package.el` 安装：

```emacs-lisp
(unless (package-installed-p 'origami)
  (package-refresh-contents)
  (package-install 'origami))
```

#### 启用 `origami-mode`

```emacs-lisp
(add-hook 'prog-mode-hook 'origami-mode)
```

#### 使用 `origami-mode`

- `C-c C-f o`: 切换折叠/展开
- `C-c C-f c`: 折叠当前节点
- `C-c C-f u`: 展开当前节点
- `C-c C-f r`: 重置所有折叠

### `fold-this`

`fold-this` 是一个简单但功能强大的折叠插件，允许你手动选择折叠区域。

#### 安装 `fold-this`

使用 `package.el` 安装：

```emacs-lisp
(unless (package-installed-p 'fold-this)
  (package-refresh-contents)
  (package-install 'fold-this))
```

#### 使用 `fold-this`

选择一段代码后，调用以下命令进行折叠：

```emacs-lisp
(global-set-key (kbd "C-c C-f f") 'fold-this)
(global-set-key (kbd "C-c C-f u") 'fold-this-unfold-at-point)
(global-set-key (kbd "C-c C-f a") 'fold-this-unfold-all)
```

### 示例配置

以下是一个示例配置，结合 `origami-mode` 和 `fold-this`：

```emacs-lisp
;; 添加 MELPA 源
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

;; 安装 origami 和 fold-this
(unless (package-installed-p 'origami)
  (package-refresh-contents)
  (package-install 'origami))

(unless (package-installed-p 'fold-this)
  (package-refresh-contents)
  (package-install 'fold-this))

;; 启用 origami-mode
(add-hook 'prog-mode-hook 'origami-mode)

;; 设置 fold-this 的快捷键
(global-set-key (kbd "C-c C-f f") 'fold-this)
(global-set-key (kbd "C-c C-f u") 'fold-this-unfold-at-point)
(global-set-key (kbd "C-c C-f a") 'fold-this-unfold-all)
```

通过这些插件，你可以在 Emacs 中轻松折叠和展开代码块，提高代码阅读和编辑的效率。

## sublimity

这是一个类似 sublime 中的侧边的一个插件，当移动坐标的时候，侧边的光标会随着上下移动，能够整体的把握整个文件的脉络，有一定的帮助。

## 使用 emacs 临时执行命令行命令

对于一些简单的操作，比如创建文件（夹），删除文件（夹），显示当前目录，编译可执行代码，执行代码看效果，打开文件，改变文件所有人和权限，显示当前的文件，完全可以直接使用 emacs 中（M-!）（也即 shell-command）的方式来执行，

## 添加和更新包源列表

### 在配置文件中添加下面内容（.emacs.d/init.el）

```lisp
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(add-to-list 'package-archives '("melpa-stable" . "https://stable.melpa.org/packages/") t)
(add-to-list 'package-archives '("gnu" . "https://elpa.gnu.org/packages/") t)
```

### 运行 list-package，然后按“U”，更新包源

## emacs 重复上一次命令

在 Emacs 中，您可以使用 `M-x repeat-complex-command` 或者快捷键 `C-x z` 来重复上一次执行的命令。

1. 使用 `M-x repeat-complex-command`：

   按下 `M-x`，然后键入 `repeat-complex-command` 并按下 `RET`。这将重复上一次执行的命令。

2. 使用快捷键 `C-x z`：

   在执行完一个命令后，按下 `C-x z` 将会重复上一次执行的命令。如果您希望连续多次重复同一个命令，可以按下 `z` 键多次。

## projectile

### 添加一个目录到已知的项目

projectile-add-known-project

### 移除一个已知的项目

projectile-remove-known-project

### 使用正则表达式替换

[原理和规则](https://www.jb51.net/article/281027.htm)

#### 使用下面命令替换

projectile-replace-regex

#### 使用下面进行保存

projectile-save-project-buffers

#### 关闭打开的 buffer

1. **使用 `kill-all-local-buffers` 命令**：
   这个命令将关闭当前窗口中的所有缓冲区，但不会关闭其他窗口中的缓冲区。你可以通过 `M-x kill-all-local-buffers` 来调用它（其中 `M-x` 是按 `Esc` 键然后按 `x` 键）。
2. **使用 `delete-other-windows` 和 `kill-this-buffer`**：
   首先，你可以使用 `C-x 1`（即 `delete-other-windows`）来确保只有一个窗口是活动的。然后，你可以使用 `C-x k`（即 `kill-buffer`）并输入要关闭的缓冲区的名称，或者只按 `C-x k` 并选择当前缓冲区来逐个关闭它们。但这种方法比较繁琐，如果你有很多缓冲区需要关闭的话。

### 命令大全

C-c C-p ESC projectile-project-buffers-other-buffer
C-c C-p ! projectile-run-shell-command-in-root
C-c C-p & projectile-run-async-shell-command-in-root
C-c C-p ? projectile-find-references
C-c C-p C projectile-configure-project
C-c C-p D projectile-dired
C-c C-p E projectile-edit-dir-locals
C-c C-p F projectile-find-file-in-known-projects
C-c C-p I projectile-ibuffer
C-c C-p K projectile-package-project
C-c C-p L projectile-install-project
C-c C-p P projectile-test-project
C-c C-p R projectile-regenerate-tags
C-c C-p S projectile-save-project-buffers
C-c C-p T projectile-find-test-file
C-c C-p V projectile-browse-dirty-projects
C-c C-p a projectile-find-other-file
C-c C-p b projectile-switch-to-buffer
C-c C-p c projectile-compile-project
C-c C-p d projectile-find-dir
C-c C-p e projectile-recentf
C-c C-p f projectile-find-file
C-c C-p g projectile-find-file-dwim
C-c C-p i projectile-invalidate-cache
C-c C-p j projectile-find-tag
C-c C-p k projectile-kill-buffers
C-c C-p l projectile-find-file-in-directory
C-c C-p m projectile-commander
C-c C-p o projectile-multi-occur
C-c C-p p projectile-switch-project
C-c C-p q projectile-switch-open-project
C-c C-p r projectile-replace
C-c C-p t projectile-toggle-between-implementation-and-test
C-c C-p u projectile-run-project
C-c C-p v projectile-vc
C-c C-p z projectile-cache-current-file
C-c C-p left projectile-previous-project-buffer
C-c C-p right projectile-next-project-buffer

C-c C-p x e projectile-run-eshell
C-c C-p x g projectile-run-gdb
C-c C-p x i projectile-run-ielm
C-c C-p x s projectile-run-shell
C-c C-p x t projectile-run-term
C-c C-p x v projectile-run-vterm

**C-c C-p s g** projectile-grep
C-c C-p s r projectile-ripgrep
C-c C-p s s projectile-ag
C-c C-p s x projectile-find-references

C-c C-p 5 D projectile-dired-other-frame
C-c C-p 5 a projectile-find-other-file-other-frame
C-c C-p 5 b projectile-switch-to-buffer-other-frame
C-c C-p 5 d projectile-find-dir-other-frame
C-c C-p 5 f projectile-find-file-other-frame
C-c C-p 5 g projectile-find-file-dwim-other-frame
C-c C-p 5 t projectile-find-implementation-or-test-other-frame

C-c C-p 4 C-o projectile-display-buffer
C-c C-p 4 D projectile-dired-other-window
C-c C-p 4 a projectile-find-other-file-other-window
C-c C-p 4 b projectile-switch-to-buffer-other-window
C-c C-p 4 d projectile-find-dir-other-window
C-c C-p 4 f projectile-find-file-other-window
C-c C-p 4 g projectile-find-file-dwim-other-window
C-c C-p 4 t projectile-find-implementation-or-test-other-window

C-c C-p x 4 v projectile-run-vterm-other-window

## emacs 图片插件

[image+](https://github.com/mhayashi1120/Emacs-imagex?tab=readme-ov-file)

当打开 png 图片的时候,运行下面的命令 M-x
imagex-auto-adjust-mode
然后重新刷新 buffer
revert-buffer

就能看到在窗口内看到大小合适的图片.

如果需要放大缩小, M-x

imagex-global-sticky-mode

然后用下面的快捷键进行缩放等操作
;; _C-c + / C-c -: Zoom in/out image.
;;_ C-c M-m: Adjust image to current frame size.
;; \* C-c C-x C-s: Save current image.

[这也是一个 image 的仓库，用于辅助上面的 iamge+](https://github.com/abo-abo/hydra)

## [eaf](https://github.com/emacs-eaf/emacs-application-framework#install)

让 emacs 成为一个操作系统

![eaf-applications](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240508215126783.png)

![安装成功](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240508222428179.png)

### 安装 gnome-extension

Gnome3 Wayland Native: You need to execute the command `cp -r emacs-application-framework/gnome-shell/eaf-wayland@emacs-eaf.org ~/.local/share/gnome-shell/extensions` and activate the `eaf-wayland@emacs-eaf.org` plugin in `gnome-extensions`
Gnome3 Wayland Native：您需要执行命令 `cp -r emacs-application-framework/gnome-shell/eaf-wayland@emacs-eaf.org ~/.local/share/gnome-shell/extensions` 并激活 `eaf-wayland@emacs-eaf.org` 插件 `gnome-extensions`

### [安装 eaf-markmap](https://github.com/emacs-eaf/eaf-markmap?tab=readme-ov-file)

markmap 是一个思维导图软件，它可以集成到 VS-code,vim,以及 emacs 当中，这个是它的 emacs 版本。[它的官网地址是这个](https://markmap.js.org/repl)。[这个是它 github 仓库的地址](https://github.com/markmap/markmap?tab=readme-ov-file)。

## neotree 插件

### M-x

neotree-toggle 打开或关闭

neotree-dir 制定打开的目录

### 通用操作

- `↑` 和 `↓`：上下移动光标选择文件或目录。
- `RET` 或 `TAB`：打开选定的文件或目录，或者展开/折叠选定的目录。
- `q`：退出 Neotree 文件树。
- `SPC`：在选定的文件或目录上进行标记或取消标记。
- `H`：显示/隐藏帮助菜单。
- `?`：显示 Neotree 的快捷键帮助信息。

## 操作命令

### 执行 init.el eval-buffer

### 执行单行代码 C-x C-e

### 关闭 buffer

在 Emacs 中，您可以使用 `kill-buffer` 函数来关闭一个或多个缓冲区。以下是一种方法：

1. **使用 `ibuffer`**：`ibuffer` 是 Emacs 中用于管理缓冲区的交互式界面。您可以使用 `M-x ibuffer` 命令打开它。
2. **标记要关闭的缓冲区**：在 `ibuffer` 界面中，您可以使用 `m` 键将要关闭的缓冲区标记为需要操作的缓冲区。按下 `m` 键会在缓冲区前面显示一个 `*` 标记。
3. **执行操作**：标记完所有要关闭的缓冲区后，按下 `D` 键执行删除操作，然后按下 `x` 键确认关闭标记的缓冲区。
4.

## 用 emacs 编辑 latex

### [AUCTex](https://www.emacswiki.org/emacs/AUCTeX)

## emacs 自动保存桌面

### 保存桌面打开的 buffer

你可以在 Emacs 启动时添加以下代码来启用 `desktop-save-mode`：

```txt
(desktop-save-mode 1)
```

你可以将这行代码添加到你的 Emacs 配置文件（通常是 `~/.emacs` 或 `~/.emacs.d/init.el`）中。

1. 配置保存会话信息的位置：

你可以配置保存会话信息的位置，例如：

```txt
(setq desktop-dirname "~/.emacs.d/desktop/")
(setq desktop-path (list desktop-dirname))
```

以上代码将会话信息保存到 `~/.emacs.d/desktop/` 目录中。

注意如果没有 desktop 文件夹的话需要先创建一个

### 保存桌面的窗口布局

[perspective](https://github.com/nex3/perspective-el)

The Perspective package provides multiple named workspaces (or "perspectives") in Emacs, similar to multiple desktops in window managers like Awesome and XMonad, and Spaces on the Mac.

### 设置桌面的主题

以下是一些在 GitHub 上备受欢迎的 Emacs 主题：

1. **Doom Emacs**：这是一个非常流行的 Emacs 配置框架，包括许多主题和配色方案，其中包括一些暗色主题。
2. **Spacemacs**：类似于 Doom Emacs，Spacemacs 也是一个 Emacs 配置框架，它提供了一些内置的暗色主题以及一些额外的主题插件。
3. **Solarized**：这是一个受欢迎的配色方案，提供了两个版本：Light 和 Dark。它在许多编辑器中都很受欢迎，包括 Emacs。
4. **Tomorrow Theme**：这是一个现代的配色方案，具有暗色和亮色版本。它有一些变种，适合不同的编程语言和环境。
5. **Dracula**：Dracula 是一个暗色主题，具有清晰的对比度和色彩饱和度，适合长时间的编程工作。

## 用 emacs 读源代码

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

[company-tern 这是一个坑人的玩意，非常麻烦](https://github.com/kevinushey/company-tern?tab=readme-ov-file)

[tern 使用也非常的麻烦](https://github.com/webpack/webpack/issues/15127)

在 emacs 中想配置直接执行 js 非常麻烦，暂时放弃

### [安装 js2-mode](https://github.com/mooz/js2-mode)

### [安装 indium](https://indium.readthedocs.io/en/latest/installation.html)

#### [配置 indium](https://emacs-china.org/t/indium-emacs-javascript/7051)

#### [下载 json-process-client](https://github.com/emacsmirror/json-process-client)

要注意顺序

#### [下载 js2-refactor](https://github.com/js-emacs/js2-refactor.el)

#### [下载 s 包](https://github.com/magnars/s.el)

#### [下载 multiple-cursors](https://github.com/magnars/multiple-cursors.el)

### [安装 Chrome 浏览器](https://support.google.com/chrome/a/answer/9025903?hl=en&ref_topic=9025817&sjid=17686342759721064849-AP)

我反复尝试了好久都没有成功，主要在于我对这个语言掌握的太少，我准备先用替代的方法，之后有机会再安装。

## use emacs to write html

### [常用软件写网页 html,新手用什么软件写 html 网页比较靠谱](https://blog.csdn.net/weixin_31056947/article/details/117853448)

### [用 emacs 写 html 文件](https://blog.csdn.net/paul08colin/article/details/6443266)

p { margin-bottom: 0.21cm; }

C-c C-f : 光标移动到当前所在位置的下一个 HTML 标签。

C-c C-b : 光标移到到当前所在位置的上一个 HTML 标签。

C-c \<left>/\<right> : 跳到该标签的开始/ 结束。

C-c DEL : 删除标签。 C-c 1~6 : 插入标题 h1~h6 。

C-c Enter : 插入段落标记\<p> 。

C-c / ：闭合 b 标签。比如可以结合上一条使用，就会自动插入\</p> 。

C-c C-c h : 插入超级链接标记。

C-c C-c n : 插入 anchor （锚标），便于在文档其他位置跳转到该位置。

需要在 Mini-buffer 中输入锚标名称。

C-c C-c u : 插入无序列表标记\<ul>\<li>\</ul> 。

C-c C-c o : 插入有序列表标记\<ol>\<li>\</ol> 。

C-c C-c l : 插入标记\<li> 。

C-c C-c - : 插入水平线\<hr> 。

C-c C-c i : 插入图像引用标记 \<img> 。

C-c C-j : 插入换行符\<br>

有时需要在 html 文本中显示 html 标记，比如\<p>，不能直接输入。可以这样： C-c C-n < ，然后输入 p ，然后再 C-c C-n >;。其实 C-c C-n 后输入的字符都不会被 html 解析而直接输出了。

c-c c-t 跳过之后的标签 [C-M-j](https://emacs.stackexchange.com/questions/35378/html-mode-insert-tag-without-attributes)

### [使用 emacs 写 html](http://blog.chinaunix.net/uid-7591142-id-112460.html)

### emacs 迈向 xhtml

#### [tidy](http://www.hollenback.net/index.php?EmacsTidy)

#### [nxml-mode](https://www.emacswiki.org/emacs/NxmlModeForXHTML#h5o-1)

#### emacs 修改配置文件

emacs 修改文件过程

1. 使用 C-h k 或者 C-h m 找到函数的定义
2. 更具一个已知的函数反复搜索，找到 map 定义
3. 更改原来的定义，以及 hook 的内容
4. 修改完以后，需要用 M-x byte-compile-file 来重新编译文件（这一步主要针对内置的文件，因为内置的文件经过编译以提高运行速率）

## 模式

### [php-mode](https://github.com/emacs-php/php-mode?tab=readme-ov-file)

原来的包里面没有 php-mode-autoloads.el，不建议直接安装

[推荐下载这个配置，然后从里面找到对应的内容](https://github.com/jstautz/.emacs.d/tree/4482419c653b823da622dedd471876399e77b1f8)

## 关于编辑器的一些议论

### [为什么还有人用 VIM](https://www.zhihu.com/question/547708456/answer/2645630850?utm_psn=1768532068147818497)

### [Excalidraw](https://www.zhihu.com/question/465346075/answer/3091803862?utm_psn=1769031940265664512)

### [专业 Emacs 入门（十）：笔记系统 org-mode](https://zhuanlan.zhihu.com/p/633047823?utm_psn=1769030680720388096)

### [emacs 配置文件参考](https://github.com/cabins/emacs.d)

### [这是一个 linux 的学习笔记，里面包含了很多配置 vim 的实际教程](https://github.com/cubxxw/awesome-cs-course/tree/master/linux)

### [这也是一个介绍 vim 优势的文章](
