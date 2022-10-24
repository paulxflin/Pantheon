class Solution:
    # # Binary Search (Accepted), O(log n) time, O(1) space
    # def arrangeCoins(self, n: int) -> int:
    #     low, high = 0, n
    #     while low < high:
    #         mid = (low + high + 1) // 2

    #         if mid**2 - mid*(mid-1)/2 <= n:
    #             low = mid
    #         else:
    #             high = mid - 1

    #     return low

    # Maths (Solution), O(1) time and space
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
