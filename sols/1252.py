class Solution:
    # Add odd combinations (Accepted), O(m + n + L) time, O(m + n) space
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        num_odd = sum(i % 2 for i in rows)
        res = 0
        for j in cols:
            if j % 2:
                res += m - num_odd
            else:
                res += num_odd
        return res

    # XOR (Top Voted), O(m + n + L) time, O(m + n) space
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        odd_rows, odd_cols = [False] * m, [False] * n
        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
        return (n - sum(odd_cols)) * sum(odd_rows) + (m - sum(odd_rows)) * sum(odd_cols)
