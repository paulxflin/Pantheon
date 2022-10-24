class Solution:
    # One Liner (Accepted + Top Voted), O(n) time, O(1) space
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums) - min(nums) - 2 * k, 0)
