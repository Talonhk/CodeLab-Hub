/*
You are given an integer array nums and an integer k.

Return the sum of all elements in nums whose TOTAL FREQUENCY in the
array is divisible by k. Each element contributes value * frequency
to the sum, but is only included when the element's frequency % k == 0.

Example:
  nums = {1,2,2,3,3,3,4,4,4,4}, k = 2
  frequencies: 1->1, 2->2, 3->3, 4->4
  include 2 (2*2) and 4 (4*4) because 2%2==0 and 4%2==0 => sum = 4 + 16 = 20
*/

#include <iostream>
#include <vector>
#include <stdexcept>
#include <unordered_map>


using namespace std;

class Solution {
public:
    int sumDivisibleByK(vector<int>& nums, int k) {
        if (k <= 0) {
            throw invalid_argument("k must be positive.");
        }

        if (nums.empty()) return 0;

        unordered_map<int,int> freq;
        for (int num : nums) ++freq[num];

        int sum = 0;
        for (const auto &p : freq) {
            int value = p.first;
            int count = p.second;
            if (count % k == 0) {
                sum += value * count;
            }
        }
        return sum;
    }
};


