import re


class Solution:
    # Regex check each case (Accepted), O(n) time and space
    def reformat(self, s: str) -> str:
        letters, digits = re.findall('[a-z]', s), re.findall('[0-9]', s)
        res = ''
        if abs(len(letters)-len(digits)) <= 1:
            if len(letters) == len(digits):
                for i in range(len(letters)):
                    res += letters[i] + digits[i]
            elif len(letters) > len(digits):
                for i in range(len(digits)):
                    res += letters[i] + digits[i]
                res += letters[len(letters)-1]
            else:
                for i in range(len(letters)):
                    res += digits[i] + letters[i]
                res += digits[len(digits)-1]
        return res

    # Simple (Top Voted), O(n) time and space
    def reformat(self, s: str) -> str:
        a, b = [], []
        for c in s:
            if 'a' <= c <= 'z':
                a.append(c)
            else:
                b.append(c)
        if len(a) < len(b):
            a, b = b, a
        if len(a) - len(b) >= 2:
            return ''
        ans = ''
        for i in range(len(a)+len(b)):
            if i % 2 == 0:
                ans += a[i//2]
            else:
                ans += b[i//2]
        return ans

    # Optimised Simple (Accepted + Top Voted), O(n) time and space
    def reformat(self, s: str) -> str:
        a, b = re.findall('[a-z]', s), re.findall('[0-9]', s)
        if len(a) < len(b):
            a, b = b, a
        if len(a) - len(b) >= 2:
            return ''
        ans = ''
        for i in range(len(s)):
            if i % 2 == 0:
                ans += a[i//2]
            else:
                ans += b[i//2]
        return ans
