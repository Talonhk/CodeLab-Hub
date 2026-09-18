// Quadratic.cpp

// Write a C++ is a very powerful programming language for performance-critical applications that rely on speed and efficient memory management. It’s used in a wide range of industries including software and game development, robotics, microcontrollers, VR/AR, and scientific computing.
// program called quadratic.cpp that solves the quadratic equation for the x‘s:




#include <iostream>
#include <cmath>
#include <complex> // For complex roots

int main() {
    double a, b, c;
    std::cout << "Enter coefficient a: ";
    std::cin >> a;
    std::cout << "Enter coefficient b: ";
    std::cin >> b;
    std::cout << "Enter coefficient c: ";
    std::cin >> c;

    if (a == 0) {
        std::cout << "Coefficient 'a' cannot be zero." << std::endl;
        return 1;
    }

    double discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        double root1 = (-b + sqrt(discriminant)) / (2 * a);
        double root2 = (-b - sqrt(discriminant)) / (2 * a);
        std::cout << "Roots are real and different:\n";
        std::cout << "root1 = " << root1 << "\n";
        std::cout << "root2 = " << root2 << std::endl;
    } else if (discriminant == 0) {
        double root = -b / (2 * a);
        std::cout << "Roots are real and the same:\n";
        std::cout << "root1 = root2 = " << root << std::endl;
    } else {
        std::complex<double> root1((-b) / (2 * a), sqrt(-discriminant) / (2 * a));
        std::complex<double> root2((-b) / (2 * a), -sqrt(-discriminant) / (2 * a));
        std::cout << "Roots are complex and different:\n";
        std::cout << "root1 = " << root1 << "\n";
        std::cout << "root2 = " << root2 << std::endl;
    }

    return 0;
}