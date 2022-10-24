class Solution:
    # Find first repeated (Accepted), O(n) time and space
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            else:
                seen.add(n)

    # One Liner (Top Voted), O(n) time and space
    def repeatedNTimes(self, nums: List[int]) -> int:
        return int((sum(nums)-sum(set(nums))) // (len(nums)//2-1))
