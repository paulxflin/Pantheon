from collections import Counter


class Solution(object):
    # # Counter (Hash Table), time O(n), space O(n)
    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     cnt = Counter(nums)
    #     for k, v in cnt.items():
    #         if v == 1:
    #             return k

    # # Math (Solution), time O(n + n) = O(n), space O(n + n) = O(n)
    # def singleNumber(self, nums):
    #     return 2 * sum(set(nums)) - sum(nums)

    # # Bit Manipulation (Solution), time O(n), space O(1)!
    # def singleNumber(self, nums):
    #     a = 0
    #     for i in nums:
    #         a ^= i
    #     return a
