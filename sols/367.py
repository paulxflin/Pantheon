class Solution:

    # Math (Accepted), O(1) time and space
    def isPerfectSquare(self, num: int) -> bool:
        return (num**0.5) % 1 == 0

    # # Binary Search (Top Voted), O(log n) time, O(1) space
    # def isPerfectSquare(self, num: int) -> bool:
    #     left, right = 0, num

    #     while left <= right:
    #         mid = left + (right-left)//2
    #         if  mid ** 2 == num:
    #             return True
    #         elif mid ** 2 > num:
    #             right = mid-1
    #         else:
    #             left = mid+1
    #     return False
