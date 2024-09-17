scrapy
======

创建的基本步骤
--------------

好的，以下是创建 Scrapy 爬虫的基本步骤：

### 1. 创建 Scrapy 项目

首先，在终端或命令行中导航到你想创建 Scrapy 项目的目录，并运行以下命令来创建一个新的 Scrapy 项目：

```bash
scrapy startproject myproject
```

这将在当前目录下创建一个名为 `myproject` 的目录结构。

### 2. 生成爬虫

接下来，导航到项目目录并生成一个新的爬虫。例如，如果你要爬取 `example.com` 网站，可以运行：

```bash
cd myproject
scrapy genspider example example.com
```

这将在 `spiders` 目录下创建一个名为 `example.py` 的文件。

### 3. 编辑爬虫

打开 `example.py` 文件并编辑爬虫代码。例如：

```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com']

    def parse(self, response):
        self.log(f"Title: {response.xpath('//title/text()').get()}")
        # 在这里添加更多解析逻辑
```

### 4. 配置 Scrapy-Splash (可选)

如果你需要处理 JavaScript 渲染页面，需要配置 Scrapy-Splash。确保在 `settings.py` 文件中添加以下配置：

```python
SPLASH_URL = 'http://localhost:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
```

并在爬虫中使用 `SplashRequest`：

```python
from scrapy_splash import SplashRequest

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        self.log(f"Title: {response.xpath('//title/text()').get()}")
        # 在这里添加更多解析逻辑
```

### 5. 运行爬虫

在项目根目录下运行以下命令来启动爬虫：

```bash
scrapy crawl example
```

### 总结

以下是创建 Scrapy 爬虫的步骤总结：

1. **创建 Scrapy 项目**：`scrapy startproject myproject`
2. **生成爬虫**：`scrapy genspider example example.com`
3. **编辑爬虫**：在 `spiders` 目录下的爬虫文件中编写解析逻辑
4. **配置 Scrapy-Splash (可选)**：在 `settings.py` 中添加相关配置
5. **运行爬虫**：`scrapy crawl example`

这应该可以帮助你创建和运行一个基本的 Scrapy 爬虫。如果有更多具体需求或问题，随时告诉我。

scrapy-selenium
---------------

[scrapy-selenium](https://github.com/clemfromspace/scrapy-selenium)

在scrapy中使用selenium中间件

[scrapy-selenium-grid](https://github.com/dozymoe/scrapy-selenium-grid)

这个使用grid来做大规模的爬虫，安装也比较方便

[这个是一个集成度更高的工具，可以直接设置浏览器打开的数量](https://github.com/kingronjan/scrapy_ajax_utils)，[这一篇是它的设计思路](https://www.cnblogs.com/kingron/p/13702291.html)