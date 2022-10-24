class Solution:
    # Brute Force (Accepted), O(n^3) time, O(1) space
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res, length = sum(arr), 3
        while length <= len(arr):
            for i in range(0, len(arr)-length+1):
                res += sum(arr[i:i+length])
            length += 2
        return res

    # Contribution of A[i] (Top Voted), O(n) time, O(1) space
    def sumOddLengthSubarrays(self, A):
        res, n = 0, len(A)
        for i, a in enumerate(A):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res
