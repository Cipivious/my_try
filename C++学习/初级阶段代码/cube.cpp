#include <iostream>

class Cube {
public:
    double m_Height;  // Changed from m_High for clarity
    double m_Length;
    double m_Width;

    // Calculate the surface area of the cube
    double calculate_surface_area() const {
        return 2 * (m_Height * m_Length + m_Length * m_Width + m_Width * m_Height);
    }

    // Calculate the volume of the cube
    double calculate_volume() const {
        return m_Length * m_Width * m_Height;
    }

    // Check if this cube is the same as another cube
    bool is_same_by(const Cube& cube) const {
        return m_Length == cube.m_Length && m_Width == cube.m_Width && m_Height == cube.m_Height;
    }
};

int main() {
    Cube c1;
    c1.m_Width = 1;
    c1.m_Length = 2;
    c1.m_Height = 3;

    std::cout << "The surface area of c1 is: " << c1.calculate_surface_area() << std::endl;
    std::cout << "The volume of c1 is: " << c1.calculate_volume() << std::endl;

    Cube c2;
    c2.m_Width = 1;
    c2.m_Length = 2;
    c2.m_Height = 3;

    std::cout << "c1 and c2 are the same? " << (c1.is_same_by(c2) ? "Yes" : "No") << std::endl;

    return 0;
}
