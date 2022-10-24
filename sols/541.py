class Solution:
    # Three pointers + Swap Reverse (Accepted), O(n) time and space
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        cur = l = 0
        a = list(s)

        while cur < n:
            l = cur
            r = min(l + k - 1, n-1)
            while l < r:
                a[l], a[r] = a[r], a[l]
                l, r = l+1, r-1
            cur += 2*k

        return "".join(a)

    # Slice assignment with inbuilt reverse (Solution), O(n) time and space
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)

    # Slice assignment with slicing reverse (Solution), O(n) time and space
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = a[i:i+k][::-1]
        return "".join(a)
