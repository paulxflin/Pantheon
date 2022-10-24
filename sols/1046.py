import bisect
import heapq


class Solution(object):
    # # Bisect.insort (Accepted), O(n^2) time, O(n) space
    # def lastStoneWeight(self, stones):
    #     """
    #     :type stones: List[int]
    #     :rtype: int
    #     """
    #     if not stones:
    #         return 0
    #     stones.sort()
    #     while len(stones) >= 2:
    #         y = stones.pop()
    #         x = stones.pop()
    #         if x != y:
    #             bisect.insort(stones, y-x)
    #     if len(stones) == 0:
    #         return 0
    #     elif len(stones) == 1:
    #         return stones[0]

    # Heapq/minmum priority queue (Top Voted), O(n log n) time, O(n) space
    def lastStoneWeight(self, stones):
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]
