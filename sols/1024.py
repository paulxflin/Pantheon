from collections import defaultdict


class Solution:
    # Dict (Accepted), O(n) time and space
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        d = defaultdict(int)
        for start, end in clips:
            if start < time:
                d[start] = max(d[start], end)
        prev, new, res = -1, 0, 0
        while new < time:
            old = new
            for i in range(prev+1, old+1):
                if d[i] > new:
                    new = d[i]
            prev = old
            if prev != new:
                res += 1
            else:
                return -1
        return res

    # Sort (Top Voted), O(n log n) time and space
    def videoStitching(self, clips, T):
        end, end2, res = -1, 0, 0
        for i, j in sorted(clips):
            if end2 >= T or i > end2:
                break
            elif end < i <= end2:
                res, end = res + 1, end2
            end2 = max(end2, j)
        return res if end2 >= T else -1
