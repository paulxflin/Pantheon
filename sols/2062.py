class Solution:
    # Brute Force (Accepted), O(n^2) time, O(1) space
    def countVowelSubstrings(self, word: str) -> int:
        res = 0
        vowels = set('aeiou')
        for l in range(5, len(word)+1):
            for i in range(len(word)+1-l):
                if set(word[i:i+l]) == vowels:
                    res += 1
        return res

    # One Pass (Top Voted), O(n) time, O(1) space
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        ans, last_consonant = 0, -1
        last_seen_vowels = {v: -2 for v in vowels}
        for i, x in enumerate(word):
            if x not in vowels:
                last_consonant = i
            else:
                last_seen_vowels[x] = i
                ans += max(min(last_seen_vowels.values())-last_consonant, 0)
        return ans
