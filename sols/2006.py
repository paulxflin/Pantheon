from collections import defaultdict


class Solution:
    # Eval all pairs (Accepted), O(n^2) time, O(1) space
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    res += 1
        return res

    # Dictionary (Top Voted), O(n) time and space
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            counter += seen[num-k] + seen[num+k]
            seen[num] += 1
        return counter
