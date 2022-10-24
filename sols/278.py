# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

import bisect


class Solution:
    # # Binary Search (Accepted), O(log n) time, O(1) space
    # def firstBadVersion(self, n):
    #     low, high = 1, n
    #     while low < high:
    #         mid = (low + high) // 2
    #         if isBadVersion(mid):
    #             high = mid
    #         else:
    #             low = mid + 1
    #     return low if isBadVersion(low) else low + 1

    # Binary Search using Bisect + Wrapper (Top Voted), O(log n) time, O(1) space
    def firstBadVersion(self, n):
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 1, n)
