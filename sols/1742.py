from collections import defaultdict


class Solution:
    # Brute Force (Accepted), O(n * h) time, O(n + h) space, n = highLimit - lowLimit + 1, h = len(str(highLimit))
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            n = sum(int(c) for c in str(i))
            d[n] += 1
        return max(d.values())

    # Id Pattern (Top Voted), O(n * h) time, O(1) space
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = [0] * 46
        lo, id = lowLimit, 0
        while lo > 0:
            id += lo % 10
            lo //= 10
        box[id] += 1
        for i in range(lowLimit + 1, highLimit + 1):
            while i % 10 == 0:
                id -= 9
                i //= 10
            id += 1
            box[id] += 1
        return max(box)
