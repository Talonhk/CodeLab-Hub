# class Solution:
#    def runningSum(self, nums: List[int]) -> List[int]:
#        for i in range(1, len(nums)):
#            nums[i] += nums[i - 1]
#        return nums


# Constraints (for reference only, not executable code)
# m == accounts.length
# n == accounts[i].length
# 1 <= m, n <= 50
# 1 <= accounts[i][j] <= 100

# Python
#class Solution:
#    def maximumWealth(self, accounts: list[list[int]]) -> int:
#        max_wealth = 0
#        for account in accounts:
#            current_wealth = sum(account)
#            if current_wealth > max_wealth:
#                max_wealth = current_wealth
#        return max_wealth

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps
