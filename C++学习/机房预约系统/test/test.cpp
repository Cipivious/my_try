#include "gtest/gtest.h"
#include <iostream>
#include <string>
// #include "CSVHandler.h"
// #include <vector>

int add(int a, int b)
{
    return a + b;
}

TEST(Add, negative)
{
    EXPECT_EQ(-3, add(-2, -1));
    EXPECT_EQ(-2, add(1, -3));
}

TEST(Add, positive)
{
    EXPECT_EQ(1, add(2, -1));
    EXPECT_EQ(2, add(-1, 3));
}

TEST(Add, limit)
{
    int a = 0x7fffffff + 1;
    std::cout << "a = " << a << "\n";
    EXPECT_EQ(a, add(0x7fffffff, 1));
    EXPECT_EQ(0, add(0xffffffff, 1));
}

int main(int argc, char **argv)
{

    ::testing::InitGoogleTest(&argc, argv);
    //::testing::GTEST_FLAG(output) = "text";

    return RUN_ALL_TESTS();

    return 0;
}

// #include <gtest/gtest.h>
// #include "CSVHandler.h"
// #include <vector>
// #include <string>

// // 测试写入 CSV 文件
// TEST(CSVHandlerTest, WriteCSV)
// {
//     // 准备要写入的数据
//     std::vector<std::vector<std::string>> data = {
//         {"Name", "Age", "City"},
//         {"Alice", "28", "Paris"},
//         {"Bob", "34", "Berlin"},
//         {"Charlie", "22", "Tokyo"}};

//     // 写入 CSV 文件
//     ASSERT_NO_THROW({
//         CSVHandler::writeCSV("test_output.csv", data);
//     });
// }

// // 测试读取 CSV 文件
// TEST(CSVHandlerTest, ReadCSV)
// {
//     // 准备要写入的数据
//     std::vector<std::vector<std::string>> expectedData = {
//         {"Name", "Age", "City"},
//         {"Alice", "28", "Paris"},
//         {"Bob", "34", "Berlin"},
//         {"Charlie", "22", "Tokyo"}};

//     // 从 CSV 文件中读取数据
//     std::vector<std::vector<std::string>> readData;
//     ASSERT_NO_THROW({
//         readData = CSVHandler::readCSV("test_output.csv");
//     });

//     // 验证读取到的数据与预期的数据是否相同
//     ASSERT_EQ(readData.size(), expectedData.size());

//     for (size_t i = 0; i < expectedData.size(); ++i)
//     {
//         ASSERT_EQ(readData[i], expectedData[i]);
//     }
// }

// // main 函数，执行所有测试
// int main(int argc, char **argv)
// {
//     std::cout << "hello world" << std::endl;
//     ::testing::InitGoogleTest(&argc, argv);
//     return RUN_ALL_TESTS();
// }

// #include <iostream>
// #include "CSVHandler.h"

// int main()
// {
//     // 准备要写入的数据
//     std::vector<std::vector<std::string>> data = {
//         {"Name", "Age", "City"},
//         {"Alice", "28", "Paris"},
//         {"Bob", "34", "Berlin"},
//         {"Charlie", "22", "Tokyo"}};

//     // 写入 CSV 文件
//     try
//     {
//         CSVHandler::writeCSV("test_output.csv", data);
//         std::cout << "Data written to CSV file successfully!" << std::endl;
//     }
//     catch (const std::exception &e)
//     {
//         std::cerr << "Error writing CSV: " << e.what() << std::endl;
//     }

//     // 从 CSV 文件中读取数据
//     try
//     {
//         std::vector<std::vector<std::string>> readData = CSVHandler::readCSV("test_output.csv");
//         std::cout << "Data read from CSV file:" << std::endl;

//         // 打印读取的数据
//         for (const auto &row : readData)
//         {
//             for (const auto &cell : row)
//             {
//                 std::cout << cell << " ";
//             }
//             std::cout << std::endl;
//         }
//     }
//     catch (const std::exception &e)
//     {
//         std::cerr << "Error reading CSV: " << e.what() << std::endl;
//     }

//     return 0;
// }
