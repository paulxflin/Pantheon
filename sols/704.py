class Solution:
    # # Binary Search (Accepted), O(n) time, O(1) space
    # def search(self, nums: List[int], target: int) -> int:
    #     low, high = 0, len(nums)
    #     while low < high:
    #         mid = (low + high) // 2
    #         val = nums[mid]
    #         if val == target:
    #             return mid
    #         elif val > target:
    #             high = mid
    #         else:
    #             low = mid+1
    #     return -1

    # Binary Search (Top Voted), O(log n) time, O(1) space
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
