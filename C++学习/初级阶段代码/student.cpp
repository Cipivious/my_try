#include <iostream>
#include <string>

class Student {
public:
    std::string name;  // 使用std::string默认构造函数初始化为空字符串
    std::string id;    // 同上

    void set_name(const std::string& c_name) {
        name = c_name;
    }

    void set_id(const std::string& c_id) {
        id = c_id;
    }

    void show_info() {
        // std::string 为空的检测应使用empty()函数
        if (!name.empty() && !id.empty()) {
            std::cout << "name: " << name << " id: " << id << std::endl;
        }
        else {
            std::cout << "the information of the student is not input!";
        }
    }
};

int main() {
    Student zhangsan;
    zhangsan.set_name("zhangsan");
    zhangsan.set_id("123456789");
    zhangsan.show_info();  // 现在会正确显示信息
    return 0;
}
