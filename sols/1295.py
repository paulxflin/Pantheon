class Solution:
    # String Len (Accepted), O(n*d) time, O(d) space
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                res += 1
        return res

    # Integer Division (Accepted), O(n*d) time, O(1) space
    def findNumbers(self, nums: List[int]) -> int:
        def num_digits(n):
            digs = 0
            while n != 0:
                n //= 10
                digs += 1
            return digs
        res = 0
        for n in nums:
            if num_digits(n) % 2 == 0:
                res += 1
        return res

    # One Liner (Top Voted), O(n*d) time, O(d) space
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(n)) % 2 == 0 for n in nums)
