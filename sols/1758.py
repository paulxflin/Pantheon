class Solution:
    # Set exp and take min of missed exp (Accepted), O(n) time, O(1) space
    def minOperations(self, s: str) -> int:
        exp = ans = 0
        for c in s:
            if int(c) != exp:
                ans += 1
            exp = (exp+1) % 2
        return min(ans, len(s)-ans)

    # Easy and Concise Enumerate (Top Voted), O(n) time, O(1) space
    def minOperations(self, s: str) -> int:
        res = sum(i % 2 == int(c) for i, c in enumerate(s))
        return min(res, len(s) - res)
