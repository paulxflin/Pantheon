import math


class Solution:
    # Track min_dist index (Accepted), O(n) time, O(1) space
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        min_dist = float('inf')
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                dist = abs(a - x) + abs(b-y)
                if dist < min_dist:
                    min_dist = dist
                    res = i
        return res

    # Multiply dist to check valid (Top Voted), O(n) time, O(1) space
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index, smallest = -1, math.inf
        for i, (r, c) in enumerate(points):
            dx, dy = x - r, y - c
            if dx * dy == 0 and abs(dx + dy) < smallest:
                smallest = abs(dx + dy)
                index = i
        return index
