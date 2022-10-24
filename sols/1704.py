class Solution:
    # Add half deduct half (Accepted), O(n) time, O(1) space
    def halvesAreAlike(self, s: str) -> bool:
        res, split = 0, len(s)//2

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for c in s[:split]:
            if c in vowels:
                res += 1

        for c in s[split:]:
            if c in vowels:
                res -= 1

        return res == 0

    # Check Equality with Set (Top Voted), O(n) time, O(1) space
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        a = b = 0
        i, j = 0, len(s) - 1
        while i < j:
            a += s[i] in vowels
            b += s[j] in vowels
            i += 1
            j -= 1
        return a == b
