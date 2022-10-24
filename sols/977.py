class Solution(object):
    # # Brute Force (Accepted), Time O(n + n log n) -> O(n log n), Space O(n)
    # def sortedSquares(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     out = []
    #     for i in nums:
    #         out.append(i**2)
    #     out.sort()
    #     return out

    # # Two Pointers + Reverse (Accepted), Time O(n), Space O(n)
    # def sortedSquares(self, nums):
    #     out = []
    #     a = 0
    #     b = len(nums) - 1
    #     while a != b:
    #         if abs(nums[a]) > abs(nums[b]):
    #             out.append(nums[a] ** 2)
    #             a += 1
    #         else:
    #             out.append(nums[b] ** 2)
    #             b -= 1
    #     out.append(nums[a] ** 2)
    #     out.reverse()
    #     return out

    # Two Pointers + Deque (Top Voted), Time O(n), Space O(n)
    def sortedSquares(self, A):
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)
