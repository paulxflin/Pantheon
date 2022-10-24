from collections import defaultdict


class Solution(object):
    # # defaultdict + Base Case (Accepted), Time O(T + N), Space O(N)
    # def findJudge(self, n, trust):
    #     """
    #     :type n: int
    #     :type trust: List[List[int]]
    #     :rtype: int
    #     """
    #     if not trust and n == 1:
    #         return n

    #     num_trusted = defaultdict(int)
    #     num_trusts = defaultdict(int)
    #     for [a, b] in trust:
    #         num_trusted[b] += 1
    #         num_trusts[a] += 1

    #     for k, v in num_trusted.items():
    #         if v == n-1 and num_trusts[k] == 0:
    #             return k
    #     return -1

    # # defaultdict + no basecase (Accepted), Time O(T + N), Space O(N)
    # def findJudge(self, n, trust):
    #     """
    #     :type n: int
    #     :type trust: List[List[int]]
    #     :rtype: int
    #     """

    #     num_trusted = defaultdict(int)
    #     num_trusts = defaultdict(int)
    #     for [a, b] in trust:
    #         num_trusted[b] += 1
    #         num_trusts[a] += 1

    #     for person in range(1, n+1):
    #         if num_trusted[person] == n-1 and num_trusts[person] == 0:
    #             return person
    #     return -1

    # Consider trust as Graph (Top Voted), Time O(T + N), Space O(N)
    def findJudge(self, N, trust):
        count = [0] * (N + 1)  # A bit of extra unused space in index 0.
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1
