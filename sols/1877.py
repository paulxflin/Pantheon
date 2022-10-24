class Solution:
    # Min + Max (Accepted), O(n log n) time, O(n) space
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = None
        while l < r:
            s = nums[l] + nums[r]
            res = s if not res or res < s else res
            l += 1
            r -= 1
        return res

    # # Min + Max (Top Voted), O(sort) time and space
    # def minPairSum(self, A: List[int]) -> int:
    #     return max(a + b for a, b in zip(sorted(A), sorted(A)[::-1]))
