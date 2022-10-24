class Solution:
    # Brute Force (Accepted), O(n^2) time, O(n) space
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, p in enumerate(prices[:-1]):
            for p2 in prices[i+1:]:
                if p >= p2:
                    prices[i] = p - p2
                    break
        return prices

    # Stack (Top Voted), O(n) time and space
    def finalPrices(self, A: List[int]) -> List[int]:
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] >= a:
                A[stack.pop()] -= a
            stack.append(i)
        return A
