#include <iostream>
#include <string>

// class GoodGay; // Forward declaration

class Building
{
public:
    Building();           // Declare constructor
    friend class GoodGay; // Declare GoodGay as friend
private:
    std::string m_sitting_room;
    std::string m_bedroom;
};

class GoodGay
{
public:
    GoodGay();  // Declare constructor
    ~GoodGay(); // Declare destructor for cleanup
    void visit();

private:
    Building *building;
};

// Define Building constructor
Building::Building()
{
    m_sitting_room = "sitting room";
    m_bedroom = "bedroom";
}

// Define GoodGay constructor
GoodGay::GoodGay()
{
    building = new Building();
}

// Define GoodGay destructor
GoodGay::~GoodGay()
{
    delete building;
}

// Define visit function
void GoodGay::visit()
{
    std::cout << "visit " << building->m_sitting_room << std::endl;
    std::cout << "visit " << building->m_bedroom << std::endl;
}

int main()
{
    GoodGay gg;
    gg.visit();
    return 0;
}
