class Solution:
    # Check basecase and construct array in loop (Accepted), O(n) time and space
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1]
        if n < 2:
            return nums[n]
        res = 1
        for i in range(2, n+1):
            nums.append(nums[i//2] if i %
                        2 == 0 else nums[i//2] + nums[i//2+1])
        return res

    # Simulate Process (Top Voted), O(n) time and space
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0]*(n+2)
        nums[1] = 1
        for i in range(2, n+1):
            nums[i] = nums[i//2] + nums[(i//2)+1] * (i % 2)
        return max(nums[:n+1])
