#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'getRemovableIndices' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. STRING str1
 *  2. STRING str2
 */

vector<int> getRemovableIndices(string str1, string str2) {
    // If the length difference between str1 and str2 is not exactly 1, return [-1]
    if (str1.length() != str2.length() + 1) {
        return {-1};
    }

    vector<int> removableIndices;

    // Iterate through str1 and try removing each character
    for (int i = 0; i < str1.length(); i++) {
        string modifiedStr1 = str1.substr(0, i) + str1.substr(i + 1); // Remove the character at index i
        if (modifiedStr1 == str2) {
            removableIndices.push_back(i); // If the modified string equals str2, add the index to the result
        }
    }

    // If no valid indices are found, return [-1]
    if (removableIndices.empty()) {
        return {-1};
    }

    return removableIndices;
}

int main()
{
    string str1;
    getline(cin, str1);

    string str2;
    getline(cin, str2);

    vector<int> result = getRemovableIndices(str1, str2);

    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i];

        if (i != result.size() - 1) {
            cout << "\n";
        }
    }

    cout << "\n";

    return 0;
}


// ------------------------------------------------------------------------------------------------------------------
#include <iostream>

int main() {
  
  int number;
  std::cout << "Enter Number 1 - 9\n";
  std::cin >> number;
  
  switch(number) {
    
    case 1 :
      std::cout << "Bulbusaur\n";
      break;
    case 2 :
      std::cout << "Ivysaur\n";
      break;
    case 3 :
      std::cout << "Venusaur\n";
      break;
    case 4 :
      std::cout << "Charmander\n";
      break;
    case 5 :
      std::cout << "Charmeleon\n";
      break;
    case 6 :
      std::cout << "Charizard\n";
      break;
    case 7 :
      std::cout << "Squirtle\n";
      break;
    case 8 :
      std::cout << "Wartortle\n";
      break;
    case 9 :
      std::cout << "Blastoise\n";
      break;
    default :
      std::cout << "Unknown\n";
      break;
  
  }
  
}



// What is Your Earth Weight
#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    double weight, earthWeight;
    cout << "Enter your weight on Earth (in kg): ";
    cin >> weight;
// Ask him to enter a number for the planet he wants to fight on.
    earthWeight = weight; // Store the weight on Earth
    cout << "Your weight on Earth: " << earthWeight << " kg" << endl;
    cout << "Choose a planet to see your weight on:\n";
    

// compute his weight on the destination planet
    cout << "1. Mercury\n";
    cout << "2. Venus\n";
    cout << "3. Mars\n";
    cout << "4. Jupiter\n";
    cout << "5. Saturn\n";
    cout << "6. Uranus\n";
    cout << "7. Neptune\n";
    cout << "Enter your choice (1-7): ";
    int choice;
    cin >> choice;
    if (choice < 1 || choice > 3) {
        cout << "Invalid choice!" << endl;
        return 1; // Exit if the choice is invalid
    }
    cout << "Calculating your weight on the selected planet...\n";
    // Display the weight on Earth
    cout << "Your weight on Earth: " << earthWeight << " kg" << endl;
    // Calculate the weight on other planets based on the choice
    if (choice == 1) {
        cout << "Your weight on Mars: " << weight * 0.38 << " kg" << endl; // Mars gravity factor
    } else if (choice == 2) {
        cout << "Your weight on Jupiter: " << weight * 2.34 << " kg" << endl; // Jupiter gravity factor
    } else if (choice == 3) {
        cout << "Your weight on the Moon: " << weight * 0.165 << " kg" << endl; // Moon gravity factor
    }
    // Display the weight on other planets
    cout << "Calculating your weight on other planets...\n";
    cout << "Your weight on Earth: " << earthWeight << " kg" << endl;
    // Display the weight on Earth
    cout << "Your weight on Mars: " << weight * 0.38 << " kg" << endl; // Mars gravity factor
    cout << "Your weight on Jupiter: " << weight * 2.34 << " kg" << endl; // Jupiter gravity factor
    cout << "Your weight on the Moon: " << weight * 0.165 << " kg" << endl; // Moon gravity factor
    // Display the weight on other planets
    cout << "Calculating your weight on other planets...\n";



    // Assuming the weight on Earth is given, calculate the weight on other planets
    double marsWeight = weight * 0.38; // Mars gravity factor
    double jupiterWeight = weight * 2.34; // Jupiter gravity factor
    double moonWeight = weight * 0.165; // Moon gravity factor

    cout << fixed << setprecision(2);
    cout << "Your weight on Mars: " << marsWeight << " kg" << endl;
    cout << "Your weight on Jupiter: " << jupiterWeight << " kg" << endl;
    cout << "Your weight on the Moon: " << moonWeight << " kg" << endl;

    return 0;
}




// ------------------------------------------------------------------------------------------------------------------
#include <iostream>

// Leap year checker
// 1. Takes a year inout
// 2. Checks to see if the year is a four-digit number
// 3. Displays whether or not the year falls on a leap year

