import heapq


class KthLargest:

    # Heap of k elements (Accepted), O(n log n + n) init time, O(log n) add time, O(k) space
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.heap = nums[:k]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

    # # Heap of k elements (Top Voted), O(n + k log n) init time, O(log n) add time, O(k) space
    # def __init__(self, k, nums):
    #     self.pool = nums
    #     self.k = k
    #     heapq.heapify(self.pool)
    #     while len(self.pool) > k:
    #         heapq.heappop(self.pool)

    # def add(self, val):
    #     if len(self.pool) < self.k:
    #         heapq.heappush(self.pool, val)
    #     elif val > self.pool[0]:
    #         heapq.heapreplace(self.pool, val)
    #     return self.pool[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
