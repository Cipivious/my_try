#include <iostream>

template<typename T>
class MyArray{
    public:
    T* array;
    int storage;
    int size;
    MyArray(int storage){
        this->array = new T[storage];
        this->storage = storage;
        this->size = 0;
    }
    MyArray(MyArray& myarray){
        this->storage = myarray.storage;
        this->size = myarray.size;
        this->array = new T[storage];
        for(int i = 0; i < storage; i++){
            array[i] = myarray.array[i];
        }
    }
    void operator=(MyArray& myarray){
        this->storage = myarray.storage;
        this->size = myarray.size;
        this->array = new T[storage];
        for(int i = 0; i < myarray.storage; i++){
            array[i] = myarray.array[i];
        }
    }
    T& operator[](int index){
        return array[index];
    }
    ~MyArray(){
        delete array;
    }
    void append(T element){
        if(size < storage){
            array[size] = element;            
            size++;
        }else{
            std::cout << "the storage of this array is over, please create a new one";
        }
    }
    void remove(){
        size--;
    }
};

void test01(){
    MyArray<int> array(10);
    array.append(20);
    array.append(30);
    MyArray<int> array2 = array;
    std::cout << "array[0] is " << array2[0] << std::endl;
    std::cout << "array[1] is " << array2[1] << std::endl;
    std::cout << "array's size is " << array2.size << std::endl;
    array.remove();
    std::cout << "array's size is " << array2.size << std::endl;
    return;
}

int main(){
    test01();
    return 0; 
}