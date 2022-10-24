class Solution:
    # Split + Slice (Accepted), O(n) time and space
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words, n = sentence.split(), len(searchWord)
        for i in range(len(words)):
            if words[i][:n] == searchWord:
                return i+1
        return -1

    # Split + Enumerate + Startswith (Top Voted), O(n) time and space
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, w in enumerate(sentence.split(' '), 1):
            if w.startswith(searchWord):
                return i
        return -1
