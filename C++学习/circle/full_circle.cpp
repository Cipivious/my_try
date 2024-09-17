#include <iostream>
#include <cmath>  // Correct include for C++

const double PI = 3.14159265358979323846;  // More precise value of PI

class Point {
public:
    double x;
    double y;
};

class Circle {
public:
    double r;
    Point circle_center;

    // Method to check position of a point relative to the circle
    int check_position(const Point& position) {
        double len = std::sqrt(std::pow(circle_center.x - position.x, 2) + std::pow(circle_center.y - position.y, 2));
        if (len > r) {
            return 1; // Outside
        } else if (len == r) {
            return 0; // On the circle
        } else {
            return -1; // Inside
        }
    }

    // Method to calculate the circumference of the circle
    double calculate_circumference() {
        return 2 * PI * r;
    }
};

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
