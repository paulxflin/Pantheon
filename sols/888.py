class Solution:
    # # For Loop Summing + Dict (Accepted), O(n + m) time, O(m) space
    # def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    #     n = m = 0
    #     bob_dict = {}
    #     for val in aliceSizes:
    #         n += val

    #     for val in bobSizes:
    #         bob_dict[val] = True
    #         m += val

    #     diff = (m - n) // 2
    #     for val in aliceSizes:
    #         if val + diff in bob_dict:
    #             return [val, val+diff]

    # # Sum and Sets (Top Voted), O(n + m) time and space
    # def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    #     dif = (sum(A) - sum(B)) / 2
    #     A = set(A)
    #     for b in set(B):
    #         if dif + b in A:
    #             return [dif + b, b]

    # Sum and Sets (Top Voted Modified), O(n + m) time, O(n) space
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        dif = (sum(A) - sum(B)) / 2
        A = set(A)
        for b in B:
            if dif + b in A:
                return [dif + b, b]
