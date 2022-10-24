class Solution:
    # Delete row func using indexes, O(n*m) time, O(1) space
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])

        def delete(j):
            for i in range(n-1):
                if strs[i][j] > strs[i+1][j]:
                    return True
            return False

        return sum(delete(j) for j in range(m))

    # One liner using zip (Top Voted), O(n*m) time and space
    def minDeletionSize(self, A):
        return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*A))
