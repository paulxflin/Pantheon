class Solution:
    # One Pass (Accepted), O(n) time, O(1) space
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        max_ = -float('inf')
        for l, w in rectangles:
            length = min(l, w)
            if length > max_:
                max_ = length
                res = 1
            elif length == max_:
                res += 1
        return res

    # Concise (Top Voted), O(n) time, O(1) space
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = mx = 0
        for l, w in rectangles:
            side = min(l, w)
            if side > mx:
                cnt, mx = 1, side
            elif side == mx:
                cnt += 1
        return cnt
