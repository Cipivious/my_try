# C

## stack的一种实现

```c
typedef struct element_ {
    struct element_ *next;
    struct element_ *prev;
    int data;
} element;

typedef struct stack_ {
    element *tail;
    int len;
} stack;

void stack_init(stack* stack) {
    stack->tail = NULL;
    stack->len = 0;
    return;
}

void stack_push(stack* stack, int data) {
    if(stack->len == 0) {
        stack->tail = (element*)malloc(sizeof(element));
        stack->tail->data = data;
        stack->tail->next = NULL;
        stack->tail->prev = NULL;
        stack->len++;
        return;
    }
    element* new_elem = (element*)malloc(sizeof(element));
    new_elem->data = data;
    new_elem->next = NULL;
    new_elem->prev = stack->tail;
    stack->tail->next = new_elem;
    stack->tail = new_elem;
    stack->len++;
    return;
}

void stack_pop(stack* stack) {
    if(stack->len == 0) {
        return;
    }
    element* to_free = stack->tail;
    stack->tail = stack->tail->prev;
    if(stack->tail) {
        stack->tail->next = NULL;
    }
    free(to_free);
    stack->len--;
    return;
}

void print_stack(stack* stack) {
    element* current = stack->tail;
    printf("Stack (len=%d): ", stack->len);
    while (current) {
        printf("%d ", current->data);
        current = current->prev;
    }
    printf("\n");
}
```



## [Glib](https://gitlab.gnome.org/GNOME/glib/)

### 介绍

GLib is the low-level core library that forms the basis for projects such as GTK and GNOME. It provides data structure handling for C, portability wrappers, and interfaces for such runtime functionality as an event loop, threads, dynamic loading, and an object system.

The official download locations are: https://download.gnome.org/sources/glib

The official web site is: https://www.gtk.org/

### Installation

See the file ‘[INSTALL.md]()’. There is [separate and more in-depth documentation]() for building GLib on Windows.

#### 路径

```bash
pkg-config --cflags glib-2.0
pkg-config --libs glib-2.0
-I/usr/local/include/glib-2.0 -I/usr/local/lib/x86_64-linux-gnu/glib-2.0/include 
-L/usr/local/lib/x86_64-linux-gnu -lglib-2.0 
```



### Supported versions

Upstream GLib only supports the most recent stable release series, the previous stable release series, and the current development release series. All older versions are not supported upstream and may contain bugs, some of which may be exploitable security vulnerabilities.

See [SECURITY.md]() for more details.

### Documentation

API documentation is available online for GLib for the:

