from collections import Counter


class Solution:
    # Find Words Appearing Once (Accepted), O(n) time and space
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter(s1.split() + s2.split())
        res = []
        for key, val in c.items():
            if val == 1:
                res.append(key)
        return res

    # Find Words Appearing Once with LC (Accepted), O(n) time and space
    def uncommonFromSentences(self, A, B):
        c = Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]
