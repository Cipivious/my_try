
#include <iostream>
#include <map>
#include <algorithm>
#include <string>

void test01(){
    std::map<std::string, std::string> dog;
    dog["name"] = "zhangsan";
    dog["age"] = "18";
    dog["hobby"] = "sleep";

    std::for_each(dog.begin(), dog.end(), [](std::pair<const std::string, std::string>& pair){std::cout << pair.first << ": " << pair.second << std::endl;});
}

int main(){
    test01();
    return 0;
}