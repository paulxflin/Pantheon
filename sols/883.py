class Solution:
    # List Comp (Accepted), O(n) time, O(1) space
    def projectionArea(self, grid: List[List[int]]) -> int:
        area_xy = sum(n > 0 for arr in grid for n in arr)
        area_xz = sum(max(arr) for arr in grid)
        area_yz = sum(max(arr) for arr in zip(*grid))
        return area_xy + area_xz + area_yz

    # Map and Better Naming (Top Voted), O(n) time, O(1) space
    def projectionArea(self, grid):
        hor = sum(map(max, grid))
        ver = sum(map(max, zip(*grid)))
        top = sum(v > 0 for row in grid for v in row)
        return ver + hor + top

    # One Liner (Top Voted), O(n) time and space
    def projectionArea(self, grid):
        return sum(map(max, grid + list(zip(*grid)))) + sum(v > 0 for row in grid for v in row)
