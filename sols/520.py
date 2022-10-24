class Solution:
    # Python Inbuilts (Accepted + Top Voted), O(n) time, O(1) space
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()

    # Count Capitalised (Top Voted), O(n) time, O(1) space
    def detectCapitalUse(self, word: str) -> bool:
        c = 0
        for i in word:
            if i == i.upper():
                c += 1
        return c == len(word) or (c == 1 and word[0] == word[0].upper()) or c == 0
