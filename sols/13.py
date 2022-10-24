class Solution:
    # Check Cases with Slice (Accepted), O(n) time, O(1) space
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in ('IV', 'IX', 'XL', 'XC', 'CD', 'CM'):
                res += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                res += d[s[i]]
                i += 1
        return res

    # Subtract smaller if before larger (Top Voted), O(n) time, O(1) space
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
