class Solution:
    # Brute Force (Accepted), O(n^2) time, O(n) space
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i, v in enumerate(nums):
            s = 0
            for v1 in nums[:i]:
                s += v1 < v
            for v2 in nums[i+1:]:
                s += v2 < v
            res.append(s)
        return res

    # Sorting (Top Voted), O(n log n) time, O(n) space
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dct = {}
        for i, n in enumerate(sorted(nums)):
            if n not in dct:
                dct[n] = i
        return [dct[n] for n in nums]

    # Counting (Top Voted), O(n) time and space
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 102):
            count[i] += count[i-1]
        return [count[num] for num in nums]
