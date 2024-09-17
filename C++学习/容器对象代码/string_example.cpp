#include <iostream>
#include <string>

void test01(){
    std::string str = "<p>this is a text</p>";
    int left_pos = str.find(">");
    int right_pos = str.rfind("<");
    std::string sub_str = str.substr(left_pos+1, right_pos-3);
    std::cout << sub_str << std::endl;
}

int main(){
    test01();
    return 0;
}