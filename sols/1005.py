class Solution:
    # # Sort + Negate Negatives + Subtract Min if Odd (Accepted), O(n log n) time, O(n) space
    # def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if k == 0:
    #             return sum(nums)
    #         elif nums[i] < 0:
    #             nums[i] = -nums[i]
    #             k -= 1
    #         else:
    #             if k % 2:
    #                 if i > 0:
    #                     return sum(nums) - 2 * min(nums[i], nums[i-1])
    #                 else:
    #                     return sum(nums) - 2 * nums[i]
    #             return sum(nums)

    # Sort + Negate Negatives + Subtract Min if Odd (Top Voted), O(n log n) time, O(n) space
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * min(A) * 2
