#ifndef CSVHANDLER_H
#define CSVHANDLER_H

#include <string>
#include <vector>

class CSVHandler
{
public:
    // 读取 CSV 文件，返回一个二维字符串向量
    static std::vector<std::vector<std::string>> readCSV(const std::string &filename);

    // 写入数据到 CSV 文件，接收一个二维字符串向量
    static void writeCSV(const std::string &filename, const std::vector<std::vector<std::string>> &data);
};

#endif // CSVHANDLER_H
