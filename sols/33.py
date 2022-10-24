class Solution:
    # Modified Binary Search (Accepted), O(log n) time, O(1) space
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1
        first = nums[0]
        if target == first:
            return 0

        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2

            val = nums[mid]

            if val == target:
                return mid
            elif first <= val < target or val < target < first or target < first <= val:
                low = mid + 1
            else:
                high = mid - 1

        return low if nums[low] == target else -1

    # Modified Binary Search (Revisited), O(log n) time, O(1) space
    # def search(self, nums: List[int], target: int) -> int:
    #     if not nums:
    #         return -1
    #     first, low, high = nums[0], 0, len(nums)-1
    #     while low <= high:
    #         mid = (low + high) // 2
    #         val = nums[mid]
    #         if val == target:
    #             return mid
    #         elif first<=val<target or val<target<first or target<first<=val:
    #             low = mid+1
    #         else:
    #             high = mid-1
    #     return -1

    # # Modified Binary Search (Top Voted), O(log n) time, O(1) space
    # def search(self, nums: List[int], target: int) -> int:

    #     if not nums:
    #         return -1

    #     low, high = 0, len(nums) - 1

    #     while low <= high:
    #         mid = (low + high) // 2
    #         if target == nums[mid]:
    #             return mid

    #         if nums[low] <= nums[mid]:
    #             if nums[low] <= target <= nums[mid]:
    #                 high = mid - 1
    #             else:
    #                 low = mid + 1
    #         else:
    #             if nums[mid] <= target <= nums[high]:
    #                 low = mid + 1
    #             else:
    #                 high = mid - 1

    #     return -1
