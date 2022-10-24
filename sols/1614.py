class Solution:
    # Count Open Paren (Accepted), O(n) time, O(1) space
    def maxDepth(self, s: str) -> int:
        cnt = 0
        res = cnt
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            if cnt > res:
                res = cnt
        return res

    # Count Open Paren (Top Voted), O(n) time, O(1) space
    def maxDepth(self, s: str) -> int:
        res = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                res = max(res, cur)
            if c == ')':
                cur -= 1
        return res
