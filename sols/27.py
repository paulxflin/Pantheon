class Solution:
    # # Two pointers from start (Accepted), O(n) time, O(1) space
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     slow = fast = 0
    #     while fast < len(nums):
    #         if nums[fast] != val:
    #             nums[slow] = nums[fast]
    #             slow += 1
    #         fast += 1
    #     return slow

    # Two pointers meet in middle (Top Voted), O(n) time, O(1) space
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], end = nums[end], end - 1
            else:
                start += 1
        return start
