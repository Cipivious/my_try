# php

## 学习笔记

### [在命令行使用PHP](https://www.php.net/manual/zh/features.commandline.usage.php)

1. 让 PHP 运行指定文件。

   ```
   $ php my_script.php
   
   $ php -f my_script.php
   ```

   以上两种方法（使用或不使用 **-f** 参数）都能够运行给定的 my_script.php 文件。注意，没有限制可以执行哪种文件， 特别是文件名也不必用 `.php` 作为扩展名。

2. 在命令行中直接传递 PHP 代码执行。

   ```
   $ php -r 'print_r(get_defined_constants());'
   ```

   必须特别注意 shell 变量的替代及引号的使用。

3. 在命令行中交互式的使用PHP

您可以使用 `php -a` 命令来启动 PHP 的交互式 shell。以下是如何使用的步骤：

   1. 打开终端。

   2. 输入以下命令并按下回车键：

      ```
      php -a
      ```

   3. 然后，您会看到 PHP 的提示符 `php >`，表示您已经进入了交互式的 PHP shell。

   4. 您可以在提示符后输入 PHP 代码，并按下回车键执行。例如：

      ```
      php > echo "Hello, world!";
      ```

      这将输出 `Hello, world!`。

   5. 您可以像在常规 PHP 脚本中一样编写和执行 PHP 代码，但是需要注意一些差异，例如在交互式 shell 中，您可以直接执行语句而不需要使用 `<?php` 和 `?>` 标签。

   6. 要退出交互式 shell，您可以输入 `exit` 或者按下 `Ctrl + D`。

   通过这种方式，您可以在命令行中方便地交互式使用 PHP，这对于测试小段代码、调试或者执行简单的任务非常有用。

### 使用php连接数据库

![使用php连接数据库](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240508112757305.png)

### 向数据库中插入数据

```php
$query = "INSERT INTO aliens_abduction (first_name, last_name, when_it_happened, how_long, how_many, alien_description, what_they_did, fang_spotted, other, email) VALUES ('Sally', 'Jones', '3 days ago', '1 day', 'four', 'green with six tentacles', 'We just talked and played with a dog', 'yes', 'I may have seen your dog. connect me.', 'sally@gregs-list.net')";
$result = $conn->query($query) or die ('Error querying database');
```



### html中使用php

#### 启动数据库

`sudo systemctl start mysql`

#### 启动服务器

`sudo systemctl start apache2`

#### 准备php文件

`cp report.php /var/www/html`

#### 改变文件权限和所有者（可选）

`sudo chown yang /var/www/html`

`sudo chmod -R 777 /var/www/html`

#### 准备html文件

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Aliens Abducted Me - Report an Abduction</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h2>Aliens Abducted Me - Report an Abduction</h2>

  <p>Share your story of alien abduction:</p>
  <form method="post" action="http://localhost/report.php">
    <label for="firstname">First name:</label>
    <input type="text" name="firstname" /><br />
    <label for="lastname">Last name:</label>
    <input type="text" name="lastname" /><br />
    <label for="email">What is your email address?</label>
    <input type="text" name="email" /><br />
    <label for="whenithappened">When did it happen?</label>
    <input type="text" name="whenithappened" /><br />
    <label for="howlong">How long were you gone?</label>
    <input type="text" name="howlong" /><br />
    <label for="howmany">How many did you see?</label>
    <input type="text" name="howmany" /><br />
    <label for="aliendescription">Describe them:</label>
    <input type="text" name="aliendescription" size="32" /><br />
    <label for="whattheydid">What did they do to you?</label>
    <input type="text" name="whattheydid" size="32" /><br />
    <label for="fangspotted">Have you seen my dog Fang?</label>
    Yes <input name="fangspotted" type="radio" value="yes" />
    No <input name="fangspotted" type="radio" value="no" /><br />
    <img src="fang.jpg" width="100" height="175"
      alt="My abducted dog Fang." /><br />
    <label for="other">Anything else you want to add?</label>
    <textarea name="other"></textarea><br />
    <input type="submit" value="Report Abduction" name="submit" />
  </form>
</body>
</html>
```

### 使用php发送邮件

```bash
yang@yang-HP-Pavilion-Laptop-14-dv0xxx:~/code/php$ cat email.php
<?php
$to = "jordanwatson186@gmail.com";
$subject = "Test Email";
$message = "This is a test email sent from PHP.";

// Additional headers
// $headers = "From: sender@example.com\r\n";
$headers = "From: 1830574935@qq.com\r\n";
$headers .= "Reply-To: sender@example.com\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

