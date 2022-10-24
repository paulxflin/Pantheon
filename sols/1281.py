class Solution:
    # # Iterate string and convert to int (Accepted), O(log n) time and space
    # def subtractProductAndSum(self, n: int) -> int:
    #     p = 1
    #     s = 0
    #     for i in str(n):
    #         p *= int(i)
    #         s += int(i)
    #     return p - s

    # # Map and Reduce (Top Voted), O(log n) time and space
    # def subtractProductAndSum(self, n: int) -> int:
    #     A = list(map(int, str(n)))
    #     return reduce(operator.mul, A) - sum(A)

    # Mod and Divide (Top Voted), O(log n) time, O(1) space
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        while n > 0:
            s += n % 10
            p *= n % 10
            n //= 10
        return p - s
