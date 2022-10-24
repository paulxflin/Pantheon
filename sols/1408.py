class Solution:
    # Sorted Brute Force (Accepted), O(w log w + w^2) time, O(w) space
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len, reverse=True)
        res = []
        for i in range(len(words)):
            if any(words[i] in w for w in words[:i]):
                res.append(words[i])
        return res

    # Build sentence + string.Count (Top Voted), O(w * s), O(w) space, s=len(arr)
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = ' '.join(words)
        subStr = [i for i in words if arr.count(i) >= 2]
        return subStr
