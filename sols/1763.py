class Solution:
    # # Brute Force (Accepted), O(n! * n) time, O(n) space
    # def longestNiceSubstring(self, s: str) -> str:
    #     def is_nice(substr):
    #         subset = set(substr)
    #         for s in subset:
    #             if (s.islower() and s.upper() not in subset) or (s.isupper() and s.lower() not in subset):
    #                 return False
    #         return True

    #     n = len(s)
    #     for l in range(n, 0, -1):
    #         for i in range(n-l+1):
    #             substr = s[i:i+l]
    #             if is_nice(substr):
    #                 return substr

    #     return ''

    # Recursive Set + Swapcase (Top Voted), O(n^2) time, O(n) space
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ""  # boundary condition
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss:
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s
