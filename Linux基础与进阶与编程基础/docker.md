docker
======

安装
----

[Windows Docker 安装](https://www.runoob.com/docker/windows-docker-install.html)

docker是依赖linux内核运行的，在Windows上安装docker本质上需要安装一个linux内核，大概需要500MB空间，也可以接受。

加载镜像
--------

`docker pull scrapinghub/splash` 的本质是从 Docker 的公共镜像仓库（Docker Hub）拉取一个名为 `scrapinghub/splash` 的 Docker 镜像。这个镜像包含了 Splash 服务器的预配置环境，使你可以轻松地在本地或服务器上运行 Splash 而无需手动配置环境。

具体步骤如下：

1. **发送请求到 Docker Hub**: 当你运行 `docker pull scrapinghub/splash` 时，Docker 客户端会向 Docker Hub 发送请求，询问是否有名为 `scrapinghub/splash` 的镜像。
2. **下载镜像**: 如果这个镜像存在，Docker Hub 会返回镜像的详细信息，并将镜像的各个层（layers）逐一下载到本地。每个镜像层都是一些文件和元数据，构成了镜像的不同部分。
3. **存储在本地**: 下载完成后，Docker 客户端会将这些层组合在一起，形成完整的镜像，并将其存储在本地的 Docker 镜像库中。
4. **运行镜像**: 你可以使用 `docker run` 命令来创建并运行一个基于这个镜像的容器，从而启动 Splash 服务器。

例如：

```
docker run -p 8050:8050 scrapinghub/splash
```

这条命令会运行 Splash 容器，并将宿主机的 8050 端口映射到容器的 8050 端口，使你可以通过 `http://localhost:8050` 访问 Splash 服务。

