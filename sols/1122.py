from collections import Counter


class Solution:
    # Count then append ordered (Accepted), O(A log A + B) time, O(A + B) space
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        cnt = Counter(arr1)
        for n in arr2:
            res += [n] * cnt[n]
        end = []
        s = set(arr2)
        for k in cnt:
            if k not in s:
                end += [k] * cnt[k]
        return res + sorted(end)

    # Two Liner (Top Voted), O(A log A + B) time, O(A + B) space
    def relativeSortArray(self, A: List[int], B: List[int]) -> List[int]:
        k = {b: i for i, b in enumerate(B)}
        return sorted(A, key=lambda a: k.get(a, 1000 + a))
