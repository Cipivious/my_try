# Andriod

## 开启开发者模式

首先到【设置】【关于平板电脑】里，连续点击 5 次【版本号】，可以开启开发者模式。

然后到【系统和更新】【开发人员选项】打开【usb调试】以及 【“仅充电”模式下允许 ADB 调试】

[荣耀平板V7Pro 与华为 matepad paper USB 调试开启教程](https://powersee.github.io/2022/04/usb-debugging-honor-and-huawei/#:~:text=%E9%A6%96%E5%85%88%E5%88%B0%E3%80%90%E8%AE%BE%E7%BD%AE%E3%80%91%E3%80%90%E5%85%B3%E4%BA%8E,%E5%8F%AF%E4%BB%A5%E5%BC%80%E5%90%AF%E5%BC%80%E5%8F%91%E8%80%85%E6%A8%A1%E5%BC%8F%E3%80%82)

## root

国内的手机厂商出于利益等方面考虑，在出场的时候关闭了手机的root权限，而且又加了各种锁来防止用户获取root权限，对于它们的这种行为我是深恶痛绝的。我花了很大的功夫，都没有获得手机的root权限，只好请别人帮我弄的，下面是简单的步骤。[参考教程](https://blog.csdn.net/xuchaoxin1375/article/details/126015726)

1. 解bootloader琐
2. 刷入magisk
3. 制作boot.img
4. 刷入手机

## adb工具

[adb-awesome](https://github.com/mzlogin/awesome-adb)

adb工具是**Android SDK Platform-Tools**的一个重要组成部分，[可以从这里下载adb以及相关的工具](https://developer.android.com/tools/releases/platform-tools?hl=zh-cn#downloads)。

ADB（Android Debug Bridge）是一个强大的命令行工具，允许开发人员与Android设备进行通信和调试。以下是一些常见的ADB命令及其用途：

### 基本命令

#### **连接设备**

   - `adb devices`：列出所有连接的Android设备。
   - `adb connect <设备IP地址>`：通过WiFi连接到设备。

#### **安装与卸载应用**

   - `adb install <路径/应用.apk>`：安装APK文件。
   - `adb uninstall <包名>`：卸载应用。

[出现bug参考这个地方](https://stackoverflow.com/questions/59795600/adb-failure-delete-failed-internal-error)

![image-20240610101413684](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240610101413684.png)

#### **设备信息**

   - `adb shell getprop`：获取设备的所有属性信息。
   - `adb shell getprop ro.product.model`：获取设备型号。
   - `adb shell getprop ro.build.version.release`：获取Android版本。

#### **重启设备**

   - `adb reboot`：重启设备。
   - `adb reboot recovery`：重启设备到恢复模式。
   - `adb reboot bootloader`：重启设备到引导加载程序模式。

#### **文件传输**

   - `adb push <本地路径> <远程路径>`：将文件从本地计算机传输到设备。
   - `adb pull <远程路径> <本地路径>`：将文件从设备传输到本地计算机。

#### **进入设备Shell**

   - `adb shell`：进入设备的命令行接口。

#### **查看日志**

   - `adb logcat`：查看设备的实时日志。
   - `adb logcat -d > log.txt`：保存日志到本地文件。

#### **启动应用**

   - `adb shell am start -n <包名>/<活动名>`：启动指定应用的活动。

#### **强制停止应用**

   - `adb shell am force-stop <包名>`：强制停止指定应用。

#### **清除应用数据**

- `adb shell pm clear <包名>`：清除应用的数据和缓存。

#### **截屏**

    - `adb shell screencap -p /sdcard/screenshot.png`：截取设备屏幕。
        - `adb pull /sdcard/screenshot.png`：将截屏文件传输到本地计算机。

#### **录屏**

    - `adb shell screenrecord /sdcard/demo.mp4`：录制设备屏幕。

#### **端口转发**

    - `adb forward tcp:<本地端口> tcp:<远程端口>`：将本地端口转发到远程端口。

#### **启用TCP/IP调试**

- `adb tcpip 5555`：将ADB服务端口设置为5555。
- `adb connect <设备IP地址>`：通过WiFi连接设备。

这些命令只是ADB工具的一部分，它们可以极大地帮助开发和调试Android应用。你可以使用`adb help`命令来获取更多详细的命令和选项。

## apk文件结构

一旦你解压了APK文件（**zip**），你将能够查看它的内部结构。通常，你会看到以下目录和文件：

- `AndroidManifest.xml`：应用程序的清单文件，包含有关应用程序的基本信息。
- `classes.dex`：包含应用程序的字节码，由Dalvik或ART虚拟机执行。
- `res/`：资源文件夹，包含XML布局文件、图片和其他资源。
- `lib/`：包含本地库文件（.so文件），按架构（如armeabi-v7a, arm64-v8a等）分类。
- `assets/`：原始资产文件。
- `META-INF/`：包含签名信息和清单文件。

## 应用涉及内容（卸载应用）

在Android设备上删除软件（应用程序）的本质是从设备中移除与该应用程序相关的文件和目录，并更新系统配置以反映应用程序的移除。具体来说，这包括删除应用程序的APK文件、数据目录和缓存目录，以及更新系统配置文件。

### 删除应用程序的步骤

1. **删除应用程序的APK文件**：
   - 对于用户安装的应用程序，APK文件通常位于 `/data/app/` 目录中。
   - 对于系统预装的应用程序，APK文件通常位于 `/system/app/` 或 `/system/priv-app/` 目录中。
2. **删除应用程序的数据和缓存**：
   - 应用程序的数据目录位于 `/data/data/<包名>/`。
   - 应用程序的缓存目录位于 `/data/data/<包名>/cache/`。
3. **更新系统配置文件**：
   - 更新 `/data/system/packages.xml` 文件以移除应用程序的记录。
   - 更新 `/data/system/users/0/package-restrictions.xml` 文件以移除用户应用程序的记录。

## 二进制文件

直接用zip解压apk以后得到的是二进制的AndriodManifest.xml,我想要使用aapt工具把这个二进制转化成正常的文件，但是没有成功。`aapt` （Android Asset Packaging Tool）。`aapt` 可以解析二进制XML文件并将其转换为文本格式。

## apktools

[apktools是一款强大andriod反编译的工具](https://apktool.org/)

[这个是它的一个使用的教程](https://blog.csdn.net/baidu_31156101/article/details/107938641)

## Magisk模块

[模块推荐，来自酷安app](https://www.coolapk.com/feed/37588281?shareKey=ODg1MTNiNjA2N2ZhNjJlMTNkMjY~&shareUid=5097617&shareFrom=com.coolapk.market_12.4)

[android_root后的玩机:magisk模块&root隐藏/lsposed&xposed框架的使用/MIUI小窗多开](https://blog.csdn.net/xuchaoxin1375/article/details/126071341?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22126071341%22%2C%22source%22%3A%22xuchaoxin1375%22%7D&ctrtid=8i2pw)

## apk下载网站

[最全的B站(bilibili)国际版下载都在这个网站了，需要自取](https://www.zeelis.com/t/370.html)

(1)apkpure https://apkpure.com/
(2)apkcombo https://apkcombo.com/
(3)ApkMirro https://www.apkmirror.com/
(4)uptodown https://en.uptodown.com/
(5)androidapksfree https://androidapksfree.com/
(6)apk-dl https://apk-dl.com/