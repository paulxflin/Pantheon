class Solution:
    # # Binary Search (Accepted), O(log n) time, O(1) space
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     low, high = 0, len(arr)-1
    #     while low < high:
    #         mid = (low + high) // 2

    #         if arr[mid - 1] < arr[mid] > arr[mid + 1]:
    #             return mid
    #         elif arr[mid-1] < arr[mid]:
    #             low = mid + 1
    #         else:
    #             high = mid

    # # Binary Search (Top Voted), O(log n) time, O(1) space
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     l, r = 0, len(arr) - 1
    #     while l < r:
    #         m = (l + r) // 2
    #         if arr[m] < arr[m + 1]:
    #             l = m + 1
    #         else:
    #             r = m
    #     return l

    # Golden Section Seach (Top Voted), O(log n) time, O(1) space
    def peakIndexInMountainArray(self, A):
        def gold1(l, r):
            return l + int(round((r - l) * 0.382))

        def gold2(l, r):
            return l + int(round((r - l) * 0.618))
        l, r = 0, len(A) - 1
        x1, x2 = gold1(l, r), gold2(l, r)
        while x1 < x2:
            if A[x1] < A[x2]:
                l = x1
                x1 = x2
                x2 = gold1(x1, r)
            else:
                r = x2
                x2 = x1
                x1 = gold2(l, x2)
        return A.index(max(A[l:r + 1]), l)
