class Solution:
    # One Liner (Accepted + Top Voted), O(n) time and space
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

    # Extend (Sample), O(n) time and space
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        ans.extend(nums)
        return ans
