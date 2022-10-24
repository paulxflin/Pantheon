class Solution:
    # Max 2 Ops (Accepted), O(n) time and space
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        else:
            return 2

    # # Max 2 Ops (Top voted), O(n) time and space
    # def removePalindromeSub(self, s: str) -> int:
    #     return 2 - (s == s[::-1]) - (s == "")
