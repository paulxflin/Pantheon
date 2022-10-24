from collections import defaultdict


class Solution:
    # Dict of Lists (Accepted), O(n) time, O(1) space
    def countPoints(self, rings: str) -> int:
        col_d = {'R': 0, 'G': 1, 'B': 2}
        rod_d = {}
        for i in range(0, len(rings), 2):
            rod = int(rings[i+1])

            if rod not in rod_d:
                rod_d[rod] = [0, 0, 0]
            rod_d[rod][col_d[rings[i]]] = 1

        res = 0
        for k in rod_d:
            if sum(rod_d[k]) == 3:
                res += 1
        return res

    # 4 Liner Dict of Sets (Top Voted), O(n) time, O(1) space
    def countPoints(self, rings: str) -> int:
        h = defaultdict(set)
        for i in range(0, len(rings) - 1, 2):
            h[rings[i + 1]].add(rings[i])
        return sum(len(v) == 3 for v in h.values())
