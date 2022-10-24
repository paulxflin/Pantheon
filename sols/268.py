class Solution:
    # Create Set and remove nums, O(n) time and space
    def missingNumber(self, nums: List[int]) -> int:
        s = set(i for i in range(len(nums) + 1))
        for n in nums:
            s.remove(n)
        return next(iter(s))

    # Exp - Sum (Accepted), O(n) time, O(1) space
    def missingNumber(self, nums: List[int]) -> int:
        exp = (0 + (len(nums))) * (len(nums) + 1) // 2
        return exp - sum(nums)

    # Exp - Sum without 0 (Top Voted), O(n) time, O(1) space
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)
