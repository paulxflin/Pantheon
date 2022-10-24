import bisect


class Solution:
    # # Binary search with Bisect Check (Accepted), O((log n)^2) time, O(1) space
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     low, high = 1, len(arr) + k
    #     while low < high:
    #         mid = (low + high) // 2
    #         if mid - bisect.bisect_right(arr, mid) < k:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return low

    # Binary Search (Top Voted), O(log n) time, O(1) space
    def findKthPositive(self, A: List[int], k: int) -> int:
        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if A[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k
