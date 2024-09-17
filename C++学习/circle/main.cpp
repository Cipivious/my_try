// main.cpp
#include <iostream>
#include "Circle.h"

int main() {
    Circle c1;
    c1.r = 2;
    c1.circle_center.x = 0;
    c1.circle_center.y = 1;

    Point p;
    p.x = 0;
    p.y = 2;
    int result = c1.check_position(p);

    std::cout << "The position between the circle and point is: " << result << std::endl;
    std::cout << "Circumference of the circle is: " << c1.calculate_circumference() << std::endl;
    return 0;
}