// Send email
if (mail($to, $subject, $message, $headers)) {
    echo "Email sent successfully to $to";
} else {
    echo "Email sending failed";
}
?>
```

### 处理来自数据库的列表内容

```php
  $query = "SELECT * FROM email_list";
  $result = mysqli_query($dbc, $query)
    or die('Error querying database.');

  while ($row = mysqli_fetch_array($result)){
    $to = $row['email'];
    $first_name = $row['first_name'];
    $last_name = $row['last_name'];
    $msg = "Dear $first_name $last_name,\n$text";
    mail($to, $subject, $msg, 'From:' . $from);
    echo 'Email sent to: ' . $to . '<br />';
  }
```

### 使用php上传和删除文件

```php
move_uploaded_file($_FILES['screenshot']['tmp_name'], $target);
//其中target是服务器文件夹的完整的路径，比如/var/www/html/image
//$_FILES是上传的文件
//tmp_name 是上传文件的临时存放路径

@unlink('/var/www/html/' . $image_path . $screenshot);
//这个用于删除服务器上面的文件
```

### 判断语句

```php
if (isset($_POST[id])) {
    //执行命令
}
else if （XXX）{
    //执行命令
}
else {
    //执行命令
}
```

### 循环语句

在PHP中，循环结构用于重复执行相同或类似的代码块。以下是PHP中常见的循环结构及其用法：

1. **for 循环：**

   ```php
   for ($i = 0; $i < 5; $i++) {
       echo "The number is: $i <br>";
   }
   ```

   这段代码将从0开始循环，每次递增1，直到 $i 小于5为止。在每次循环中，输出当前的 $i 值。

2. **foreach 循环：**

   ```php
   $colors = array("Red", "Green", "Blue");
   foreach ($colors as $color) {
       echo "$color <br>";
   }
   ```

   这段代码用于遍历数组 $colors 中的每个元素，并将每个元素的值赋给变量 $color。然后输出每个颜色。

3. **while 循环：**

   ```php
   $i = 0;
   while ($i < 5) {
       echo "The number is: $i <br>";
       $i++;
   }
   ```

   这段代码将在 $i 小于5的条件下重复执行循环体内的代码块，每次循环结束后递增 $i 的值。

4. **do...while 循环：**

   ```php
   $i = 0;
   do {
       echo "The number is: $i <br>";
       $i++;
   } while ($i < 5);
   ```

   这段代码首先执行循环体内的代码块，然后检查循环条件。只要条件为真，就会重复执行循环体，直到条件为假为止。

这些是PHP中常见的循环结构及其用法。它们可以根据具体的需求来选择使用哪种循环结构。

### php中的数据结构

下面是一个完整的总结，包括 PHP 中常见的数组和其他数据结构的使用方法（从本质上来说，下面的php其实只是一种结构，有一个数组的名称，然后是里面的元素，每个元素都由元素的索引（也可以说是元素的名称），以及元素的值构成的，可以参考下面的图片，至于队列和栈只是特殊操作而已，并不特别。）：

![参考图片](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240515202027666.png)

1. **数组（Array）：** 数组是一种用于存储多个值的数据结构，可以通过数字索引或关联索引访问。

   - 数字索引数组：

     ```php
     $numbers = array(1, 2, 3, 4, 5);
     echo $numbers[0]; // 输出 1
     ```

   - 关联索引数组：

     ```php
     $person = array("name" => "John", "age" => 30, "city" => "New York");
     echo $person["name"]; // 输出 John
     ```

2. **多维数组（Multidimensional Array）：** 多维数组是一种包含一个或多个数组作为元素的数组。

   ```php
   $students = array(
       array("name" => "John", "age" => 20),
       array("name" => "Alice", "age" => 22),
       array("name" => "Bob", "age" => 21)
   );
   echo $students[0]["name"]; // 输出 John
   ```

3. **列表（List）：** 列表是一种只包含数字索引的数组。

   ```php
   $colors = ["Red", "Green", "Blue"];
   echo $colors[1]; // 输出 Green
   ```

4. **堆栈（Stack）和队列（Queue）：** 堆栈和队列是一种特殊的数组，具有特定的数据结构和操作方式。

   - 堆栈：

     ```php
     $stack = array();
     array_push($stack, "Apple");
     array_push($stack, "Banana");
     $fruit = array_pop($stack); // 从堆栈中弹出 Banana
     ```

   - 队列：

     ```php
     $queue = array();
     array_push($queue, "Apple");
     array_push($queue, "Banana");
     $fruit = array_shift($queue); // 从队列中移出 Apple
     ```

这些数据结构在 PHP 中用于存储和处理数据，你可以根据具体的需求选择适合的数据结构。

### 变量对应关系

`$_POST,$_GET,$FILE`,一类的变量，和请求体是对应的，对应的表单里面的是name的名字，比如表单提交的时候有一个`<input name="dog">`这部分，那到时候找这部分的值的时候就对应使用$_POST['dog']

对于file来说，他还有一些特别的属性

```php
$screenshot = $_FILES['screenshot']['name'];
$screenshot_type = $_FILES['screenshot']['type'];
$screenshot_size = $_FILES['screenshot']['size']; 
$_FILES['screenshot']['tmp_name']
```

### php中的字符串操作函数

1. **explode():**

   - 语法：`explode(分隔符, 字符串, 限制)`

   - 描述：将一个字符串根据指定的分隔符拆分成数组。

   - 示例：

     ```php
     $string = "苹果,香蕉,橙子";
     $fruits = explode(",", $string);
     print_r($fruits); // 输出：Array ( [0] => 苹果 [1] => 香蕉 [2] => 橙子 )
     ```

2. **implode():**

   - 语法：`implode(分隔符, 数组)`

   - 描述：使用指定的分隔符将数组的元素连接成一个字符串。

   - 示例：

     ```php
     $fruits = array("苹果", "香蕉", "橙子");
     $string = implode(", ", $fruits);
     echo $string; // 输出：苹果, 香蕉, 橙子
     ```

3. **str_replace():**

   - 语法：`str_replace(搜索字符串, 替换字符串, 目标字符串, 替换次数)`

   - 描述：在给定的字符串中，将所有出现的搜索字符串替换为替换字符串。

   - 示例：

     ```php
     $string = "你好，世界！";
     $new_string = str_replace("世界", "PHP", $string);
     echo $new_string; // 输出：你好，PHP！
     ```

4. **trim():**

   - 语法：`trim(字符串, 字符集)`

   - 描述：删除字符串开头和结尾的空格或指定的字符集。

   - 示例：

     ```php
     $string = "   你好，世界！   ";
     $new_string = trim($string);
     echo $new_string; // 输出：你好，世界！
     ```

5. **strlen():**

   - 语法：`strlen(字符串)`

   - 描述：返回字符串的长度。

   - 示例：

     ```php
     $string = "你好，世界！";
     $length = strlen($string);
     echo $length; // 输出：9
     ```

6. **strpos():**

   - 语法：`strpos(字符串, 查找字符串, 开始位置)`

   - 描述：查找字符串中第一次出现指定子字符串的位置，并返回其索引。如果未找到，则返回 false。
   - 示例：

   ```php
   $string = "Hello, world!";
   $position = strpos($string, "world");
   echo $position; // 输出：7
   ```

7. **substr():**

   - 语法：`substr(字符串, 起始位置, 长度)`

   - 描述：从字符串中返回指定长度的子字符串。

   - 示例：

     ```php
     $string = "Hello, world!";
     $substring = substr($string, 7, 5);
     echo $substring; // 输出：world
     ```

8. **strtolower() 和 strtoupper():**

   - 语法：`strtolower(字符串)` 和 `strtoupper(字符串)`

   - 描述：将字符串转换为小写或大写。

   - 示例：

     ```php
     $string = "Hello, World!";
     $lowercase = strtolower($string);
     $uppercase = strtoupper($string);
     echo $lowercase; // 输出：hello, world!
     echo $uppercase; // 输出：HELLO, WORLD!
     ```

9. **strrev():**

   - 语法：`strrev(字符串)`

   - 描述：反转字符串中的字符顺序。

   - 示例：

     ```php
     $string = "Hello, World!";
     $reversed = strrev($string);
     echo $reversed; // 输出：!dlroW ,olleH
     ```

10. **htmlspecialchars() 和 htmlentities():**

    - 语法：`htmlspecialchars(字符串)` 和 `htmlentities(字符串)`

    - 描述：将字符串中的特殊字符转换为 HTML 实体。

    - 示例：

      ```php
      $string = "<script>alert('Hello');</script>";
      $escaped = htmlspecialchars($string);
      echo $escaped; // 输出：&lt;script&gt;alert('Hello');&lt;/script&gt;
      ```



### 请求体

一般性的请求体构成原则：

1. **请求头部分**：请求头包含了关于请求的元信息，例如请求方法、请求路径、主机地址、内容类型等。这些信息通过请求头部发送到服务器。
2. **空行**：在请求头部分和请求体之间有一个空行，用于分隔头部和请求体。
3. **请求体部分**：请求体包含了请求所传递的数据。它的内容根据请求方法和内容类型的不同而有所不同。
   - 对于 GET 请求，通常不包含请求体，因为数据直接放在 URL 中。
   - 对于 POST 请求，请求体中包含了提交的数据，可以是表单数据、JSON 数据、XML 数据等。数据的格式由请求头部的 Content-Type 指定。
   - 对于其他 HTTP 方法（如 PUT、DELETE 等），请求体的内容取决于请求的目的和使用场景。

```
GET /ch05/final/guitarwars/admin.php HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Host: localhost
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
```

### 管理员认证

```php
//admin.php
<?php
  require_once('authorize.php');
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Guitar Wars - High Scores Administration</title>
	.......
    
   
