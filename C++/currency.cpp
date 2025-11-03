// currency.cpp

// prompts the user for the amount of each foreign currency
// and converts it to US dollars
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;
int main() {
    std::string currency;
    double amount, rate;

    std::cout << "Which currency do you want to exchange? (pesos/reais/soles): ";
    std::cin >> currency;

    std::cout << "Enter the amount of " << currency << ": ";
    std::cin >> amount;

    std::cout << "Enter the current exchange rate for " << currency << " to USD: ";
    std::cin >> rate;

    double dollars = amount / rate;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << amount << " " << currency << " is $" << dollars << " USD at the current rate." << std::endl;

    return 0;
}

