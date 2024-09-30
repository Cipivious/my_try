# gtest 测试框架（C++）

## 配置 gtest

1. 使用 vcpkg install gtest 安装 gtest
2. 写 CMakeLists.txt 文件，添加下面内容

   ```cmake
   enable_testing()

   # 查找 Google Test 库
   find_package(GTest CONFIG REQUIRED)

   # 包含头文件的目录（你之前的配置）
   include_directories(include)

   # 为你的测试源文件创建可执行目标（例如 test_csv）
   add_executable(test_csv test/test.cpp)
   target_sources(test_csv PRIVATE ${SOURCE_FILES})

   # 将 GTest 链接到测试可执行目标中
   target_link_libraries(test_csv PRIVATE GTest::gtest GTest::gtest_main)

   # 添加一个测试，使用 test_csv 可执行文件
   add_test(NAME AllTestsInMain COMMAND test_csv)
   ```

3. 类似下面的格式，写具体的测试的内容

   ```cpp
   // 这里有一个注意的要点，就是TEST后面有两个参数，其中前面一个必须一致，否则编译通过以后会出现段错误。
   #include "gtest/gtest.h"
   #include <iostream>
   #include <string>

   int add(int a, int b)
   {
        return a + b;
   }

   TEST(add, negative)
   {
        EXPECT_EQ(-3, add(-2,-1));
        EXPECT_EQ(-2, add(1,-3));
   }

   TEST(add, positive)
   {
        EXPECT_EQ(1, add(2,-1));
        EXPECT_EQ(2, add(-1,3));
   }

   TEST(add, limit)
   {
        int a = 0x7fffffff + 1;
        std::cout<<"a = "<<a<<"\n";
        EXPECT_EQ(a, add(0x7fffffff,1));
        EXPECT_EQ(0, add(0xffffffff,1));
   }

   int main(int argc, char **argv){
        ::testing::InitGoogleTest(&argc, argv);
        return RUN_ALL_TESTS();
        return 0;
   }
   ```
