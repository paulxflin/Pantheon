class Solution:
    # Find index and reverse slice (Accepted + Top Voted), O(n) time and space
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i >= 0:
            return word[:i+1][::-1] + word[i+1:]
        return word
