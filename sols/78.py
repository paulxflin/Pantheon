from itertools import chain, combinations


class Solution:
    # Powerset with Itertools Recipe (Accepted), O(n * 2^n) time, O(n * 2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1))

    # DFS (Top Voted), O(n * 2^n) time and space
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], ret)

    # Iterative (Top Voted), O(n * 2^n) time and space
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res
