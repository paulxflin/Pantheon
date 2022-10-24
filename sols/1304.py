class Solution:
    # Continuous Values (Accepted), O(n) time and space
    def sumZero(self, n: int) -> List[int]:
        c = n // 2
        if n % 2:
            return [i-c for i in range(n)]
        else:
            res = []
            for i in range(1, c + 1):
                res.append(i)
                res.append(-i)
            return res

    # Find the Rule (Top Voted), O(n) time and space
    def sumZero(self, n: int) -> List[int]:
        return range(1 - n, n, 2)
