class Solution:
    # # Greedy (Accepted), O(n) time, O(1) space
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    #     plots = len(flowerbed)
    #     flowerbed.append(0)
    #     prev = planted = 0
    #     for i in range(plots):
    #         if flowerbed[i] == 0:
    #             if prev == 0 and flowerbed[i+1] == 0:
    #                 planted += 1
    #                 flowerbed[i] = 1
    #         prev = flowerbed[i]
    #     return planted >= n

    # Greedy (Top Voted), O(n) time, O(1) space
    def canPlaceFlowers(self, A: List[int], N: int) -> bool:
        for i, x in enumerate(A):
            if (not x and (i == 0 or A[i-1] == 0)
                    and (i == len(A)-1 or A[i+1] == 0)):
                N -= 1
                A[i] = 1
        return N <= 0
