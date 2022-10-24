class Solution:
    # Loop and Divide (Accepted), O(log n) time, O(1) space
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n != 1:
            n /= 3
            if n != int(n):
                return False
        return True

    # Two conditions (Top Voted), O(1) time and space
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 == 3**19 % n
