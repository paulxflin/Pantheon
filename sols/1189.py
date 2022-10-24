import collections
from collections import Counter


class Solution:
    # Counter + Int Div (Accepted), O(n) time and space
    def maxNumberOfBalloons(self, text: str) -> int:
        txt_c, bal_c = Counter(text), Counter('balloon')
        return min(txt_c[c] // bal_c[c] for c in bal_c)

    # Counter + Int Div (Top Voted), O(n) time and space
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)
        cntBalloon = collections.Counter('balloon')
        return min([cnt[c] // cntBalloon[c] for c in cntBalloon])
