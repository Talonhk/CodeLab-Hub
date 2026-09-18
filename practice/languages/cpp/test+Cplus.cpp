// Test C++ skills


//Create a program that takes in the weight of an item and calculates how much it will weight on Mars.
#include <iostream>
int main() {
    using namespace std;
    float weightEarth;

    cout << "Enter the weight of the item on Earth (in kg): ";
    cin >> weightEarth;

    float weightMars = weightOnMars(weightEarth);
    cout << "The weight of the item on Mars is: " << weightMars << " kg" << endl;

    // Ask for distance in miles and convert to kilometers
    float miles;
    cout << "Enter a distance in miles: ";
    cin >> miles;

    float kilometers = milesToKilometers(miles);
    cout << "The distance in kilometers is: " << kilometers << " km" << endl;

    return 0;
}
using namespace std;
 double weightOnMars(float weightEarth);
float milesToKilometers(float miles);

weightOnMars(float weightEarth) {
    const float marsGravity = 0.38; // Mars gravity relative to Earth
    return weightEarth * marsGravity;
}



// Create a progeam that asks for a distance in miles as input. The program will output that distance in kilometers
float milesToKilometers(float miles) {
    const float conversionFactor = 1.60934; // 1 mile = 1.60934 kilometers
    return miles * conversionFactor;
}
