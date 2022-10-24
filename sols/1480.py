class Solution(object):
    # # Sum in Place (Accepted), O(n) time, O(1) space
    # def runningSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     running_sum = 0
    #     for i in range(len(nums)):
    #         running_sum += nums[i]
    #         nums[i] = running_sum
    #     return nums

    # Use prior element (Top Voted), O(n) time, O(1) space
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
