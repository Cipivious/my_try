// Circle.h
#ifndef CIRCLE_H
#define CIRCLE_H

#include "Point.h"  // Include the Point class definition

class Circle {
public:
    double r;
    Point circle_center;

    int check_position(const Point& position);
    double calculate_circumference();
};

#endif // CIRCLE_H
