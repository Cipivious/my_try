#include <iostream>

template<typename T>
void swap(T& a, T& b){
    T temp;
    temp = a;
    a = b;
    b = temp;
}

void test01(){
    int a = 0;
    int b = 1;
    swap(a, b);
    std::cout << "a is: " << a << std::endl;
    std::cout << "b is: " << b << std::endl;
    return;
}

int main(){
    test01();
    return 0;
}