- [GLib](https://docs.gtk.org/glib/)
- [GObject](https://docs.gtk.org/gobject/)
- [GModule](https://docs.gtk.org/gmodule/)
- [GIO](https://docs.gtk.org/gio/)

### Discussion

If you have a question about how to use GLib, seek help on [GNOME’s Discourse instance](https://discourse.gnome.org/tags/glib). Alternatively, ask a question on [StackOverflow and tag it `glib`](https://stackoverflow.com/questions/tagged/glib).

### Reporting bugs

Bugs should be [reported to the GNOME issue tracking system](https://gitlab.gnome.org/GNOME/glib/issues/new). You will need to create an account for yourself. You may also submit bugs by e-mail (without an account) by e-mailing [incoming+gnome-glib-658-issue-@gitlab.gnome.org](mailto:incoming+gnome-glib-658-issue-@gitlab.gnome.org), but this will give you a degraded experience.

Bugs are for reporting problems in GLib itself, not for asking questions about how to use it. To ask questions, use one of our [discussion forums](#discussion).

In bug reports please include:

- Information about your system. For instance:
  - What operating system and version
  - For Linux, what version of the C library
  - And anything else you think is relevant.
- How to reproduce the bug.
  - If you can reproduce it with one of the test programs that are built in the `tests/` subdirectory, that will be most convenient.  Otherwise, please include a short test program that exhibits the behavior. As a last resort, you can also provide a pointer to a larger piece of software that can be downloaded.
- If the bug was a crash, the exact text that was printed out when the crash occurred.
- Further information such as stack traces may be useful, but is not necessary.

### Contributing to GLib

Please follow the [contribution guide]() to know how to start contributing to GLib.

Patches should be [submitted as merge requests](https://gitlab.gnome.org/GNOME/glib/-/merge_requests/new) to gitlab.gnome.org. If the patch fixes an existing issue, please refer to the issue in your commit message with the following notation (for issue 123):

```plaintext
Closes: #123
```

Otherwise, create a new merge request that introduces the change. Filing a separate issue is not required.

## c语言库安装

### libatomic-ops-dev

## struct dirent

```c
struct dirent {
               ino_t          d_ino;       /* Inode number ：An inode number (or simply inode) is a unique identifier for a file or a directory within a filesystem on Unix-like operating systems, such as Linux. Each inode contains metadata about the file or directory it represents, but not the actual data or name.*/
               off_t          d_off;       /* Not an offset; see below ：This field is intended to represent an offset within the directory. However, in some systems, it might not represent an actual byte offset. Instead, it can be used by the readdir implementation to keep track of the directory position.*/
               unsigned short d_reclen;    /* Length of this record ：This field indicates the length of this directory entry record. It’s the number of bytes that make up this particular struct dirent entry. This is important when reading directory entries because it tells you how much memory to move to get to the next entry.*/
               unsigned char  d_type;      /* Type of file; not supported by all filesystem types ：This field indicates the type of the file. Not all filesystems support this field, so it might be zero on those that don't. When supported, it can provide information about the type of file the directory entry refers to,  */
               char           d_name[256]; /* Null-terminated filename */
           };
```

## 以_n结尾的目的

The purpose of the `_n` macro is to provide a consistent, readable way to refer to function names in logging and error messages. This can be particularly useful in larger codebases where tracking errors and debugging requires clear and consistent messages.

Using such conventions helps developers quickly identify which system call or function caused an error, improving the maintainability and debuggability of the code.

这段C代码定义了一个内联（inline）函数，名为`ngx_write_fd`，该函数用于向一个文件描述符（file descriptor, 简称 `fd`）写入数据。让我们一步步地解析这个定义：

## 特殊c语言函数定义结构

```c
static ngx_inline ssize_t
ngx_write_fd(ngx_fd_t fd, void *buf, size_t n)
{
    return write(fd, buf, n);
}
```



1. **`static`**:

   - 这是一个存储类说明符，表示这个函数只在这个源文件（或称为编译单元）中可见，即它是私有的，不能被其他源文件直接访问。

2. **`ngx_inline`**:

   - 这通常是一个宏定义，用于建议编译器将此函数内联。内联函数是在调用它的地方直接插入其代码的函数，而不是像常规函数调用那样进行跳转。这可以减少函数调用的开销，但会增加生成的代码大小。注意，`inline`只是建议，编译器可以选择忽略它。
   - `ngx_inline`可能是在某个头文件中定义的，类似这样：

   ```c
   #ifndef NGX_INLINE  
   #define NGX_INLINE static inline  
   #endif
   ```

   但具体定义可能会因库或项目而异。

3. **函数返回类型 `ssize_t`**:

   - `ssize_t` 是一个有符号整数类型，通常用于表示可能为正或负的字节大小。在POSIX系统中，`write` 函数就使用这种类型作为返回类型。

4. **函数名和参数**:

   - `ngx_write_fd` 是函数的名称。
   - 它接受三个参数：
     - `ngx_fd_t fd`: 这是一个文件描述符类型（可能是一个`typedef`为整数的类型）。文件描述符是一个用于指代文件、套接字、管道等对象的非负整数。
     - `void *buf`: 这是一个指向要写入数据的缓冲区的指针。由于它是`void`指针，所以它可以指向任何类型的数据。
     - `size_t n`: 表示要写入的数据的字节数。`size_t`是一个无符号整数类型，通常用于表示对象的大小。

5. **函数体**:

   - 函数体只包含一个表达式：`return write(fd, buf, n);`。这调用了POSIX的`write`系统调用来实际将数据写入文件描述符。`write`函数将返回实际写入的字节数（在成功时）或-1（在失败时）。

总之，`ngx_write_fd`函数是一个简单的封装，用于调用POSIX的`write`系统调用，但添加了`static`和`inline`属性，并可能使用了特定的类型别名（如`ngx_fd_t`）。

## memcpy

```c
SYNOPSIS
       #include <string.h>
       void *memcpy(void dest[restrict .n], const void src[restrict .n],
                    size_t n);
DESCRIPTION
       The  memcpy()  function  copies n bytes from memory area src to memory area dest.  The memory areas must not overlap.  Use memmove(3) if the memory areas do overlap.

RETURN VALUE
       The memcpy() function returns a pointer to dest.
```

## mkdir

```c
SYNOPSIS
       #include <sys/stat.h>

       int mkdir(const char *pathname, mode_t mode);

       #include <fcntl.h>           /* Definition of AT_* constants */
       #include <sys/stat.h>

       int mkdirat(int dirfd, const char *pathname, mode_t mode);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       mkdirat():
           Since glibc 2.10:
               _POSIX_C_SOURCE >= 200809L
           Before glibc 2.10:
               _ATFILE_SOURCE

DESCRIPTION
       mkdir() attempts to create a directory named pathname.
       The  argument mode specifies the mode for the new directory (see inode(7)).  It is modified by the process's umask in the usual way: in the absence
       of a default ACL, the mode of the created directory is (mode & ~umask & 0777).  Whether other mode bits are honored for the created  directory  de‐
       pends on the operating system.  For Linux, see NOTES below.

       The  newly  created directory will be owned by the effective user ID of the process.  If the directory containing the file has the set-group-ID bit
       set, or if the filesystem is mounted with BSD group semantics (mount -o bsdgroups or, synonymously mount -o grpid), the new directory will  inherit
       the group ownership from its parent; otherwise it will be owned by the effective group ID of the process.

       If the parent directory has the set-group-ID bit set, then so will the newly created directory.

   mkdirat()
       The mkdirat() system call operates in exactly the same way as mkdir(), except for the differences described here.

       If  the  pathname  given in pathname is relative, then it is interpreted relative to the directory referred to by the file descriptor dirfd (rather
       than relative to the current working directory of the calling process, as is done by mkdir() for a relative pathname).

       If pathname is relative and dirfd is the special value AT_FDCWD, then pathname is interpreted relative to the  current  working  directory  of  the
       calling process (like mkdir()).

       If pathname is absolute, then dirfd is ignored.

       See openat(2) for an explanation of the need for mkdirat().

RETURN VALUE
       mkdir() and mkdirat() return zero on success.  On error, -1 is returned and errno is set to indicate the error.
```



## shadow buffer

在编程和特别是图形编程中，"shadow buffer" 或 "shadow copy" 的概念通常用于表示一个数据的备份或副本，这个备份或副本与原始数据保持同步，但在某些操作或计算中可能被用作中间状态，以避免直接修改原始数据。

当你提到“如果此缓冲区是另一个缓冲区的影子（shadow），则指向另一个缓冲区”时，这通常意味着在某种数据结构或对象中，除了包含缓冲区自身的数据外，还有一个指针或引用指向该缓冲区的原始或主缓冲区。

## context

在编程和计算机科学领域，`ctx` 通常是 `context` 的缩写。`context` 在这个领域里指的是一个操作或进程的上下文环境，它包含了该操作或进程所需的所有状态信息。

## alloc, calloc, palloc

1. **alloc**：
   - `alloc` 函数是标准的 C 语言中的内存分配函数，通常是指 `malloc` 函数或者其类似函数（如 `realloc`）。
   - `alloc` 函数用于分配指定大小的内存块，并返回指向该内存块的指针。
   - 在 Nginx 中，`alloc` 可能用于分配大块内存，例如从操作系统层面分配的内存，而不是从 Nginx 内存池中分配。
2. **calloc**：
   - `calloc` 函数也是标准的 C 语言中的内存分配函数，用于分配指定数量和大小的内存块，并初始化为零。
   - 与 `alloc` 函数不同，`calloc` 函数会将分配的内存块的内容初始化为零，而 `alloc` 函数不会进行初始化操作。
   - 在 Nginx 中，`calloc` 通常不直接使用，因为 Nginx 内存池的分配函数并不提供类似 `calloc` 的初始化功能。
3. **palloc**：(即 pool alloc, 从内存池中分配内存)
   - `palloc` 函数是 Nginx 内存池中的内存分配函数，用于从内存池中分配指定大小的内存块。
   - 与标准的 C 语言中的 `malloc` 函数不同，`palloc` 函数是针对 Nginx 内存池设计的，它从预分配的内存池中分配内存，提高了内存分配的效率。
   - `palloc` 函数会从内存池中分配内存，并返回指向该内存块的指针。

## 对齐操作

```c
#define ngx_align_ptr(p, a) \
    (unsigned char *) (((uintptr_t) (p) + ((uintptr_t) a - 1)) & ~((uintptr_t) a - 1))
```

```mathematica
f[n_, a_] := (n + a - 1) - Mod[(n + a - 1), a];
```

以上两种表达的本质上是等价的，他们都可以求大于p的对小的是a的倍数的数。

## `#if 0`

在 C 语言中，使用 `#if 0` 是一种常见的预处理技巧，用于条件性地忽略代码块。虽然被忽略的代码不会被编译和执行，但这种做法在实际开发中有其具体的目的和好处。以下是一些常见原因：

### 临时禁用代码

有时候，开发人员需要临时禁用某段代码进行调试或测试，而不想永久删除该代码。使用 `#if 0` 可以方便地做到这一点，并且稍后可以轻松恢复。

```c
#if 0
// 这段代码暂时不需要，但可能以后会用到
static void *ngx_get_cached_block(size_t size) {
    // 函数实现
}
#endif
```

### 保留参考代码

开发人员可能在重构或优化代码时，保留旧版本的代码以便参考。这样做可以确保在出现问题时，可以快速回滚或对比新旧实现。

```c
#if 0
// 旧的实现方式
static void *ngx_get_cached_block(size_t size) {
    // 旧的函数实现
}
#endif

// 新的实现方式
static void *ngx_get_cached_block(size_t size) {
    // 新的函数实现
}
```

### 文档注释或示例代码

在源代码中保留示例代码或注释，帮助其他开发人员理解某些功能的实现方式或用法。这些代码片段不需要被编译。

```c
// 示例代码，展示如何实现缓存块获取
#if 0
static void *ngx_get_cached_block(size_t size) {
    // 示例函数实现
}
#endif
```

## `char` 和 `u_char` 的区别

1. **基本类型**：
   - `char` 是标准的 C 语言字符类型，表示一个字节，可以是有符号（signed）或者无符号（unsigned）。
   - `u_char` 是 Nginx 代码中定义的一个无符号字符类型，相当于 `unsigned char`。
2. **符号性**：
   - `char` 默认是有符号的，范围是 -128 到 127（在大多数实现中）。
   - `unsigned char` 的范围是 0 到 255。Nginx 使用 `u_char` 作为 `unsigned char` 的别名，确保字符总是无符号的。
3. **使用场景**：
   - `char` 一般用于表示普通字符串、文本数据和字符。
   - `u_char` 通常用于表示二进制数据、缓冲区以及需要明确表示为无符号字符的情况。

## ngx_null_command

在 Nginx 中，配置指令的数组通常以一个 `ngx_null_command` 结尾，这是一种惯用的设计模式。让我们详细解释一下为什么需要这个 `ngx_null_command`，以及如果没有它会发生什么。

### 作用

`ngx_null_command` 的主要作用是标记配置指令数组的结束。它类似于 C 字符串中的空字符（`'\0'`），用于表示数组的终止。

### 定义

通常，`ngx_null_command` 被定义为一个全零的 `ngx_command_t` 结构体。例如：

```c
#define ngx_null_command { ngx_null_string, 0, NULL, 0, 0, NULL }
```

其中，`ngx_null_string` 是一个全零的 `ngx_str_t` 结构体：

```c
#define ngx_null_string { 0, NULL }
```

## socket

```c
struct sockaddr_in {
           sa_family_t     sin_family;     /* AF_INET */
           in_port_t       sin_port;       /* Port number */
           struct in_addr  sin_addr;       /* IPv4 address */
       };
```



### 常见的地址族

`sin_family` 字段指定了套接字的地址族（Address Family），用于指明套接字使用的通信协议。`sa_family_t` 类型通常是一个无符号的短整型，代表不同的地址族。在 `sockaddr` 结构体中，它也是 `sa_family_t` 类型。常用的地址族包括但不限于以下几种：

1. **AF_INET**:
   - **说明**: IPv4 协议
   - **用途**: 用于 IPv4 网络通信。
   - **示例**: `sin_family = AF_INET;`
2. **AF_INET6**:
   - **说明**: IPv6 协议
   - **用途**: 用于 IPv6 网络通信。
   - **示例**: `sin_family = AF_INET6;`
3. **AF_UNIX (或 AF_LOCAL)**:
   - **说明**: Unix 域套接字
   - **用途**: 用于同一主机上的进程间通信。
   - **示例**: `sin_family = AF_UNIX;`
4. **AF_NETLINK**:
   - **说明**: Netlink
   - **用途**: 用于在内核与用户空间之间传递消息。
   - **示例**: `sin_family = AF_NETLINK;`
5. **AF_PACKET**:
   - **说明**: 原始套接字
   - **用途**: 允许用户通过链路层接口直接访问数据链路层。
   - **示例**: `sin_family = AF_PACKET;`
6. **AF_X25**:
   - **说明**: X.25 协议
   - **用途**: 用于 X.25 协议网络通信。
   - **示例**: `sin_family = AF_X25;`
7. **AF_AX25**:
   - **说明**: AX.25 协议
   - **用途**: 用于业余无线电包络协议。
   - **示例**: `sin_family = AF_AX25;`
8. **AF_IPX**:
   - **说明**: IPX 协议
   - **用途**: 用于 IPX/SPX 网络协议。
   - **示例**: `sin_family = AF_IPX;`
9. **AF_BLUETOOTH**:
   - **说明**: Bluetooth 协议
   - **用途**: 用于蓝牙设备通信。
   - **示例**: `sin_family = AF_BLUETOOTH;`

### 端口

`in_port_t` 是一个数据类型，用于存储端口号。端口号在网络通信中用于标识主机上不同的服务或应用程序。`sin_port` 是 `struct sockaddr_in` 结构体中的一个字段，用于指定端口号。

#### 详细解释 `in_port_t sin_port`

- 类型

  ```
  in_port_t
  ```

  - `in_port_t` 是一个定义在 `<netinet/in.h>` 头文件中的类型，通常为 16 位无符号整数，用于表示端口号。

- 字段名

  ```
  sin_port
  ```

  - `sin_port` 是 `sockaddr_in` 结构体中的一个字段，表示网络通信的端口号。

#### 端口号和网络字节顺序

端口号在网络通信中需要使用网络字节顺序（大端字节序）。这意味着最重要的字节存储在最低的内存地址处。这与大多数主机使用的小端字节序不同。

为了确保端口号以网络字节顺序存储，通常使用 `htons` 函数将主机字节顺序的端口号转换为网络字节顺序。`htons` 代表 "host to network short"，它将 16 位的主机字节顺序转换为网络字节顺序。

### htons

`htons()` 是一个用于网络编程的函数，其功能是将主机字节顺序（host byte order）中的无符号短整型整数（通常是 16 位）转换为网络字节顺序（network byte order）。这个函数在网络编程中非常重要，因为不同计算机体系结构可能使用不同的字节顺序，而网络协议通常使用统一的网络字节顺序（大端字节序）。

计算机系统通常使用两种字节顺序中的一种：

- **小端字节序 (Little-endian)**: 低序字节存储在低位地址，高序字节存储在高位地址。大多数 x86 架构的计算机使用小端字节序。
- **大端字节序 (Big-endian)**: 高序字节存储在低位地址，低序字节存储在高位地址。网络协议（如 TCP/IP）规定数据在网络上传输时应使用大端字节序。

## http服务器示例

### 代码

```c
//http-server-super
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define PORT 8080
#define MAXLINE 1024

void handle_connection(int connfd) {
    char buffer[MAXLINE];
    char method[16], path[256], version[16];
    char response[MAXLINE];
    char filepath[512];
    int fd;
    ssize_t n;

    // 读取客户端发送的数据
    n = read(connfd, buffer, MAXLINE - 1);
    if (n < 0) {
        perror("Read failed");
        close(connfd);
        return;
    }
    buffer[n] = '\0';

    // 解析请求行（假设是 GET 请求）
    sscanf(buffer, "%s %s %s", method, path, version);
    printf("Request: %s %s %s\n", method, path, version);
    printf("Client request:\n%s\n", buffer);
    // 构建文件路径
    snprintf(filepath, sizeof(filepath), "/data%s", path);

    // 处理根路径情况
    if (strcmp(path, "/") == 0) {
        snprintf(filepath, sizeof(filepath), "/data/index.html");
    }

    // 打开文件
    fd = open(filepath, O_RDONLY);
    if (fd < 0) {
        // 文件不存在，返回 404 Not Found
        snprintf(response, sizeof(response),
                 "HTTP/1.1 404 Not Found\r\n"
                 "Content-Type: text/html\r\n\r\n"
                 "<html><body><h1>404 Not Found</h1></body></html>\r\n");
        write(connfd, response, strlen(response));
    } else {
        // 读取文件内容并发送响应
        snprintf(response, sizeof(response),
                 "HTTP/1.1 200 OK\r\n"
                 "Content-Type: text/html\r\n\r\n");
        write(connfd, response, strlen(response));

        while ((n = read(fd, buffer, sizeof(buffer))) > 0) {
            write(connfd, buffer, n);
        }
        close(fd);
    }

    close(connfd);
}

int main() {
    int listenfd, connfd;
    struct sockaddr_in servaddr, cliaddr;
    socklen_t clilen;

    // 创建监听套接字
    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    if (listenfd < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // 清零 servaddr 结构体
    memset(&servaddr, 0, sizeof(servaddr));

    // 设置地址族为 IPv4
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);

    // 绑定地址和端口
    if (bind(listenfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // 开始监听连接
    if (listen(listenfd, 5) < 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port %d...\n", PORT);

    while (1) {
        clilen = sizeof(cliaddr);
        // 接受客户端连接
        connfd = accept(listenfd, (struct sockaddr *)&cliaddr, &clilen);
        if (connfd < 0) {
            perror("Accept failed");
            exit(EXIT_FAILURE);
        }

        printf("Client connected: %s:%d\n", inet_ntoa(cliaddr.sin_addr), ntohs(cliaddr.sin_port));

        // 处理连接
        handle_connection(connfd);
    }

    return 0;
}
```

### 思路

![思维导图](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240601191314096.png)

## 进程调度

### c语言版本

```c
/**********************************************************************************************************************************************************************************/
/* 这个是使用C语言实现调用其他进程的方法，以下是思路：
   首先用popen("ps","w")打开进程buffer，
   然后向buffer中写入命令，
   再刷新buffer执行命令，
   然后从缓冲区读出输出的结果。                                              */
/**********************************************************************************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    char buffer[1024];

    // 打开Wolfram Kernel内核进程
    fp = popen("wolfram", "w");

    if (fp == NULL) {
        printf("Error: Failed to open Wolfram Kernel process.\n");
        return 1;
    }

    // 向Wolfram Kernel发送一条命令
    fprintf(fp, "Print[1 + 1]\n");
    fflush(fp); // 刷新输出缓冲区

    // 从Wolfram Kernel读取输出
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("Wolfram Kernel Output: %s", buffer);
    }

    // 关闭Wolfram Kernel进程
    pclose(fp);

    return 0;
}
```

### python版本

```py
import subprocess

# 启动 Wolfram Kernel 进程
process = subprocess.Popen(["wolfram"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 发送命令并获取输出
command = "f[n_] := n^3;  f /@ Range[10]\n"
process.stdin.write(command)
output, error = process.communicate()

print("Output:", output)
if error != '':
    print("Error:", error.strip())

# 关闭进程
process.stdin.close()
process.stdout.close()
process.stderr.close()
```

### lisp版本

```lisp
(defun run-wolfram ()
  "Run Wolfram Kernel in a new buffer."
  (interactive)
  (let ((wolfram-buffer (get-buffer-create "*Wolfram Kernel*")))
    (pop-to-buffer-same-window wolfram-buffer)
    (unless (comint-check-proc wolfram-buffer)
      (let ((wolfram-process
             (make-comint-in-buffer "Wolfram Kernel" wolfram-buffer "wolfram" nil)))
        (set-process-query-on-exit-flag (get-buffer-process wolfram-buffer) nil)
        (accept-process-output (get-buffer-process wolfram-buffer) 1)))))

(defun send-wolfram-code (code)
  "Send Wolfram CODE to Wolfram Kernel."
  (let ((wolfram-buffer (get-buffer "*Wolfram Kernel*")))
    (when wolfram-buffer
      (with-current-buffer wolfram-buffer
        (comint-send-string (get-buffer-process wolfram-buffer) code)
        (comint-send-string (get-buffer-process wolfram-buffer) "\n"))))
```

## sdl2

```c
//这个代码利用SDL实现，它实现的功能是从命令行输入参数，然后会在图形窗口动态显示，当数据超过一定的值的时候，会把之前的内容顶掉，始终显示最新的结果。
#include <stdio.h>
#include <SDL2/SDL.h>
#include "time.h"
#include <stdlib.h>
#define WIDTH 800
#define HEIGHT 600
#define QUEUE_SIZE 10 // 队列的最大容量

double queue[QUEUE_SIZE];
int tag = 0; // 队头索引
int rear = 0; // 队尾索引（初始化为-1表示队列为空）

void drawGraph(SDL_Renderer *renderer, double points[], int count) {
  double y_scale = HEIGHT / 10.0;

  SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE);
  SDL_RenderClear(renderer);

  SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);

  if (tag == 0) {
    for (int i = 0; i<rear; ++i)
      {
        double x = (double)i * WIDTH / count;
        double y = HEIGHT - points[i] * y_scale;
        double x1 = (double)(i+1) * WIDTH / count;
        double y1 = HEIGHT - points[(i + 1) % QUEUE_SIZE] * y_scale;
        SDL_RenderDrawLine(renderer, (int)x, (int)y,(int)x1,(int)y1);

      }
  } else {
    int i, j;
    for (i = rear, j = 0; j < QUEUE_SIZE - 1;j++, i = (i + 1) % QUEUE_SIZE) {
      double x = (double)j * WIDTH / count;
      double y = HEIGHT - points[i] * y_scale;
      double x1 = (double)(j+1) * WIDTH / count;
      double y1 = HEIGHT - points[(i + 1) % QUEUE_SIZE] * y_scale;
      SDL_RenderDrawLine(renderer, (int)x, (int)y,(int)x1,(int)y1);

    }
    j = 9;
    double x = (double)j * WIDTH / count;
    double y = HEIGHT - points[i] * y_scale;
    double x1 = (double)(j+1) * WIDTH / count;
    double y1 = HEIGHT - points[(i) % QUEUE_SIZE] * y_scale;
    SDL_RenderDrawLine(renderer, (int)x, (int)y,(int)x1,(int)y1);

  }

  SDL_RenderPresent(renderer);
}


// 添加元素到队列末尾
void enqueue(int value) {
  if (rear == 9) {
    tag++;
  }
  queue[rear] = value; // 在队尾添加新元素
  rear = (rear + 1) % QUEUE_SIZE; // 更新队尾索引
}

// 显示队列内容
void displayQueue() {
  if (tag == 0) {
    printf("Queue: ");
    for (int i = 0; i<rear; ++i)
      {
        printf("%f ", queue[i]);
      }
    printf("\n");
  } else {
    printf("Queue: ");
    int j;
    for (int i = rear, j = 0; j < QUEUE_SIZE;j++, i = (i + 1) % QUEUE_SIZE) {
      printf("%f ", queue[i]);
    }
    printf("\n");
  }
}

int main() {
  if (SDL_Init(SDL_INIT_VIDEO) != 0) {
    printf("SDL_Init Error: %s\n", SDL_GetError());
    return 1;
  }

  SDL_Window *win = SDL_CreateWindow("y = x^3", 100, 100, WIDTH, HEIGHT, SDL_WINDOW_SHOWN);
  if (win == NULL) {
    printf("SDL_CreateWindow Error: %s\n", SDL_GetError());
    SDL_Quit();
    return 1;
  }

  SDL_Renderer *renderer = SDL_CreateRenderer(win, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
  if (renderer == NULL) {
    SDL_DestroyWindow(win);
    printf("SDL_CreateRenderer Error: %s\n", SDL_GetError());
    SDL_Quit();
    return 1;
  }
  /* int count = 10; */
  /* double points[count]; */
  /* srand(time(NULL)); */

  /* for (int i = 0; i < count ; i++) { */
  /*     points[i] = rand() % 10;  // 生成 0 到 999 的随机数 */
  /* } */
  double value;

  // 主循环接收用户输入
  while (1) {
    printf("Enter a number (or 'q' to quit): ");
    if (scanf("%lf", &value) != 1) {
      // 输入的不是数字，可能是'q'或其他字符
      char c;
      if (scanf("%c", &c) == 1 && c == 'q') {
        break; // 如果是'q'，则退出循环
      }
      // 清除输入缓冲区中的无效输入
      while (getchar() != '\n');
      continue; // 继续下一次循环
    }

    enqueue(value); // 将数字添加到队列中
    displayQueue(); // 显示当前队列内容
    drawGraph(renderer, queue, QUEUE_SIZE);
  }



  SDL_Event e;
  int quit = 0;
  while (!quit) {
    while (SDL_PollEvent(&e)) {
      if (e.type == SDL_QUIT) {
        quit = 1;
      }
    }
  }

  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(win);
  SDL_Quit();

  return 0;
}
```

## qmake

`qmake` 是一个由 Qt 提供的工具，用于生成项目文件（通常是 `.pro` 文件），这些文件描述了如何构建和编译 Qt 程序。它是 Qt 的一部分，主要用于帮助开发者管理项目的构建过程。

### 主要功能包括：

1. **项目文件生成**：
   - `qmake` 通过读取 `.pro` 文件生成相应的 Makefile 或其他构建系统的描述文件，使得项目可以在不同的操作系统和编译环境中构建。

2. **跨平台支持**：
   - Qt 本身是跨平台的，`qmake` 也支持跨平台的项目构建。开发者可以使用相同的 `.pro` 文件在不同的操作系统上进行构建，而不需要为每个平台编写不同的构建脚本。

3. **模块化和扩展性**：
   - `qmake` 支持模块化的项目描述，允许开发者声明不同的模块、依赖项和构建规则。它还支持自定义函数和变量，使得开发者可以根据需要定制构建过程。

4. **集成开发环境（IDE）支持**：
   - 许多集成开发环境（如 Qt Creator）集成了 `qmake`，使得开发者可以在 GUI 中创建和管理 `.pro` 文件，并通过简单的操作完成项目的构建和调试。

5. **简化的语法**：
   - `.pro` 文件使用简洁的语法描述项目的目录结构、文件依赖关系和编译选项，使得开发者可以更专注于项目的逻辑开发而不是构建细节。

总之，`qmake` 是 Qt 开发中一个重要的工具，它通过简化和自动化项目的构建过程，提高了开发效率，并支持跨平台的应用程序开发和部署。

