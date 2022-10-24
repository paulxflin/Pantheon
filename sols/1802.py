import math


class Solution:
    # Maths + Binary Search (Accepted), O(log(s)) time, O(1) space, s=maxSum
    def maxValue(self, n: int, i: int, maxSum: int) -> int:
        x = math.floor(
            (2 * maxSum - (-2 * i*i - 2*i - n*n + 2*i*n + n)) / (2*n))

        def test_hyp(x):
            s = x
            # Left Sum
            if x-i < 1:
                s += x * (x-1) / 2 + i-x+1
            else:
                s += ((x-i)+(x-1)) * i / 2

            # Right Sum
            if (x-(n-i-1)) < 1:
                s += x * (x-1) / 2 + n-i-x
            else:
                s += (x-(n-1-i) + x-1) * (n-i-1) / 2

            if s > maxSum:
                return False
            else:
                return True

        # Binary Search
        if test_hyp(x):
            return x

        low, high = 1, x
        while low < high:
            mid = (low + high + 1) // 2
            if test_hyp(mid):
                low = mid
            else:
                high = mid-1
        return low

    # Binary Search (Top Voted), O(log(s)) time, O(1) space
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) / 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) / 2
            return res - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1

    # Binary Search (Revisited), O(log(s)) time, O(1) space

    def maxValue(self, n, index, maxSum):
        def sum_hyp(x):
            a = max(0, x-index)
            total = (a + x) * (x - a + 1) / 2
            b = max(0, x-(n-1-index))
            total += (b + x) * (x-b + 1) / 2
            return total - x
        maxSum -= n
        l, r = 0, maxSum
        while l < r:
            m = (l + r + 1) // 2
            if sum_hyp(m) <= maxSum:
                l = m
            else:
                r = m - 1
        return l + 1
