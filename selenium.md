selenium
========

安装
----

[参考这个网页](https://github.com/appium/python-client/issues/863)，注意会有一个bug，要安装4.9.0版本的selenium

浏览器
------

要安装浏览器和对应版本的driver，chrome[浏览器下载](https://www.google.com/intl/en_sg/chrome/browser-tools/)，chrome driver[参考这个网页](https://googlechromelabs.github.io/chrome-for-testing/)

[测试脚本](https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/first_script/)
--------

```python 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
time.sleep(5)
driver.quit()

```

启动浏览器的时候加载用户的配置
------------------------------

[我尝试了里面的方法，但是没有成功](https://blog.csdn.net/zhusongziye/article/details/79636567)。

[元素选择](https://juejin.cn/post/6844904002103050254)
------------------------------------------------------

当使用CSS选择器时，我们可以通过多种方法来精确地选择页面上的元素。以下是常见的选择器及其用法总结：

### 1. 基本选择器

- **标签选择器**：根据 HTML 元素的标签名选择元素。
  ```css
  div {}   /* 选择所有 <div> 元素 */
  p {}     /* 选择所有 <p> 元素 */
  ```

- **类选择器**：根据 HTML 元素的类名选择元素。
  ```css
  .class-name {}   /* 选择所有具有 class="class-name" 的元素 */
  ```

- **ID 选择器**：根据 HTML 元素的 ID 属性选择元素（ID 在文档中应该是唯一的）。
  ```css
  #element-id {}   /* 选择具有 id="element-id" 的元素 */
  ```

- **属性选择器**：根据 HTML 元素的属性选择元素。
  ```css
  [attribute-name] {}          /* 选择具有指定属性的元素 */
  [attribute-name="value"] {}  /* 选择具有指定属性和值的元素 */
  ```

### 2. 组合选择器

- **后代选择器**（空格分隔符）：选择所有符合条件的后代元素。
  ```css
  div p {}   /* 选择所有 <div> 元素下的所有 <p> 元素 */
  ```

- **直接子元素选择器**（`>` 符号）：选择直接子元素。
  ```css
  ul > li {}   /* 选择所有 <ul> 元素下的直接子元素 <li> */
  ```

- **相邻兄弟元素选择器**（`+` 符号）：选择紧接在另一个元素后的同级元素。
  ```css
  h1 + p {}   /* 选择紧接在 <h1> 元素后的第一个 <p> 元素 */
  ```

- **通用兄弟元素选择器**（`~` 符号）：选择在同一父元素下的所有同级元素。
  ```css
  h1 ~ p {}   /* 选择所有紧接在 <h1> 元素后的所有 <p> 元素 */
  ```

### 3. 伪类和伪元素选择器

- **伪类选择器**：根据元素的状态或位置选择元素，如链接的状态、鼠标悬停等。
  ```css
  a:hover {}      /* 鼠标悬停在链接上时应用的样式 */
  :nth-child(n) {}/* 选择指定位置的子元素 */
  ```

- **伪元素选择器**：用于向某些选择器添加特殊效果，例如 `::before` 和 `::after`。

### 总结

CSS选择器提供了多种灵活和强大的方法来选择页面上的元素，可以根据元素的结构、属性、状态和位置等特征来精确地定位元素并应用样式。选择器的合理使用不仅能提高代码的可维护性和可读性，还能有效地操作和管理页面上的元素。

格式化python
------------

[在 Visual Studio Code (VSCode) 中自动格式化 Python 代码](https://developer.baidu.com/article/details/2925823)

seleniumIDE
-----------

### [安装](https://chromewebstore.google.com/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd?pli=1)

### [录制操作](https://www.selenium.dev/selenium-ide/docs/en/introduction/getting-started)

### [回放操作](https://www.selenium.dev/selenium-ide/docs/en/introduction/command-line-runner)

下载fnm，再下载npm，node，然后下载selenium-side-runner，最后用·`selenium-side-runner /path/to/your-project.side`来执行录制的操作

fnm
---

#### 安装 Node.js 版本

```
fnm install <version>
```

例如，安装最新的 Node.js 版本：

```
fnm install latest
```

或者安装特定版本：

```
fnm install 14.17.0
```

#### 使用特定版本

```
fnm use <version>
```

例如，使用 14.17.0 版本：

```
fnm use 14.17.0
```

#### 列出已安装的版本

```
fnm list
```

#### 卸载某个版本

```
fnm uninstall <version>
```

#### 设置默认版本

```
fnm default <version>
```

#### 升级 `fnm`

你可以通过重新运行安装脚本来升级 `fnm`：

```
curl -fsSL https://fnm.vercel.app/install | bash
```

小红书爬取
----------

```python
# 要点1 把之前打开的浏览器关掉，程序加载之前的用户配置直接打开浏览器，直接就进入之前的登录状态
# 判断页面是否加载完成，有的时候页面不是同时加载完成的，有多种方法判断页面是否全部加载完成，第一种是等待某个元素加载，第二种是JavaScript的加载状态，第三种是AJAX的请求，结合实际进行选择
# 小红书一些页面使用了动态加载的功能，所以要通过selenium来模拟翻页，然后可以通过页面高度的变化，来判断是否翻到了文件的底部
# csv写入，具体参见代码的74行
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import csv

options = webdriver.ChromeOptions()
options.add_argument(r"--start-maximized")
options.add_experimental_option("detach", True)
options.add_argument(
    r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
)
options.add_argument(r"--profile-directory=Default")

driver = webdriver.Chrome(options=options)

driver.get(
    "https://www.xiaohongshu.com/user/profile/5c568ea2000000001803e7dc?tab=liked&subTab=note"
)

try:
    previous_height = driver.execute_script("return document.body.scrollHeight")
    page_name = 0
    bangs = []
    while True:
        # 等待页面内容加载完成
        WebDriverWait(driver, 100).until(
   		 lambda d: d.execute_script('return document.readyState') == 'complete'
        )

        parent = driver.find_element(
            by=By.XPATH,
            value='//*[@id="userPageContainer"]/div[3]/div/div[3]/div[1]',
        )
        elements = parent.find_elements(by=By.TAG_NAME, value="section")

        for element in elements:
            content = re.split(r"\r?\n", element.text)
            href = element.find_elements(by=By.TAG_NAME, value="a")[1].get_attribute(
                "href"
            )
            content.append(href)
            if content in bangs:
                continue
            bangs.append(content)
            # bangs = bangs.append(content.append(href))

        """ for element in elements:
            if (
                element.get_attribute("href") != ""
                and element.get_attribute("href") not in bangs
            ):
                bangs.append(element.get_attribute("href")) """
        # 获取当前页面的滚动高度
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == previous_height:
            break
        previous_height = new_height
    with open("output.csv", "w", newline="", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        # 写入头部字段
        csvwriter.writerow(["Title", "Author", "Views", "URL"])
        # 写入数据到 CSV 文件
        for row in bangs:
            csvwriter.writerow(row)

finally:
    driver.quit()
```

[微博爬取参阅这个页面](https://blog.csdn.net/poorlytechnology/article/details/109686906)

cookie
------

[作者的思路分成两步，第一步是获取cookie，第二步是利用cookie来进行登录](https://blog.csdn.net/weixin_43821172/article/details/105199481)

### 获取cookie

```python
from selenium import webdriver
import os
import time
import json
 
def browser_initial():
    """"
    进行浏览器初始化
    """
    os.chdir('E:\\pythonwork')
    browser = webdriver.Chrome()
    log_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'
    return log_url,browser
 
def get_cookies(log_url,browser):
    """
    获取cookies保存至本地
    """
    browser.get(log_url)
    time.sleep(15)     # 进行扫码
    dictCookies = browser.get_cookies()    # 获取list的cookies
    jsonCookies = json.dumps(dictCookies) #  转换成字符串保存
    
    with open('damai_cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')
 
if __name__ == "__main__":
    tur = browser_initial()
    get_cookies(tur[0], tur[1])
```

### 利用cookie登录

```python
from selenium import webdriver
import os
import json
 
def browser_initial():
    """"
    浏览器初始化,并打开大麦网购票界面（未登录状态）
    """
    os.chdir('E:\\pythonwork')
    browser = webdriver.Chrome()
    browser.get('https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.8778f91as7xLdc&id=610870234751&clicktitle=2020%E5%BC%A0%E6%9D%B0%E3%80%8C%E6%9C%AA%C2%B7LIVE%E3%80%8D%E5%B7%A1%E5%9B%9E%E6%BC%94%E5%94%B1%E4%BC%9A%20%E5%90%88%E8%82%A5%E7%AB%99')
    return browser
 
def log_damai(browser):
    """
    从本地读取cookies并刷新页面,成为已登录状态
    """
    with open('damai_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
 
    # 往browser里添加cookies
    for cookie in listCookies:
        cookie_dict = {
            'domain': '.damai.cn',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        browser.add_cookie(cookie_dict)
    browser.refresh()                      # 刷新网页,cookies才成功
    
if __name__ == "__main__":
    browser = browser_initial()
    log_damai(browser)
```

[微博爬虫终极版](https://github.com/otonashi-ayana/SpiderWeibo)
---------------------------------------------------------------

这篇文章用request，beautyfly等非常基础的爬虫库，以及MySQL数据库，实现了十万数量级的数据的爬取，我准备深入的研究一下。

selenium grid
-------------

[Selenium Grid快速起步](https://www.selenium.dev/zh-cn/documentation/grid/getting_started/)

Here’s a more complex example of using Selenium Grid with multiple browsers (Chrome and Edge) on a local machine. This script will open both browsers, navigate to a website, perform some actions, and print the page titles.

1. ### **Run the Selenium Grid Hub**:

   ```bash
   java -jar selenium-server-4.22.0.jar hub
   ```

2. ### **Run the Selenium Grid Nodes**:

   ```bash
   java -jar selenium-server-4.22.0.jar node --detect-drivers
   ```

3. ### **Python Script**:

   ```python
   from selenium import webdriver
   from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
   from selenium.webdriver.common.by import By
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   
   # Define the hub URL
   hub_url = "http://localhost:4444"
   
   # Define the capabilities for Chrome
   chrome_capabilities = DesiredCapabilities.CHROME.copy()
   chrome_capabilities['browserName'] = 'chrome'
   
   # Define the capabilities for Edge
   edge_capabilities = DesiredCapabilities.EDGE.copy()
   edge_capabilities['browserName'] = 'MicrosoftEdge'
   
   # Start a remote WebDriver session for Chrome
   chrome_driver = webdriver.Remote(
       command_executor=hub_url,
       desired_capabilities=chrome_capabilities
   )
   
   # Start a remote WebDriver session for Edge
   edge_driver = webdriver.Remote(
       command_executor=hub_url,
       desired_capabilities=edge_capabilities
   )
   
   def test_browser(driver, url):
       driver.get(url)
       WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
       print(f"Title in {driver.capabilities['browserName']}: {driver.title}")
       # Perform additional actions here
       driver.quit()
   
   # Test with Chrome
   test_browser(chrome_driver, "https://www.selenium.dev")
   
   # Test with Edge
   test_browser(edge_driver, "https://www.selenium.dev")
   
   # Test with multiple pages
   def test_multiple_pages(driver, urls):
       for url in urls:
           driver.get(url)
           WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
           print(f"Title in {driver.capabilities['browserName']} at {url}: {driver.title}")
       driver.quit()
   
   urls_to_test = [
       "https://www.selenium.dev",
       "https://www.google.com",
       "https://www.github.com"
   ]
   
   # Test multiple pages with Chrome
   chrome_driver = webdriver.Remote(
       command_executor=hub_url,
       desired_capabilities=chrome_capabilities
   )
   test_multiple_pages(chrome_driver, urls_to_test)
   
   # Test multiple pages with Edge
   edge_driver = webdriver.Remote(
       command_executor=hub_url,
       desired_capabilities=edge_capabilities
   )
   test_multiple_pages(edge_driver, urls_to_test)
   ```

selenium作用
------------

除了爬虫，Selenium 主要用于以下几个方面：

1. **自动化测试**:
   - Selenium 是一种强大的工具，用于自动化 Web 应用程序的测试。它允许测试人员编写脚本来模拟用户行为并验证应用程序的功能是否正常。
   - 支持多种编程语言（如 Java, Python, C# 等），并且可以与各种测试框架（如 JUnit, TestNG, pytest 等）集成。

2. **回归测试**:
   - 在开发过程中，每次更新代码后都需要重新测试应用程序的功能。Selenium 自动化测试可以在每次代码更改后运行，以确保新代码没有破坏现有功能。

3. **持续集成和持续交付（CI/CD）**:
   - Selenium 可以集成到 CI/CD 流程中，如 Jenkins、GitLab CI、Travis CI 等。当代码提交到版本控制系统时，可以自动运行 Selenium 测试，以确保代码质量和应用程序稳定性。

4. **跨浏览器测试**:
   - Selenium 支持在不同的浏览器（如 Chrome、Firefox、Edge 等）上运行测试，确保应用程序在各种浏览器上都能正常工作。

5. **用户行为模拟**:
   - Selenium 可以模拟用户在浏览器上的操作，如点击、输入文本、导航等，这使得它在功能测试和用户体验测试中非常有用。

通过这些应用，Selenium 不仅提高了测试效率，还减少了手动测试的重复性劳动，使开发团队能够更快、更可靠地发布高质量的软件。

无头浏览器
----------

之前有一个应用广泛的无头浏览器“PhantomJS”，后来谷歌也推出了chrome的无头浏览器，它就走向没落了，在selenium中使用无头浏览器添加以下选项。

```python
options.add_argument("--headless")  # 启用无头模式
options.add_argument("--disable-gpu")  # 禁用 GPU 加速
options.add_argument("--window-size=1920,1080")  # 设置窗口大小
```

资源占用情况
------------

具体的资源消耗会根据实际情况和配置有所不同，但可以给出一些一般性的估计值作为参考：

1. **空间消耗**：
   - **Chrome 浏览器本身**：约 200-300 MB 左右（具体取决于版本和安装选项）。
   - **ChromeDriver**：约 10-20 MB 左右。
   - **总体空间消耗**：大约 250-350 MB，考虑到其他系统和驱动的一些额外消耗。
2. **内存消耗**：
   - **Chrome 浏览器**：加载简单网页时大约消耗 200-300 MB 左右的内存。
   - **复杂网页和大量标签页**：内存消耗可能会增加到 1 GB 或更多，特别是加载大量 JavaScript 和动态内容时。
   - **ChromeDriver 和脚本执行**：通常会增加额外的几十到几百 MB 的内存消耗，具体取决于执行的脚本复杂性和频率。
3. **CPU消耗**：
   - **页面加载和渲染**：在页面加载和渲染期间，Chrome 浏览器会占用一定的 CPU 资源，通常在单个核心上使用 10-20% 的情况比较常见。
   - **JavaScript 执行**：执行复杂 JavaScript 脚本时，CPU 使用率可能会显著增加，高峰时可能达到 50-100% 或更高，取决于脚本复杂性和执行频率。

这些数字仅供参考，具体的资源消耗会因服务器的硬件配置、操作系统负载、运行的脚本复杂性等因素而有所不同。建议在实际部署前进行基准测试，以确保服务器能够满足预期的性能要求和资源消耗。
