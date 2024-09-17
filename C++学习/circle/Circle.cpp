// Circle.cpp
#include "Circle.h"
#include <cmath>  // For std::sqrt and std::pow

const double PI = 3.14159265358979323846;  // More precise value of PI

int Circle::check_position(const Point& position) {
    double len = std::sqrt(std::pow(circle_center.x - position.x, 2) + std::pow(circle_center.y - position.y, 2));
    if (len > r) {
        return 1; // Outside
    } else if (len == r) {
        return 0; // On the circle
    } else {
        return -1; // Inside
    }
}

double Circle::calculate_circumference() {
    return 2 * PI * r;
}
