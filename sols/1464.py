class Solution:
    # Store Max 2 (Accepted + Top Voted), O(n) time, O(1) space
    def maxProduct(self, nums: List[int]) -> int:
        a = b = -float('inf')
        for n in nums:
            if n > a:
                b = a
                a = n
            elif n > b:
                b = n
        return (a-1) * (b-1)
