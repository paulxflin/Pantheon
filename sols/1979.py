class Solution:
    # One Pass find min/max + Eucliean (Accepted), O(n + log(min(a,b))) time, O(1) space
    def findGCD(self, nums: List[int]) -> int:
        a, b = float('inf'), -float('inf')
        for n in nums:
            if n < a:
                a = n
            if n > b:
                b = n

        r = a % b
        while r != 0:
            a, b = b, r
            r = a % b
        return b

    # Euclidean (Accepted), O(n + log(min(a,b))) time, O(1) space
    def findGCD(self, nums: List[int]) -> int:
        a, b = max(nums), min(nums)
        r = a % b
        while r != 0:
            a, b = b, r
            r = a % b
        return b

    # Euclidean (Top Voted), O(n + log(min(a,b))) time, O(1) space
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        while a:
            a, b = b % a, a
        return b
