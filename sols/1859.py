class Solution:
    # Split, Sort, Join (Accepted), O(n log n) time and space
    def sortSentence(self, s: str) -> str:
        li = s.split()
        li.sort(key=lambda s: int(s[-1:]))
        return " ".join(map(lambda s: s[:-1], li))

    # Split, build list, then join (Top Voted), O(n) time and space
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ans = [None] * len(words)
        for word in words:
            ans[int(word[-1]) - 1] = word[: -1]
        return ' '.join(ans)
