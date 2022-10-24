class Solution:
    # One pass find right (Accepted), O(n) time and space
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l, r = -float("inf"), s.find(c)
        ans = []
        for i in range(len(s)):
            if i == r:
                l = r
                r = s.find(c, r+1)
            if r == -1:
                ans.append(i-l)
            else:
                ans.append(min(i-l, r-i))
        return ans

    # Two pass (Top Voted), O(n) time and space
    def shortestToChar(self, S, C):
        n, pos = len(S), -float('inf')
        res = [n] * n
        for i in list(range(n)) + list(range(n)[::-1]):
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res
