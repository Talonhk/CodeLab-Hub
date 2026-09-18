#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    std::srand(static_cast<unsigned int>(std::time(0)));
    int secret = std::rand() % 100 + 1; // Random number between 1 and 100
    int guess;
    int attempts = 0;

    std::cout << "Guess the number (between 1 and 100): ";

    do {
        std::cin >> guess;
        attempts++;
        if (guess < secret) {
            std::cout << "Too low. Try again: ";
        } else if (guess > secret) {
            std::cout << "Too high. Try again: ";
        }
    } while (guess != secret);

    std::cout << "Congratulations! You guessed the number in " << attempts << " attempts." << std::endl;
    return 0;
}