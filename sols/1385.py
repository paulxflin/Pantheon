import bisect


class Solution:
    # # Sort + Binary Search (Accepted), O((n + m) log m) time, O(n) space
    # def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    #     res = 0
    #     arr2.sort()
    #     for n in arr1:
    #         ind = bisect.bisect_left(arr2, n)
    #         if ind > 0 and ind < len(arr2):
    #             if abs(n - arr2[ind]) > d and abs(n - arr2[ind-1]) > d:
    #                 res += 1
    #         elif ind == 0 and abs(n - arr2[0]) > d:
    #             res += 1
    #         elif ind == len(arr2) and abs(n - arr2[ind-1]) > d:
    #             res += 1

    #     return res

    # Sort + Binary Search (Accepted), O((n + m) log m) time, O(n) space
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        arr2.sort()
        m = len(arr2)
        for n in arr1:
            ind = bisect.bisect_left(arr2, n)
            if not (ind > 0 and abs(n - arr2[ind-1]) <= d or ind < m and abs(n - arr2[ind]) <= d):
                res += 1
        return res

    # # One Liner (Top Voted), O(m * n) time, O(1) space
    # def findTheDistanceValue(self, A: List[int], B: List[int], d: int) -> int:
    #     return sum(all(abs(a - b) > d for b in B) for a in A)
