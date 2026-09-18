/*The Hogwarts School of Witchcraft and Wizardry welcomes you! First-year students must go through the annual Sorting Ceremony.

The Sorting Hat is a talking hat at Hogwarts that magically determines which of the four school Houses each new student belongs most to:

    gryffindor
    hufflepuff
    ravenclaw
    slytherin
*/

#include <iostream>
#include <string>
using namespace std;

// Delacre four int varibles to store the points for each house
// int gryffindor = 0, hufflepuff = 0, ravenclaw = 0, slytherin = 0;
int main() {
    int gryffindor = 0, hufflepuff = 0, ravenclaw = 0, slytherin = 0;
    string answer;

//  declare another four int variables to store each of their answers 1-4
string answer1, answer2, answer3, answer4;


//add statement that tells the Muggle that they have started the quiz with the phrase "The Sorting Hat Quiz!"
    std::cout << "The Sorting Hat Quiz!\n";
    
    // Question 1
    std::cout << "Question 1: When I'm dead, I want people to remember me as:\n";
    std::cout << " (1) The Good\n";
    std::cout << " (2) The Great\n";
    std::cout << " (3) The Wise\n";
    std::cout << " (4) The Bold\n";
    cin >> answer1;
    if (answer1 == "1") {
        hufflepuff += 1;
    } else if (answer == "2") {
        slytherin += 1;
    } else if (answer == "3") {
        ravenclaw += 1;
    } else if (answer == "4") {
        gryffindor += 1;
    }
    //Question 2
    std::cout << "Question 2: Dawn or Dusk?\n";
    std::cout << " (1) Dawn\n";
    std::cout << " (2) Dusk\n";
    cin >> answer2;
    if (answer2 == "1") {
        gryffindor += 1;
        ravenclaw += 1;
    } else if (answer2 == "2") {
        hufflepuff += 1;
        slytherin += 1;
    }
    //Question 3
    std::cout << "Question 3: Which kind of instrument most pleases your ear?\n";
    std::cout << " (1) The violin\n";
    std::cout << " (2) The trumpet\n";
    std::cout << " (3) The piano\n";
    std::cout << " (4) The drum\n";
    cin >> answer3;
    if (answer3 == "1") {
        slytherin += 1;
    } else if (answer3 == "2") {
        hufflepuff += 1;
    } else if (answer3 == "3") {
        ravenclaw += 1;
    } else if (answer3 == "4") {
        gryffindor += 1;
    }
    //Question 4
    std::cout << "Question 4: Which road tempts you most?\n";
    std::cout << " (1) The wide, sunny grassy lane\n";
    std::cout << " (2) The narrow, dark, lantern-lit alley\n";
    std::cout << " (3) The twisting, leaf-strewn path through woods\n";
    std::cout << " (4) The cobbled street lined (ancient buildings)\n";
    cin >> answer4;
    if (answer4 == "1") {
        hufflepuff += 1;
    } else if (answer4 == "2") {
        slytherin += 1;
    } else if (answer4 == "3") {
        gryffindor += 1;
    } else if (answer4 == "4") {
        ravenclaw += 1;
    }
    // Determine the house with the highest points
    string house;
    int maxPoints = gryffindor;
    house = "Gryffindor";
    if (hufflepuff > maxPoints) {
        maxPoints = hufflepuff;
        house = "Hufflepuff";
    }
    if (ravenclaw > maxPoints) {
        maxPoints = ravenclaw;
        house = "Ravenclaw";
    }
    if (slytherin > maxPoints) {
        maxPoints = slytherin;
        house = "Slytherin";
    }

    // Output the result
    std::cout << "You have been sorted into " << house << "!\n";
    return 0;
}
