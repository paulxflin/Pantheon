class Solution:
    # One pass while loops (Accepted), O(n) time, O(1) space
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ep, op, n = 0, 1, len(nums)
        while ep < n and op < n:
            if nums[ep] % 2 == 1 and nums[op] % 2 == 0:
                nums[ep], nums[op] = nums[op], nums[ep]
            while ep < n and nums[ep] % 2 == 0:
                ep += 2
            while op < n and nums[op] % 2 == 1:
                op += 2
        return nums

    # One pass if, elif, else (Top Voted), O(n) time, O(1) space
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ep, op, n = 0, 1, len(nums)
        while ep < n and op < n:
            if nums[ep] % 2 == 0:
                ep += 2
            elif nums[op] % 2 == 1:
                op += 2
            else:
                nums[ep], nums[op] = nums[op], nums[ep]
                ep += 2
                op += 2
        return nums
