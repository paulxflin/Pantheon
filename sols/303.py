class NumArray:

    # # Brute Force (Accepted), O(n * c) time, O(1) space, where n is len(nums), c is number of calls to sumRange
    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     i = left
    #     res = 0
    #     while i <= right:
    #         res += self.nums[i]
    #         i += 1
    #     return res

    # Memorisation/DP (Accepted), O(n) time and space
    def __init__(self, nums: List[int]):
        self.memo = []
        s = 0
        for i in nums:
            s += i
            self.memo.append(s)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.memo[right]
        else:
            return self.memo[right] - self.memo[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
