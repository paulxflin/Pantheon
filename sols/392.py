class Solution:
    # # Two Pointers (Accepted), O(t) time, O(1) space
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     if not s:
    #         return True
    #     elif not t:
    #         return False

    #     if len(t) < len(s):
    #         return False
    #     i = 0
    #     j = 0
    #     while j < len(t):
    #         if s[i] == t[j]:
    #             i += 1
    #         if i == len(s):
    #             return True
    #         j += 1
    #     return False

    # # Iterator (Top Voted), O(t) time, O(1) space
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     t = iter(t)
    #     return all(c in t for c in s)

    # Explicit Iterator (Top Voted), O(t) time, O(1) space
    def isSubsequence(self, s, t):
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True
