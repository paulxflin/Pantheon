from collections import Counter


class Solution(object):
    # # Brute Force Solution (Accepted), O(n^2) time, O(n) space
    # def numIdenticalPairs(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     good = 0
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 good += 1
    #     return good

    # # Hash + Math (Accepted), O(n) time, O(n) space
    # def numIdenticalPairs(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     cnt = Counter(nums)
    #     good = 0
    #     for k, v in cnt.items():
    #         if v > 1:
    #             good += v * (v - 1) / 2
    #     return good

    # Hash + Math (Top Voted), O(n) time, O(n) space
    def numIdenticalPairs(self, nums):
        return sum(k * (k - 1) / 2 for k in collections.Counter(nums).values())
