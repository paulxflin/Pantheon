class Solution:
    # While-Else (Accepted), O(n) time, O(1) space
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for grp in groups:
            l = len(grp)
            while i < len(nums):
                if nums[i:i+l] == grp:
                    i += l
                    break
                else:
                    i += 1
            else:
                return False
        return True

    # For-Else (Top Voted), O(n) time, O(1) space
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for grp in groups:
            for ii in range(i, len(nums)):
                if nums[ii:ii+len(grp)] == grp:
                    i = ii + len(grp)
                    break
            else:
                return False
        return True