// 3 Criteria that must be taken into account to identify a leap year:
// If the year can be evenly divided by 4 then it is a leap year, however
// if that year can be evenly didvided by 100, and it is not evenly divieded by 400, then it is NOT a leap year.
// if that year is evenly dixisible by 400, then it is a leap year.
int main() {
    int year;
    std::cout << "Enter a year: ";
    std::cin >> year;

    // Check if the year is a four-digit number
    if (year < 1000 || year > 9999) {
        std::cout << "Please enter a four-digit year." << std::endl;
        return 1; // Exit if the input is not a four-digit number
    }

    // Check for leap year conditions
    else if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        std::cout << year << " is a leap year." << std::endl;
    } else {
        std::cout << year << " is not a leap year." << std::endl;
    }

    return 0;
}
// ------------------------------------------------------------------------------------------------------------------
#include <iostream>




// Square Numebers

#include <iostream>

int main() {

    int i =0;
    int square = 0;

    while (i < 10) {
        
        square = i * i;
        std::cout << "The square of " << i << " is " << square << std::endl;
        i++;
        
    }
}


// ------------------------------------------------------------------------------------------------------------------
#include <iostream>
#include <vector>


/*Write a program to find the sum of even numbers and the product of odd numbers in a vector.

For example:

Suppose we have a vector that is {2, 4, 3, 6, 1, 9}.

Then the program should output: 
Sum of even numbers is 12
Product of odd numbers is 27
/*/

int main() {

    
    int sumEven = 0;
    int productOdd = 1;

    std::vector<int> numbers = {2, 4, 3, 6, 1, 9};

    bool hasOdd = false; // To check if there are any odd numbers

    for (int num : numbers) {
        if (num % 2 == 0) {
            sumEven += num; // Sum even numbers
        } else {
            productOdd *= num; // Product of odd numbers
            hasOdd = true; // Mark that we have at least one odd number
        }
    }

    std::cout << "Sum of even numbers is " << sumEven << std::endl;
    if (hasOdd) {
        std::cout << "Product of odd numbers is " << productOdd << std::endl;
    } else {
        std::cout << "No odd numbers in the vector." << std::endl;
    }

    return 0;
}

// ------------------------------------------------------------------------------------------------------------------

/* Takes a phrase like "turpentine and turtles" and translate it into its “whale talk” equivalent, "uueeieeauuee".

There are a few simple rules for translating text to whale language:

    There are no consonants. Only vowels excluding the letter y.
    The u‘s and e‘s are extra long, so we must double them.

Once we have converted text to the whale language, the result is sung slowly, as is custom in the ocean.

Write a whale.cpp program that accomplishes this translation using loops and vectors. 4*/

#include <iostream>
#include <vector>
#include <string>

int main() {
    std::string input = "turpentine and turtles";
    std::string vowels = "aeiou";
    std::vector<char> result;

    for (char c : input) {
        // Check if the character is a vowel
        if (vowels.find(c) != std::string::npos) {
            // Double 'u' and 'e'
            if (c == 'u' || c == 'e') {
                result.push_back(c);
            }
            result.push_back(c);
        }
    }

    // Output the whale talk
    for (char c : result) {
        std::cout << c;
    }
    std::cout << std::endl;

    return 0;
}


// ------------------------------------------------------------------------------------------------------------------
#include <iostream>
#include <cstdlib>


int main() {
    
    //This seeds the random Number generator
    srand (time(NULL));

    // use rand() below to initialize the_amazing_random_number

    int the_amazing_random_number = rand() % 29;

    std::cout << "The amazing random number is: " << the_amazing_random_number << "\n";

}


// Define oscar_wilde_quote() below:

void oscar_wilde_quote() {
    std::cout << "Be yourself; everyone else is already taken. - Oscar Wilde\n";
}

int main() {
  
  // Call your function here:
  return oscar_wilde_quote();
  
}


// ------------------------------------------------------------------------------------------------------------------
#include <iostream>

// Define get_emergency_number() below:

void get_emergency_number(std::string emergency_number) {
    std::cout << "For emergencies, dial: " << emergency_number << "\n";
  
}

int main() {
  
  // Original emergency services number 
  std::string old_emergency_number = "999";
  
  // For nicer ambulances, faster response times
  // and better-looking drivers
  std::string new_emergency_number = "0118 999 881 999 119 725 3";
  
  // Call get_emergency_number() below with
  // the number you want!
 get-emergency_number(new_emergency_number);


// ------------------------------------------------------------------------------------------------------------------

#include <iostream>
#include <string>

// Define name_x_times() below: string name , integer x

void name_x_times(std::string name, int x) {
    //create a while loop that will run as long as x is greater than 0. 
    //Inside the loop, print the name and decrement x by 1.
    while (x > 0) {
        std::cout << name << "\n";
        x--;

}

int main() {
  
  std::string my_name = "Add your name here!";
  int some_number = 5; // Change this if you like!
  // Call name_x_times() below with my_name and some_number
  
  // Now, call name_x_times() in main() with my_name and some_number as arguments. 
    name_x_times(my_name, some_number);
    return 0;
}

