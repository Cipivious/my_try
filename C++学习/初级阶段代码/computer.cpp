#include <iostream>

class Cpu{
    public:
    virtual void calculate() = 0;
};

class Gpu{
    public:
    virtual void display() = 0;
};

class Memory{
    public:
    virtual void storage() = 0;
};
class IntelCpu: public Cpu{
    public:
    virtual void calculate() {
        std::cout << "intel cpu is calculating..." << std::endl;
    }
};

class IntelGpu: public Gpu{
    public:
    virtual void display() {
        std::cout << "intel gpu is displaying..." << std::endl;
    }
};

class INtelMemory: public Memory{
    public:
    virtual void storage() {
        std::cout << "intel memory is memorying..." << std::endl;
    }
};
class IntelCpu2: public Cpu{
    public:
    virtual void calculate() {
        std::cout << "intel2 cpu is calculating..." << std::endl;
    }
};

class IntelGpu2: public Gpu{
    public:
    virtual void display() {
        std::cout << "intel2 gpu is displaying..." << std::endl;
    }
};

class INtelMemory2: public Memory{
    public:
    virtual void storage() {
        std::cout << "intel2 memory is memorying..." << std::endl;
    }
};
class Computer{
    public:
    Cpu* cpu;
    Gpu* gpu;
    Memory* memory;
    Computer(Cpu* cpu, Gpu* gpu, Memory* memory){
        this->cpu = cpu;
        this->gpu = gpu;
        this->memory = memory;
    }
    void start(){
        this->cpu->calculate();
        this->gpu->display();
        this->memory->storage();
    }
    ~Computer(){
        std::cout << "now is running ~Computer()" << std::endl;
        delete this->cpu;
        delete this->gpu;
        delete this->memory;
    }
};

int main(){
    Computer first_computer(new IntelCpu, new IntelGpu, new INtelMemory);
    Computer secend_computer(new IntelCpu2, new IntelGpu2, new INtelMemory2);
    Computer third_computer(new IntelCpu, new IntelGpu2, new INtelMemory2);
    first_computer.start();
    std::cout << "------------------------------" << std::endl;
    secend_computer.start();
    std::cout << "------------------------------" << std::endl;
    third_computer.start();
    std::cout << "------------------------------" << std::endl;
    return 0;
}