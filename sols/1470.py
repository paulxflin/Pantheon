class Solution:
    # Append twice (Accepted), O(n) time and space
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res

    # Append array (Accepted), O(n) time and space
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res += [nums[i], nums[i+n]]
        return res

    # Deconstruct zip (Top Voted), O(n) time and space
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n], nums[n:]):
            res += [i, j]
        return res
