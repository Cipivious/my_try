#include "CSVHandler.h"
#include <fstream>
#include <sstream>
#include <stdexcept>

// 读取 CSV 文件的实现
std::vector<std::vector<std::string>> CSVHandler::readCSV(const std::string &filename)
{
    std::ifstream file(filename);
    if (!file.is_open())
    {
        throw std::runtime_error("Could not open file");
    }

    std::vector<std::vector<std::string>> data;
    std::string line, cell;

    while (std::getline(file, line))
    {
        std::stringstream lineStream(line);
        std::vector<std::string> row;

        while (std::getline(lineStream, cell, ','))
        {
            row.push_back(cell);
        }

        data.push_back(row);
    }

    file.close();
    return data;
}

// 写入 CSV 文件的实现
void CSVHandler::writeCSV(const std::string &filename, const std::vector<std::vector<std::string>> &data)
{
    std::ofstream file(filename);
    if (!file.is_open())
    {
        throw std::runtime_error("Could not open file");
    }

    for (const auto &row : data)
    {
        for (size_t i = 0; i < row.size(); ++i)
        {
            file << row[i];
            if (i != row.size() - 1)
            {
                file << ",";
            }
        }
        file << "\n";
    }

    file.close();
}
