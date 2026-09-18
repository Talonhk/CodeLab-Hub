
#include <iostream>
#include <vector>
#include <string>

using namespace std;

double average(double num1, double num2) {
    double result;
    result = (num1 + num2) / 2;
    return result;
}

void introduction(const string& first_name, const string& last_name) {
    cout << last_name << ", " << first_name << " " << last_name << endl;
}

int tenth_power(int num) {
    int result = 1;
    for (int i = 0; i < 10; i++) {
        result *= num;
    }
    return result;
}

vector<int> first_three_multiples(int num) {
   vector<int> multiples;
   for (int i = 1; i <= 3; i++) {
       multiples.push_back(num * i);
   }
    return multiples;
}

/* Define a function needs_water() that accepts:

    First argument: An int number of days since the previous watering.
    Second argument: A bool value is_succulent. (A value of true would indicate that the plant is a succulent.)

Inside the function, you’ll need some conditional logic:

    If is_succulent is false and days is greater than 3, return "Time to water the plant.".
    If is_succulent is true and days is 12 or less, return "Don't water the plant!".
    If is_succulent is true and days is greater than or equal to 13, return "Go ahead and give the plant a little water.".
    Otherwise, return "Don't water the plant!".
/*/

string needs_water(int days, bool is_succulent) {
    if (!is_succulent && days > 3) {
        return "Time to water the plant.";
    } else if (is_succulent && days <= 12) {
        return "Don't water the plant!";
    } else if (is_succulent && days >= 13) {
        return "Go ahead and give the plant a little water.";
    } else {
        return "Don't water the plant!";
    }
}

/*Define a function is_palindrome() that takes:

    An std::string parameter text.

The function should return:

    true if text is a palindrome.
    false if text is not a palindrome.

(A palindrome is any text that has the same characters backwards as it does forwards. For example, “hannah” and “racecar” are palindromes, while “menu” and “aardvark” are not.)
*/

bool is_palindrome(const string& text) {
    size_t i = 0;
    if (text.empty()) return true;
    size_t j = text.size() - 1;
    while (i < j) {
        if (text[i++] != text[j--]) return false;
    }
    return true;
}

/*class Solution {

public:
    // Finds the smallest positive multiple of k that is missing from nums
    int missingMultiple(vector<int>& nums, int k) {
        if (k <= 0) throw invalid_argument("k must be positive");

        // store the multiplier m such that num == m * k (and m >= 1)
        unordered_set<int> seen;
        for (int num : nums) {
            if (num > 0 && num % k == 0) {
                seen.insert(num / k);
            }
        }

        // find the smallest positive integer m not in seen
        for (int m = 1; ; ++m) {
            if (seen.find(m) == seen.end()) {
                long long result = 1LL * m * k;
                if (result > numeric_limits<int>::max()) {
                    throw overflow_error("result overflow");
                }
                return static_cast<int>(result);
            }
        }
    }
};

int main() {
    Solution sol;

    vector<int> nums1 = {8, 2, 3, 4, 6};
    int k1 = 2;
    cout << "Missing multiple for nums1: " << sol.missingMultiple(nums1, k1) << endl; // Expected: 10

    vector<int> nums2 = {1, 4, 7, 10, 15};
    int k2 = 5;
    cout << "Missing multiple for nums2: " << sol.missingMultiple(nums2, k2) << endl; // Expected: 5

    return 0;
}
*/