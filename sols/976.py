class Solution:
    # # Sort and Try Biggest (Accepted), O(n log n) time, O(n) space
    # def largestPerimeter(self, nums: List[int]) -> int:
    #     nums.sort(reverse=True)
    #     for i in range(len(nums)-2):
    #         tot = sum(nums[i:i+3])
    #         if nums[i] < tot - nums[i]:
    #             return tot
    #     return 0

    # Sort and Try Biggest (Top Voted), O(n log n) time, O(n) space
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)[::-1]
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
