class Solution:
    # Binary Search (Accepted + Top Voted), O(log n) time, O(1) space
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low < high:
            mid = (low + high + 1) // 2

            if mid * mid <= x:
                low = mid
            else:
                high = mid - 1

        return low if low * low <= x else -1
