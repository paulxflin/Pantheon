class Solution:
    # Brute force (Accepted), O(n) time, O(1) space
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for n in nums:
            product *= n
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0

    # Line Sweep (Top Voted), O(n) time, O(1) space
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                ans *= -1
        return ans
