//Let's Play rock paper scissors Lizard Spock

#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    std::string choices[] = {"rock", "paper", "scissors", "lizard", "spock"};
    std::string userChoice;
    std::string computerChoice;
    
    // Initialize random seed
    std::srand(static_cast<unsigned int>(std::time(0)));
    
    // Get user input
    std::cout << "Enter rock, paper, scissors, lizard, or spock: ";
    std::cin >> userChoice;
    
    // Validate user input
    bool validInput = false;
    for (const auto& choice : choices) {
        if (userChoice == choice) {
            validInput = true;
            break;
        }
    }
    
    if (!validInput) {
        std::cout << "Invalid choice. Please choose rock, paper, scissors, lizard, or spock." << std::endl;
        return 1;
    }
    
    // Generate computer choice
    computerChoice = choices[std::rand() % 5];
    
    // Display choices
    std::cout << "You chose: " << userChoice << std::endl;
    std::cout << "Computer chose: " << computerChoice << std::endl;
    
    // Determine winner
    if (userChoice == computerChoice) {
        std::cout << "It's a tie!" << std::endl;
    } else if ((userChoice == "rock" && (computerChoice == "scissors" || computerChoice == "lizard")) ||
               (userChoice == "paper" && (computerChoice == "rock" || computerChoice == "spock")) ||
               (userChoice == "scissors" && (computerChoice == "paper" || computerChoice == "lizard")) ||
               (userChoice == "lizard" && (computerChoice == "spock" || computerChoice == "paper")) ||
               (userChoice == "spock" && (computerChoice == "scissors" || computerChoice == "rock"))) {
        std::cout << "You win!" << std::endl;
    } else {
        std::cout << "Computer wins!" << std::endl;
    }
    
    return 0;
}