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
