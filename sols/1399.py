from collections import defaultdict


class Solution:
    # Sum Digits in Dict (Accepted), O(n) time, O(1) space
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(n):
            res = 0
            while n > 0:
                res += n % 10
                n //= 10
            return res

        d = defaultdict(int)
        for i in range(1, n+1):
            d[sum_digits(i)] += 1

        max_ = max(d.values())
        res = 0
        for i in d:
            if d[i] == max_:
                res += 1
        return res

    # Divmod with DP (Top Voted), O(n) time and space
    def countLargestGroup(self, n: int) -> int:
        dp = {0: 0}
        counts = [0] * (4 * 9)
        for i in range(1, n + 1):
            quotient, reminder = divmod(i, 10)
            dp[i] = reminder + dp[quotient]
            counts[dp[i] - 1] += 1

        return counts.count(max(counts))
