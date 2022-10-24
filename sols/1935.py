class Solution:
    # Split + Set + Any (Accepted), O(n) time and space
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = len(words)
        broken_set = set(brokenLetters)
        for word in words:
            if any(c in broken_set for c in word):
                res -= 1
        return res

    # Set + Split + All (Top Voted), O(n) time and space
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        no, cnt = set(brokenLetters), 0
        for word in text.split():
            if all(c not in no for c in word):
                cnt += 1
        return cnt
