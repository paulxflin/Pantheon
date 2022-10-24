class Solution:
    # # Popping Elements (Accepted), O(n^2) time, O(1) space
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     cur = nums[0]
    #     count = 0
    #     i = 0
    #     while i < len(nums):
    #         if nums[i] == cur:
    #             count += 1
    #         else:
    #             cur = nums[i]
    #             count = 1
    #         if count > 2:
    #             nums.pop(i)
    #             count = 2
    #         else:
    #             i += 1
    #     return i

    # # Two pointers (Revisited), O(n) time, O(1) space
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     res = 0
    #     cur = None
    #     cur_cnt = 0
    #     cur_ind = 0
    #     for i in range(len(nums)):
    #         if nums[i] == cur:
    #             if cur_cnt == 2:
    #                 continue
    #             cur_cnt += 1
    #         else:
    #             cur = nums[i]
    #             cur_cnt = 1
    #         nums[cur_ind] = nums[i]
    #         cur_ind += 1
    #         res += 1
    #     return res

    # Setting first n elements (Top Voted), O(n) time, O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
