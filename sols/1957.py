class Solution:
    # String Concat (Accepted), O(n) time and space
    def makeFancyString(self, s: str) -> str:
        cur = res = ''
        for c in s:
            if c != cur[:1]:
                res += cur
                cur = c
            elif len(cur) < 2:
                cur += c
        return res + cur

    # Join with Basecase Check (Top Voted), O(n) time and space
    def makeFancyString(self, s: str) -> str:
        cnt, a = 0, []
        for i, c in enumerate(s):
            if i > 0 and c == s[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                a.append(c)
        return ''.join(a)

    # Optimised Join (Accepted), O(n) time and space
    def makeFancyString(self, s: str) -> str:
        res, cnt = [s[0]], 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                res.append(s[i])
        return ''.join(res)
