class Solution:
    # Enumerate (Accepted), O(n) time, O(1) space
    def smallestEqual(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i % 10 == n:
                return i
        return -1

    # One Liner (Top Voted), O(n) time, O(1) space
    def smallestEqual(self, nums: List[int]) -> int:
        return next((i for i, x in enumerate(nums) if i % 10 == x), -1)
