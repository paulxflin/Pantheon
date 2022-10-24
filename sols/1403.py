class Solution:
    # Reverse Sort + Sum Target + Slicing (Accepted), O(n log n) time, O(n) space
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        target = sum(nums) / 2
        s = 0
        for i in range(len(nums)):
            if s <= target:
                s += nums[i]
            else:
                return nums[:i]
        return nums

    # # Reverse Sort + sum res (Sample), O(n^2) time (without sum caching), O(n) space
    # def minSubsequence(self, nums: List[int]) -> List[int]:
    #     nums.sort(reverse=True)
    #     tot = sum(nums) / 2

    #     res = []
    #     for i in range(len(nums)):
    #         res.append(nums[i])
    #         if sum(res) > tot:
    #             return res
