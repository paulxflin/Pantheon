class Solution(object):
    # # Backtracking (Top Voted), O(2^n) time, O(n) space
    # def subsetXORSum(self, nums):
    #     def go(i = 0, x = 0):
    #         if i == len(nums):
    #             return x
    #         include = go(i + 1, x ^ nums[i])
    #         exclude = go(i + 1, x)
    #         return include + exclude
    #     return go()

    # Bitwise approach (Top Voted), O(n) time, O(1) space
    def subsetXORSum(self, nums):
        bits = 0
        for a in nums:
            bits |= a
        return bits * int(pow(2, len(nums)-1))
