from collections import deque


class RecentCounter(object):

    def __init__(self):
        self.queue = deque()

    # # Queue with Break (Accepted), O(1) time, O(1) space (based on problem spec)
    # def ping(self, t):
    #     """
    #     :type t: int
    #     :rtype: int
    #     """
    #     self.queue.append(t)
    #     for i in range(len(self.queue)):
    #         if self.queue[0] < (t - 3000):
    #             self.queue.popleft()
    #         else:
    #             break
    #     return len(self.queue)

    # Queue (Accepted + Top Voted), O(1) time and space
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        while self.queue[0] < (t - 3000):
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
