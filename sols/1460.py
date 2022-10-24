from collections import Counter


class Solution:
    # Sort (Accepted + Top Voted), O(n log n) time, O(n) space
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

    # Counter (Accepted + Top Voted), O(n) time and space
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
