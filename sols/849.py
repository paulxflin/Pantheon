class Solution:
    # One Pass Walrus (Accepted), O(n) time, O(1) space
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev, max_space, n = -1, 0, len(seats)
        for i in range(n):
            if seats[i]:
                if (space := i-prev-1) > max_space:
                    max_space = space
                prev = i
        return max((max_space + 1)//2, seats.index(1), n-prev-1)

    # One Pass (Top Voted), O(n) time, O(1) space
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last) // 2)
                last = i
        return max(res, n - last - 1)
