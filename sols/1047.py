class Solution:
    # Two pointers with backstep (Accepted), O(n) time and space
    def removeDuplicates(self, s: str) -> str:
        i = 0
        while i+1 < len(s):
            if s[i] == s[i+1]:
                l, r = i-1, i+2
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l, r = l-1, r+1
                s = s[:l+1] + s[r:]
                i = l+1
            else:
                i += 1
        return s

    # Stack Solution (Top Voted), O(n) time and space
    def removeDuplicates(self, S):
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)
