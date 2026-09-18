//Let's Play rock paper scissors

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

int main() {
    // Live long and prosper

    std::string choices[3] = {"rock", "paper", "scissors"};
    std::string userChoice;
    std::string computerChoice;

    // Seed the random number generator
    std::srand(static_cast<unsigned int>(std::time(0)));

    // Get user's choice
    std::cout << "Enter rock, paper, or scissors: ";
    std::cin >> userChoice;

    // Generate computer's choice
    int randomIndex = std::rand() % 3;
    computerChoice = choices[randomIndex];

    std::cout << "Computer chose: " << computerChoice << std::endl;

    // Determine the winner
    if (userChoice == computerChoice) {
        std::cout << "It's a tie!" << std::endl;
    } else if ((userChoice == "rock" && computerChoice == "scissors") ||
               (userChoice == "paper" && computerChoice == "rock") ||
               (userChoice == "scissors" && computerChoice == "paper")) {
        std::cout << "You win!" << std::endl;
    } else if ((userChoice == "rock" && computerChoice == "paper") ||
               (userChoice == "paper" && computerChoice == "scissors") ||
               (userChoice == "scissors" && computerChoice == "rock")) {
        std::cout << "Computer wins!" << std::endl;
    } else {
        std::cout << "Invalid input. Please enter rock, paper, or scissors." << std::endl;
    }

    return 0;
}