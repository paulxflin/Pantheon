from collections import Counter


class Solution:
    # Counter and sort by key (Accepted), O(n log n) time, O(n) space
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        nums.sort(key=lambda n: (cnt[n], -n))
        return nums

    # Two Liner (Top Voted), O(n log n) time, O(n) space
    def frequencySort(self, nums: List[int]) -> List[int]:
        r = Counter(nums)
        return sorted(nums, key=lambda x: (r[x], -x))
