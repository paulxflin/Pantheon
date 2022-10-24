class Solution:
    # Accumulator List (Accepted), O(n) time and space
    def waysToMakeFair(self, nums: List[int]) -> int:
        acc = []
        is_even = True
        n = len(nums)
        for i in range(n):
            even, odd = acc[i-1] if i > 0 else (0, 0)
            if is_even:
                even += nums[i]
            else:
                odd += nums[i]
            is_even = not is_even
            acc.append((even, odd))

        res = 0
        for i in range(n):
            even = odd = 0
            if i > 0:
                even += acc[i-1][0]
                odd += acc[i-1][1]
            if i < n-1:
                even += acc[n-1][1] - acc[i][1]
                odd += acc[n-1][0] - acc[i][0]
            if even == odd:
                res += 1
        return res

    # Two Sum Pairs for even and odd (Top Voted), O(n) time, O(1) space
    def waysToMakeFair(self, A: List[int]) -> int:
        s1, s2 = [0, 0], [sum(A[0::2]), sum(A[1::2])]
        res = 0
        for i, a in enumerate(A):
            s2[i % 2] -= a
            res += s1[0] + s2[1] == s1[1] + s2[0]
            s1[i % 2] += a
        return res
