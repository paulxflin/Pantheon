class Solution:
    # Two Pointers + Prev (Accepted), O(n) time, O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        prev = None
        while r < len(nums):
            if nums[r] != prev:
                nums[l] = prev = nums[r]
                l += 1
            r += 1
        return l

    # Two Pointers (Sample), O(n) time, O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i = i + 1
        return i
