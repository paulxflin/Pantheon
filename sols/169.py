from collections import Counter


class Solution(object):
    # # Counter/Hashmap (Accepted), Time O(n), Space O(n)
    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     cnt = Counter(nums)
    #     maj = len(nums) / 2
    #     for k, v in cnt.items():
    #         if v > maj:
    #             return k

    # # Sorting (Solution), Time O(n log n), Space O(n)
    # def majorityElement(self, nums):
    #     nums.sort()
    #     return nums[len(nums)//2]

    # # Divide and Conquer (Solution), Time O(n log n), Space O(log n)
    # def majorityElement(self, nums, lo=0, hi=None):
    #     def majority_element_rec(lo, hi):
    #         # base case; the only element in an array of size 1 is the majority
    #         # element.
    #         if lo == hi:
    #             return nums[lo]

    #         # recurse on left and right halves of this slice.
    #         mid = (hi-lo)//2 + lo
    #         left = majority_element_rec(lo, mid)
    #         right = majority_element_rec(mid+1, hi)

    #         # if the two halves agree on the majority element, return it.
    #         if left == right:
    #             return left

    #         # otherwise, count each element and return the "winner".
    #         left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
    #         right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

    #         return left if left_count > right_count else right

    #     return majority_element_rec(0, len(nums)-1)

    # Boyer-Moore Voting Algorithm (Best Solution), Time O(n), Space O(1)
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