//this is authorize.php
<?php
  // User name and password for authentication
  $username = 'rock';
  $password = 'roll';

  if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW']) ||
    ($_SERVER['PHP_AUTH_USER'] != $username) || ($_SERVER['PHP_AUTH_PW'] != $password)) {
    // The user name/password are incorrect so send the authentication headers
    header('HTTP/1.1 401 Unauthorized');
    header('WWW-Authenticate: Basic realm="Guitar Wars"');
    exit('<h2>Guitar Wars</h2>Sorry, you must enter a valid user name and password to access this page.');
  }
?>
//$_SERVER['PHP_AUTH_USER'],$_SERVER['PHP_AUTH_PW']这些值会作为全局变量储存
//通过管理员模式，我们可以对用户提交的信息做一次核对，经过核对的信息才会被存储以及
```

### 用户注册和登陆

```php
 //用户注册 
if (isset($_POST['submit'])) {
    // Grab the profile data from the POST
    $username = mysqli_real_escape_string($dbc, trim($_POST['username']));
    $password1 = mysqli_real_escape_string($dbc, trim($_POST['password1']));
    $password2 = mysqli_real_escape_string($dbc, trim($_POST['password2']));

    if (!empty($username) && !empty($password1) && !empty($password2) && ($password1 == $password2)) {
      // Make sure someone isn't already registered using this username
      $query = "SELECT * FROM mismatch_user WHERE username = '$username'";
      $data = mysqli_query($dbc, $query);
      if (mysqli_num_rows($data) == 0) {
        // The username is unique, so insert the data into the database
        $query = "INSERT INTO mismatch_user (username, password, join_date) VALUES ('$username', SHA('$password1'), NOW())";
        mysqli_query($dbc, $query);

        // Confirm success with the user
        echo '<p>Your new account has been successfully created. You\'re now ready to <a href="login.php">log in</a>.</p>';

        mysqli_close($dbc);
        exit();
      }
      else {
        // An account already exists for this username, so display an error message
        echo '<p class="error">An account already exists for this username. Please use a different address.</p>';
        $username = "";
      }
    }
 //password确认两次
 //password在传到服务器前用SHA加密
 //避免出现相同的用户名
 //exit() 是 PHP 中用于终止脚本执行的函数。它可以用于退出当前的 PHP 脚本，停止执行后续的代码。通常情况下，exit() 函数可以带有一个可选的状态码参数，用于指定脚本的退出状态。
    
//用户登陆
  if (!isset($_SESSION['user_id'])) {
    if (isset($_POST['submit'])) {
      // Connect to the database
      $dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

      // Grab the user-entered log-in data
      $user_username = mysqli_real_escape_string($dbc, trim($_POST['username']));
      $user_password = mysqli_real_escape_string($dbc, trim($_POST['password']));

      if (!empty($user_username) && !empty($user_password)) {
        // Look up the username and password in the database
        $query = "SELECT user_id, username FROM mismatch_user WHERE username = '$user_username' AND password = SHA('$user_password')";
        $data = mysqli_query($dbc, $query);

        if (mysqli_num_rows($data) == 1) {
          // The log-in is OK so set the user ID and username session vars (and cookies), and redirect to the home page
          $row = mysqli_fetch_array($data);
          $_SESSION['user_id'] = $row['user_id'];
          $_SESSION['username'] = $row['username'];
          setcookie('user_id', $row['user_id'], time() + (60 * 60 * 24 * 30));    // expires in 30 days
          setcookie('username', $row['username'], time() + (60 * 60 * 24 * 30));  // expires in 30 days
          $home_url = 'http://' . $_SERVER['HTTP_HOST'] . dirname($_SERVER['PHP_SELF']) . '/index.php';
          header('Location: ' . $home_url);
        }
        else {
          // The username/password are incorrect so set an error message
          $error_msg = 'Sorry, you must enter a valid username and password to log in.';
        }
      }
      else {
        // The username/password weren't entered so set an error message
        $error_msg = 'Sorry, you must enter your username and password to log in.';
      }
    }    
```

### mysqli函数集合

好的，以下是一些常用的 mysqli 函数及其简要说明：

1. **mysqli_connect()**：建立与 MySQL 数据库服务器的连接。

   ```php
   $link = mysqli_connect($host, $user, $password, $database);
   ```

2. **mysqli_close()**：关闭与 MySQL 数据库服务器的连接。

   ```php
   mysqli_close($link);
   ```

3. **mysqli_real_escape_string()**：对字符串进行 SQL 转义，防止 SQL 注入攻击。

   ```php
   $escaped_string = mysqli_real_escape_string($link, $string);
   ```

4. **mysqli_query()**：执行一条 SQL 查询。

   ```php
   $result = mysqli_query($link, $query);
   ```

5. **mysqli_num_rows()**：返回结果集中的行数。

   ```php
   $num_rows = mysqli_num_rows($result);
   ```

6. **mysqli_fetch_array()**：从结果集中获取一行作为关联数组、数字数组或混合数组。

   ```php
   $row = mysqli_fetch_array($result, $resulttype);
   //这是一个类似C语言里面文件读取的操作，每读取一次，对应的指针就会偏移一次，一般使用类似下面的方式来完成全部读取
     while ($row = mysqli_fetch_array($data)) {
   	//dosomething
     }
   //在读完以后最后一个读到的值是NULL，也就会跳出循环了。
   ```

7. **mysqli_insert_id()**：返回最后插入行的 ID。

   ```php
   $last_insert_id = mysqli_insert_id($link);
   ```

8. **mysqli_error()**：返回上一个数据库操作的错误消息。

   ```php
   $error_message = mysqli_error($link);
   ```

9. **mysqli_stmt_prepare()**：准备要执行的 SQL 语句。

   ```php
   $stmt = mysqli_stmt_prepare($link, $query);
   ```

10. **mysqli_stmt_bind_param()**：将变量与预处理语句中的参数绑定。

    ```php
    mysqli_stmt_bind_param($stmt, $types, $param1, $param2, ...);
    ```

11. **mysqli_stmt_execute()**：执行准备好的语句。

    ```php
    mysqli_stmt_execute($stmt);
    ```

这些函数能够帮助你在 PHP 中与 MySQL 数据库进行交互，执行查询、插入、更新、删除等操作，并处理错误和防止 SQL 注入攻击。

### 设置cookie

#### 添加cookie

setcookie(变量名称，给变量赋的值，time()+（cookie保存的时间）)，这里的时间是以秒为单位的

```php
/var/www/html/ch07/final/mismatch/#login.php#
30:          setcookie('user_id', $row['user_id'], time() + (60 * 60 * 24 * 30));    // expires in 30 days
31:          setcookie('username', $row['username'], time() + (60 * 60 * 24 * 30));  // expires in 30 days
```

#### 清除cookie

和上面的类似，setcookie(变量的名称，‘’，time()-3600),它的意思是把变量置空，并且在一小时之前就过期了，浏览器就会清除这个cookie，cookie一类的操作主要还是依靠浏览器完成的。

```php
setcookie('user_id', '',time() - 3600);
```

### session与cookie

#### 二者之间的差异

- **Session** 是一种在服务器端保存状态信息的机制。当用户访问网站时，服务器会为每个用户创建一个唯一的会话标识（session ID），并将该标识存储在服务器上。在会话期间，服务器可以使用该会话标识来存储和检索与用户相关的数据。通常情况下，会话数据存储在服务器的内存中或持久化存储（例如数据库）中。Session 机制可以用于跟踪用户的登录状态、购物车内容、用户首选项等信息。
- **Cookie** 是一种在客户端（通常是用户的浏览器）保存数据的机制。服务器可以通过设置 HTTP 响应头来向客户端发送 Cookie，客户端会将这些 Cookie 存储在本地。随后，客户端的每个请求都会自动将相应的 Cookie 发送回服务器。Cookie 可以用于跟踪用户的浏览行为、记住用户的登录凭证、记录用户的偏好设置等。由于 Cookie 存储在客户端，因此它们可以被用户随时删除或修改，因此不适合存储敏感信息。

#### session的储存路径

在默认情况下，如果没有对会话存储路径进行配置，PHP 的会话数据将会保存在服务器的临时文件夹中。对于 Apache 服务器，这些临时文件夹通常位于操作系统的临时目录下。

具体而言，对于使用 PHP 的 Apache 服务器，会话文件通常会存储在 `/var/lib/php/sessions/` 目录中。在这个目录下，每个会话都会有一个对应的会话文件，文件名以 `sess_` 开头，后跟会话 ID。例如，`sess_jaklfj2o3ij3oifj3oij3o`。这些会话文件是由 PHP 自动创建和管理的。

你可以在服务器上使用命令行或文件浏览器来访问这个目录，查看其中的会话文件。需要注意的是，这些会话文件通常是以 PHP 序列化格式存储的，你可能需要解析这些文件才能读取其中的内容。

如果你想确认会话的存储路径，可以查看你的 PHP 配置文件（通常是 `php.ini` 文件）中的 `session.save_path` 配置选项。你也可以在 PHP 的信息页面中找到这个配置的值。

![查看会话中储存的变量以及他们的值](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240514104555821.png)

#### cookie的存储路径

在ubuntu下的chrome中cookie的默认存储路径是~/.config/google-chrome/Default,[可以从chrome://version网站获取](chrome://version/)

![cookie的存储路径](https://raw.githubusercontent.com/Cipivious/my_try/main/image/image-20240514105206809.png)

### cookie值的解释

- `creation_utc`：记录条目创建的时间戳。
- `host_key`：存储网站的主机键或主机名。
- `top_frame_site_key`：记录顶层框架的站点键。
- `name`：存储 cookie 的名称。
- `value`：存储 cookie 的值。
- `encrypted_value`：可能是存储加密的 cookie 值（如果浏览器启用了 cookie 加密）。
- `path`：记录 cookie 的路径。
- `expires_utc`：记录 cookie 过期的时间戳。
- `is_secure`：指示是否是安全 cookie。
- `is_httponly`：指示是否是 HTTP only cookie。
- `last_access_utc`：记录最后一次访问此 cookie 的时间戳。
- `has_expires`：指示是否设置了 cookie 的过期时间。
- `is_persistent`：指示是否是持久 cookie。
- `priority`：可能是 cookie 的优先级。
- `samesite`：指示 cookie 的 SameSite 属性。
- `source_scheme`：记录来源的协议方案。
- `source_port`：记录来源的端口。
- `last_update_utc`：记录此条目的最后更新时间戳。

### 页面重定向

```php
$home_url = 'http://' . $_SERVER['HTTP_HOST'] . dirname($_SERVER['PHP_SELF']) . '/index.php';
header('Location: ' . $home_url);

假设当前脚本的 URL 是 http://www.example.com/folder/script.php：

$_SERVER['HTTP_HOST'] 是 www.example.com 主机地址
$_SERVER['PHP_SELF'] 是 /folder/script.php 当前正在执行的脚本的路径
dirname($_SERVER['PHP_SELF']) 是 /folder 文件夹
所以 $home_url 最终是 http://www.example.com/folder/index.php
header('Location: ' . $home_url); 发送 HTTP 头，使得浏览器重定向到 http://www.example.com/folder/index.php
这个重定向通常用于用户认证、表单处理后跳转等情景。
```

### 分页展示示例脚本

```php
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Risky Jobs - Search</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <img src="riskyjobs_title.gif" alt="Risky Jobs" />
  <img src="riskyjobs_fireman.jpg" alt="Risky Jobs" style="float:right" />
  <h3>Risky Jobs - Search Results</h3>

<?php
  // This function builds a search query from the search keywords and sort setting
  function build_query($user_search, $sort) {
    $search_query = "SELECT * FROM riskyjobs";

    // Extract the search keywords into an array
    $clean_search = str_replace(',', ' ', $user_search);
    $search_words = explode(' ', $clean_search);
    $final_search_words = array();
    if (count($search_words) > 0) {
      foreach ($search_words as $word) {
        if (!empty($word)) {
          $final_search_words[] = $word;
        }
      }
    }

    // Generate a WHERE clause using all of the search keywords
    $where_list = array();
    if (count($final_search_words) > 0) {
      foreach($final_search_words as $word) {
        $where_list[] = "description LIKE '%$word%'";
      }
    }
    $where_clause = implode(' OR ', $where_list);

    // Add the keyword WHERE clause to the search query
    if (!empty($where_clause)) {
      $search_query .= " WHERE $where_clause";
    }

    // Sort the search query using the sort setting
    switch ($sort) {
    // Ascending by job title
    case 1:
      $search_query .= " ORDER BY title";
      break;
    // Descending by job title
    case 2:
      $search_query .= " ORDER BY title DESC";
      break;
    // Ascending by state
    case 3:
      $search_query .= " ORDER BY state";
      break;
    // Descending by state
    case 4:
      $search_query .= " ORDER BY state DESC";
      break;
    // Ascending by date posted (oldest first)
    case 5:
      $search_query .= " ORDER BY date_posted";
      break;
    // Descending by date posted (newest first)
    case 6:
      $search_query .= " ORDER BY date_posted DESC";
      break;
    default:
      // No sort setting provided, so don't sort the query
    }

    return $search_query;
  }

  // This function builds heading links based on the specified sort setting
  function generate_sort_links($user_search, $sort) {
    $sort_links = '';

    switch ($sort) {
    case 1:
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=2">Job Title</a></td><td>Description</td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=3">State</a></td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=5">Date Posted</a></td>';
      break;
    case 3:
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=1">Job Title</a></td><td>Description</td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=4">State</a></td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=5">Date Posted</a></td>';
      break;
    case 5:
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=1">Job Title</a></td><td>Description</td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=3">State</a></td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=6">Date Posted</a></td>';
      break;
    default:
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=1">Job Title</a></td><td>Description</td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=3">State</a></td>';
      $sort_links .= '<td><a href = "' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=5">Date Posted</a></td>';
    }

    return $sort_links;
  }

  // This function builds navigational page links based on the current page and the number of pages
  function generate_page_links($user_search, $sort, $cur_page, $num_pages) {
    $page_links = '';

    // If this page is not the first page, generate the "previous" link
    if ($cur_page > 1) {
      $page_links .= '<a href="' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=' . $sort . '&page=' . ($cur_page - 1) . '"><-</a> ';
    }
    else {
      $page_links .= '<- ';
    }

    // Loop through the pages generating the page number links
    for ($i = 1; $i <= $num_pages; $i++) {
      if ($cur_page == $i) {
        $page_links .= ' ' . $i;
      }
      else {
        $page_links .= ' <a href="' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=' . $sort . '&page=' . $i . '"> ' . $i . '</a>';
      }
    }

    // If this page is not the last page, generate the "next" link
    if ($cur_page < $num_pages) {
      $page_links .= ' <a href="' . $_SERVER['PHP_SELF'] . '?usersearch=' . $user_search . '&sort=' . $sort . '&page=' . ($cur_page + 1) . '">-></a>';
    }
    else {
      $page_links .= ' ->';
    }

    return $page_links;
  }

  // Grab the sort setting and search keywords from the URL using GET
  $sort = $_GET['sort'];
  $user_search = $_GET['usersearch'];

  // Calculate pagination information
  $cur_page = isset($_GET['page']) ? $_GET['page'] : 1;
  $results_per_page = 5;  // number of results per page
  $skip = (($cur_page - 1) * $results_per_page);

  // Start generating the table of results
  echo '<table border="0" cellpadding="2">';

  // Generate the search result headings
  echo '<tr class="heading">';
  echo generate_sort_links($user_search, $sort);
  echo '</tr>';

  // Connect to the database
  require_once('connectvars.php');
  $dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

  // Query to get the total results 
  $query = build_query($user_search, $sort);
  $result = mysqli_query($dbc, $query);
  $total = mysqli_num_rows($result);
  $num_pages = ceil($total / $results_per_page);

  // Query again to get just the subset of results
  $query =  $query . " LIMIT $skip, $results_per_page";
  $result = mysqli_query($dbc, $query);
  while ($row = mysqli_fetch_array($result)) {
    echo '<tr class="results">';
    echo '<td valign="top" width="20%">' . $row['title'] . '</td>';
    echo '<td valign="top" width="50%">' . substr($row['description'], 0, 100) . '...</td>';
    echo '<td valign="top" width="10%">' . $row['state'] . '</td>';
    echo '<td valign="top" width="20%">' . substr($row['date_posted'], 0, 10) . '</td>';
    echo '</tr>';
  } 
  echo '</table>';

  // Generate navigational page links if we have more than one page
  if ($num_pages > 1) {
    echo generate_page_links($user_search, $sort, $cur_page, $num_pages);
  }

  mysqli_close($dbc);
?>

</body>
</html>
```

### 图形验证

```php
//该文件名为captcha.php
//使用方法为：
//<img src="captcha.php" alt="Verification pass-phrase" />
//还需要加入以下的验证
//    $user_pass_phrase = hash('sha256', $_POST['verify']);
//    if ($_SESSION['pass_phrase'] == $user_pass_phrase) {


<?php
session_start();

// Set some important CAPTCHA constants
define('CAPTCHA_NUMCHARS', 6);  // number of characters in pass-phrase
define('CAPTCHA_WIDTH', 100);   // width of image
define('CAPTCHA_HEIGHT', 25);   // height of image

// Generate the random pass-phrase
$pass_phrase = "";
for ($i = 0; $i < CAPTCHA_NUMCHARS; $i++) {
    $pass_phrase .= chr(rand(97, 122));
}

// Store the encrypted pass-phrase in a session variable
$_SESSION['pass_phrase'] = hash('sha256', $pass_phrase);

// Create the image
$img = imagecreatetruecolor(CAPTCHA_WIDTH, CAPTCHA_HEIGHT);

// Set a white background with black text and gray graphics
$bg_color = imagecolorallocate($img, 255, 255, 255);     // white
$text_color = imagecolorallocate($img, 0, 0, 0);         // black
$graphic_color = imagecolorallocate($img, 64, 64, 64);   // dark gray

// Fill the background
imagefilledrectangle($img, 0, 0, CAPTCHA_WIDTH, CAPTCHA_HEIGHT, $bg_color);

// Draw some random lines
for ($i = 0; $i < 5; $i++) {
    imageline($img, 0, rand() % CAPTCHA_HEIGHT, CAPTCHA_WIDTH, rand() % CAPTCHA_HEIGHT, $graphic_color);
}

// Sprinkle in some random dots
for ($i = 0; $i < 50; $i++) {
    imagesetpixel($img, rand() % CAPTCHA_WIDTH, rand() % CAPTCHA_HEIGHT, $graphic_color);
}

// Draw the pass-phrase string
$font_path = '/var/www/html/ch11/final/guitarwars/Courier New Bold.ttf';  // Update this path to your font file
imagettftext($img, 18, 0, 5, CAPTCHA_HEIGHT - 5, $text_color, $font_path, $pass_phrase);

// Output the image as a PNG using a header
header("Content-type: image/png");
imagepng($img);

// Clean up
imagedestroy($img);
?>
```

### 权限

在服务器当中，要给文件配置合适的读写权限，否则会引发严重的问题，会出现严重的500错误。









## 安装php

### **安装 PHP 解释器**：

- 在 Ubuntu 上，您可以使用以下命令安装 PHP：

  ```bash
  sudo apt update
  sudo apt install php
  sudo apt install php-mysqli #这个部分是为了安装mysqli，它负责建立与数据库的连接
  sudo apt-get install php-gd #这个部分是为了安装图形验证的库
  sudo apt-get install php-xml #这一部分是为了安装xml写入的库
  ```

### **配置 Web 服务器**：

     - 如果您只需要在本地运行 PHP 文件而不是 Web 应用程序，则可以跳过此步骤。
    
     - 如果您计划在本地搭建 Web 应用程序，则需要配置 Web 服务器，例如 Apache 或 Nginx，并将 PHP 配置为 Web 服务器的模块或 FastCGI 进程。
    
     - 在 Ubuntu 上，您可以使用以下命令安装 Apache 和 PHP：
    
       ```
       sudo apt update
       sudo apt install apache2
       sudo apt install libapache2-mod-php
       ```
    
     - 在 Windows 上，您可以安装 WampServer、XAMPP 或直接在 IIS 上配置 PHP。

### **创建和运行 PHP 文件**：

     - 创建一个新的 PHP 文件，例如 
    
       ```
       hello.php
       ```
    
       并在其中编写 PHP 代码，例如：
    
       ```
       <?php
       echo "Hello, World!";
       ?>
       ```
    
     - 将该 PHP 文件放在您的 Web 服务器的文档根目录下（通常是 `/var/www/html` 或 `C:\xampp\htdocs`）。
    
     - 启动您的 Web 服务器，并在浏览器中访问该 PHP 文件的 URL（例如 `http://localhost/hello.php`）以查看 PHP 运行结果。



