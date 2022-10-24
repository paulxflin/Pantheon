from collections import Counter


class Solution:
    # Counter (Accepted + Top Voted), O(n) time and space
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        return len(set(cnt.values())) == len(cnt)
