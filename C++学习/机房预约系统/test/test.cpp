#include <iostream>
#include "CSVHandler.h"

int main()
{
    // 准备要写入的数据
    std::vector<std::vector<std::string>> data = {
        {"Name", "Age", "City"},
        {"Alice", "28", "Paris"},
        {"Bob", "34", "Berlin"},
        {"Charlie", "22", "Tokyo"}};

    // 写入 CSV 文件
    try
    {
        CSVHandler::writeCSV("test_output.csv", data);
        std::cout << "Data written to CSV file successfully!" << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error writing CSV: " << e.what() << std::endl;
    }

    // 从 CSV 文件中读取数据
    try
    {
        std::vector<std::vector<std::string>> readData = CSVHandler::readCSV("test_output.csv");
        std::cout << "Data read from CSV file:" << std::endl;

        // 打印读取的数据
        for (const auto &row : readData)
        {
            for (const auto &cell : row)
            {
                std::cout << cell << " ";
            }
            std::cout << std::endl;
        }
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error reading CSV: " << e.what() << std::endl;
    }

    return 0;
}
