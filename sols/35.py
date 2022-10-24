import bisect


class Solution:
    # Bisect Binary Search (Accepted + Top Voted), O(log n) time, O(1) space
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
