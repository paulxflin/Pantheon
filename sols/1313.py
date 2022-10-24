class Solution:
    # Generating List by Append (Accepted), O(n) time and space
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums) // 2):
            for _ in range(nums[2*i]):
                res.append(nums[2*i + 1])
        return res

    # Concatenating Lists (Accepted), O(n) time and space
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums) // 2):
            res += [nums[2*i+1]] * nums[2*i]
        return res

    # One Liner Concatenating Lists (Top Voted), O(n) time and space
    def decompressRLElist(self, A: List[int]) -> List[int]:
        return [x for a, b in zip(A[::2], A[1::2]) for x in [b] * a]
