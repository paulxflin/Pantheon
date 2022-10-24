from itertools import zip_longest


class Solution:
    # One Pointer (Accepted), O(n+m) time and space
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l1, l2 = len(word1), len(word2)
        i = 0
        while i < l1 or i < l2:
            if i >= l1:
                return res + word2[i:]
            elif i >= l2:
                return res + word1[i:]
            else:
                res += word1[i] + word2[i]
            i += 1
        return res

    # Itertools Zip Longest (Accepted), O(n+m) time and space
    def mergeAlternately(self, w1: str, w2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(w1, w2, fillvalue=''))
