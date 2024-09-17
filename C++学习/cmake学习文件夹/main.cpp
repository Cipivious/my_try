#include <iostream>
#include <nlohmann/json.hpp>

int main() {
    // 创建一个 JSON 对象
    nlohmann::json j;
    j["name"] = "John";
    j["age"] = 30;
    j["is_student"] = false;

    // 输出 JSON 对象
    std::cout << j << std::endl;

    return 0;
}
