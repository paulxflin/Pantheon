class Solution:
    # # Inplace Dynamic Programming / Kandane's (Accepted), O(n) time, O(1) space
    # def maxSubArray(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     res = nums[0]
    #     for i in range(1, len(nums)):
    #         nums[i] = max(nums[i], nums[i] + nums[i-1])
    #         res = nums[i] if nums[i] > res else res
    #     return res

    # # Kadane's Algorithm (Top Voted), O(n) time, O(1) space
    # def maxSubArray(self, nums: List[int]) -> int:
    #     for i in range(1, len(nums)):
    #         if nums[i-1] > 0:
    #             nums[i] += nums[i-1]
    #     return max(nums)

    # # Divide and Conquer (Accepted), O(n) time, O(log n) space
    # def maxSubArray(self, nums: List[int]) -> int:

    #     def divide_and_conquer(low, high):
    #         if low == high:
    #             return nums[low], nums[low], nums[low], nums[low]

    #         mid = low + (high - low)//2
    #         r1, l1, o1, s1 = divide_and_conquer(low, mid)
    #         r2, l2, o2, s2 = divide_and_conquer(mid + 1, high)

    #         # Right inclusive max
    #         ri_max = max(r2, r1+s2)

    #         # Left inclusive max
    #         li_max = max(l1, s1+l2)

    #         # Overall max
    #         o_max = max(o1, o2, r1+l2)

    #         # Sum
    #         s = s1+s2

    #         return ri_max, li_max, o_max, s

    #     if not nums:
    #         return 0
    #     _, _, res, _ = divide_and_conquer(0, len(nums)-1)
    #     return res

    # Divide and Conquer (Top Voted), O(n) time, O(log n) space
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_and_conquer(nums, i, j):
            if i == j-1:
                return nums[i], nums[i], nums[i], nums[i]

            # we will compute :
            # a which is max contiguous sum in nums[i:j] including the first value
            # m which is max contiguous sum in nums[i:j] anywhere
            # b which is max contiguous sum in nums[i:j] including the last value
            # s which is the sum of all values in nums[i:j]

            # compute middle index to divide array in two halves
            i_mid = i+(j-i)//2

            # compute a, m, b, s for left half
            a1, m1, b1, s1 = divide_and_conquer(nums, i, i_mid)

            # compute a, m, b, s for right half
            a2, m2, b2, s2 = divide_and_conquer(nums, i_mid, j)

            # combine a, m, b, s values from left and right halves to form a, m, b, s for whole array (bottom up)
            a = max(a1, s1+a2)
            b = max(b2, s2+b1)
            m = max(m1, m2, b1+a2)
            s = s1+s2
            return a, m, b, s

        _, m, _, _ = divide_and_conquer(nums, 0, len(nums))
        return m
