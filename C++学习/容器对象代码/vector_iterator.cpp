#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

int add(int value, int add_number){
    return value + add_number;
}

void test01(){
    std::vector<std::vector<int>> two_dim_arr;
    std::vector<int> arr = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    for(int i = 0; i < 10; i++){
        std::for_each(arr.begin(), arr.end(), [i](int &n){n+=i;});
        two_dim_arr.push_back(arr);
    }
    for(std::vector<std::vector<int>>::iterator it = two_dim_arr.begin(); it != two_dim_arr.end(); it++){
        for(int i = 0; i < 10; i++){
            std::cout << (*it)[i] <<" ";
        }
        std::cout << std::endl;
    }
}
template<typename T>
void print_arr(T& arr){
    std::for_each(arr.begin(), arr.end(), [](int &n){std::cout << n << " ";});
}

void test02(){
    std::vector<int> arr = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    arr.insert(arr.begin()+2, 5);
    arr.insert(arr.end() - 4, 20);
    arr.erase(arr.begin() + 4);
    std::sort(arr.begin(), arr.end());
    print_arr(arr);
}
void test03(){
    std::vector<int> arr;
    int capacity = 0;
    int num = 10000;
    int* p = NULL;
    arr.reserve(10000); 
    for(int i = 0; i < 10000; i++){
        arr.push_back(i);
        if(capacity != arr.capacity() || p != &arr[0]){
            std::cout << "arr'capacity is: " << capacity << std::endl;
            capacity = arr.capacity();
            std::cout << "the num is: " << num << std::endl;
            num++;
            p = &arr[0];
        }
    }
}
void test04(){
    std::deque<int> deque_example = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    deque_example.insert(deque_example.begin()+2, 5);
    deque_example.insert(deque_example.end() - 4, 20);
    deque_example.erase(deque_example.begin() + 4);
    print_arr(deque_example);
}

int main(){
    test02();
    return 0;
}











































