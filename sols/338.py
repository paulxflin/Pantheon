class Solution:
    # # Brute Force (Accepted), O(n log n) time, O(log n) space
    # def countBits(self, n: int) -> List[int]:
    #     res = []
    #     for i in range(n + 1):
    #         s = 0
    #         for c in bin(i):
    #             if c == '1':
    #                 s += 1
    #         res.append(s)
    #     return res

    # # DP + Bit Manipulation (Top Voted), O(n) time and space
    # def countBits(self, num: int) -> List[int]:
    #     counter = [0]
    #     for i in range(1, num+1):
    #         counter.append(counter[i >> 1] + i % 2)
    #     return counter

    # DP + Bit Manipulation (Top Voted), O(n) time and space
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + (i & 1))
        return counter
