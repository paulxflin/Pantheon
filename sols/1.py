class Solution(object):
    # Brute Force (Accepted), time O(n^2), space O(1)
    # def twoSum(self, nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """

    # One pass Hash Table (Solution), time O(n), space O(n)
    # def twoSum(self, nums, target):
    #     num_dict = {}
    #     for k, v in enumerate(nums):
    #         num_dict[v] = k
    #     for i in range(len(nums)):
    #         complement = target - nums[i]
    #         if complement in num_dict and num_dict[complement] != i:
    #             return [i, num_dict[complement]]

    # Two Pass Hash Table, time O(n), space O(n)
    def twoSum(self, nums, target):
        num_dict = {}
        for k, v in enumerate(nums):
            complement = target - v
            if complement in num_dict and num_dict[complement] != k:
                return [num_dict[complement], k]
            num_dict[v] = k
