import itertools


class Solution:
    # Itertools (Accepted), O(n!) time, O(n * n!) space
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)

    # DFS (Top Voted), O(n!) time, O(n * n!) space
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
