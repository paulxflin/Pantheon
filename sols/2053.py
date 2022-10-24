class Solution:
    # Counter (Accepted), O(n) time and space
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        for s in arr:
            if cnt[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ""

    # Three Liner (Top Voted), O(n) time and space
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        arr = [s for s in arr if c[s] == 1]
        return k <= len(arr) and arr[k-1] or ''
