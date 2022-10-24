class Solution:
    # Sort and Count Equal (Accepted), O(n log n) time, O(n) space
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, n in enumerate(sorted(nums)):
            if n == target:
                res.append(i)
            if n > target:
                return res
        return res

    # Count Smaller (Top Voted), O(n) time and space
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        cnt_smaller = 0
        cnt_equal = 0
        for x in nums:
            if x < target:
                cnt_smaller += 1
            elif x == target:
                cnt_equal += 1
        return range(cnt_smaller, cnt_smaller + cnt_equal)
