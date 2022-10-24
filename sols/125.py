import re


class Solution:
    # Regular Expressions (Accepted), O(n) time and space
    def isPalindrome(self, s: str) -> bool:
        A = re.findall("[a-z0-9]", s.lower())
        return A == A[::-1]

    # Two Pointers if-elif-else (Accepted), O(n) time, O(1) space
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if l < r and not s[l].isalnum():
                l += 1
            elif l < r and not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True

    # Two Pointers Nested-While (Top Voted), O(n) time, O(1) space
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
