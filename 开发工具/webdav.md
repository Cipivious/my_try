# 共享网络配置

## 问题描述

我想要在电脑上编辑我的服务器上面的文件，但是总是出现问题，我目前想到了一种新的方式，就是我可以直接利用 ssh 连接远程的服务器，然后使用 emacs 来进行编辑即可。

## 具体的实现步骤

1. 我先尝试了用 vscode 的远程连接的功能，发觉并不方便
2. 于是我觉得还是直接使用命令行的工具比较方便
3. 首先要在本地生成 ssh 的 isa.pub 然后赋值到服务器的.ssh 下面的一个文件
4. 之后创建一个包含下面内容的文件（比如 server.bat）

   ```bat
   @echo off
   REM 设置服务器的 IP 地址和用户名
   set SERVER_IP=47.93.85.206
   set USERNAME=root
   set SSH_KEY_PATH=C:\Users\Administrator\.ssh\id_rsa

   REM 使用 SSH 密钥连接服务器，并保持连接
   ssh -i %SSH_KEY_PATH% -o ServerAliveInterval=60 %USERNAME%@%SERVER_IP%

   REM 保持窗口打开
   pause
   ```

5. 然后可以创建一个快捷方式移动到桌面即可
6. 我的服务器里面有 emacs，可以直接用 emacs 来便捷的修改文件
