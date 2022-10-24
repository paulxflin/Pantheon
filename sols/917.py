class Solution:
    # # One Pass, Two Pointers, if-while-while loop (Accepted), O(n) time and space
    # def reverseOnlyLetters(self, s: str) -> str:
    #     n = len(s)
    #     l, r = 0, n-1
    #     s = list(s)
    #     while l < r:
    #         if s[l].isalpha() and s[r].isalpha():
    #             s[l], s[r] = s[r], s[l]
    #             l, r = l+1, r-1
    #         while l < n and not s[l].isalpha():
    #             l += 1
    #         while r >= 0 and not s[r].isalpha():
    #             r -= 1
    #     return "".join(s)

    # # Two Pointers, One pass, while-while loop (Top Voted), O(n) time, O(n) space
    # def reverseOnlyLetters(self, S: str) -> str:
    #     i, j = 0, len(S) - 1
    #     S = list(S)
    #     while i < j:
    #         while i < j and not S[i].isalpha(): i += 1
    #         while i < j and not S[j].isalpha(): j -= 1
    #         S[i], S[j] = S[j], S[i]
    #         i, j = i + 1, j - 1
    #     return "".join(S)

    # Two Pointers, One pass, while-if loop (Top Voted), O(n) time, O(n) space
    def reverseOnlyLetters(self, S: str) -> str:
        S, i, j = list(S), 0, len(S) - 1
        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i, j = i + 1, j - 1
        return "".join(S)
