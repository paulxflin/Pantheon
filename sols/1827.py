class Solution:
    # Greedy with Base Cases (Accepted), O(n) time, O(1) space
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        exp = nums[0] + 1
        res = 0
        for i in range(1, n):
            if nums[i] < exp:
                diff = exp - nums[i]
                res += diff
                exp += 1
            else:
                exp = nums[i] + 1
        return res

    # Greedy (Top Voted), O(n) time, O(1) space
    def minOperations(self, nums: List[int]) -> int:
        cnt = prev = 0
        for cur in nums:
            if cur <= prev:
                prev += 1
                cnt += prev - cur
            else:
                prev = cur
        return cnt
