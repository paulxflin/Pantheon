class Solution:
    # # Sort then access with stride 2 (Accepted), O(n log n) time, O(n) space
    # def arrayPairSum(self, nums: List[int]) -> int:
    #     nums.sort()
    #     res = i = 0
    #     while i < len(nums):
    #         res += nums[i]
    #         i += 2
    #     return res

    # One liner stepped slicing (Top Voted), O(n log n) time, O(n) space
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
