import bisect


class Solution:
    # # Binary Search with Bisect (Accepted), O(n log n + (log n)^2) time, O(n) space
    # def specialArray(self, nums: List[int]) -> int:
    #     high = n = len(nums)
    #     nums.sort()
    #     low = 0
    #     while low < high:
    #         mid = (low + high) // 2
    #         if n-bisect.bisect_left(nums, mid) > mid:
    #             low = mid+1
    #         else:
    #             high = mid
    #     return low if n-bisect.bisect_left(nums, low) == low else -1

    # Reverse Sort Binary Search (Top Voted), O(n log n) time, O(n) space
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return -1 if left < len(nums) and left == nums[left] else left
