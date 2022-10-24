class Solution:
    # Max to Min distance pair, O(n^2) time, O(1) space
    def maxDistance(self, colors: List[int]) -> int:
        for dist in range(len(colors)-1, 0, -1):
            for i in range(len(colors)-dist):
                if colors[i] != colors[i+dist]:
                    return dist

    # Max dist from endpoints (Top Voted), O(n) time, O(1) space
    def maxDistance(self, A: List[int]) -> int:
        i, j = 0, len(A) - 1
        while A[0] == A[j]:
            j -= 1
        while A[-1] == A[i]:
            i += 1
        return max(len(A) - 1 - i, j)
