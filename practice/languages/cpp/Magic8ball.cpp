/* Magic 8 Ball
The answers inside a standard Magic 8-Ball are: It is certain, It is decidedly so.
Without a doubt, Yes - definitely, You may rely on it, As I see it, yes, Most likely,
Outlook good, Yes, Signs point to yes, Reply hazy, try again., Ask again later, Better not tell you now, Cannot predict now, Concentrate and ask again, Don't count on it, My reply is no., My sources say no. , Outlook not so good, Very doubtful.
*/

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
using namespace std;

int main() {
    // Initialize the random number generator
    srand(static_cast<unsigned int>(time(0)));

    // List of Magic 8 Ball responses
    vector<string> responses = {
        "It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely",
        "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
        "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
        "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
        "Don't count on it", "My reply is no", "My sources say no",
        "Outlook not so good", "Very doubtful"
    };

    // Edge case: Check if responses list is empty
    if (responses.empty()) {
        cout << "No responses available. Please check the Magic 8 Ball configuration." << endl;
        return 1;
    }

    // Optional: Prompt user for a question
    cout << "Ask the Magic 8 Ball a yes/no question: ";
    string question;
    getline(cin, question);

    // Generate a random index to select a response
    int index = rand() % responses.size();

    // Output the selected response
    cout << "Magic 8 Ball says: " << responses[index] << endl;

    return 0;
}
// Compile with: g++ -std=c++11 Magic8ball.cpp -o Magic8ball
// Run with: ./Magic8ball
// This program simulates a Magic 8 Ball by randomly selecting and displaying one of the standard responses.



