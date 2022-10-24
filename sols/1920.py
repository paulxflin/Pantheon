class Solution:
    # List Comprehension (Accepted), O(n) time and space
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]

    # Euclidian Algorithm (Top Voted), O(n) time, O(1) space
    def buildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)
        for i, c in enumerate(nums):
            nums[i] += q * (nums[c] % q)
        for i in range(len(nums)):
            nums[i] //= q
        return nums
