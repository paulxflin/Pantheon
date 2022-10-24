class Solution:
    # Convert to Base Array (Accepted), O(log n) time and space
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        arr = []
        while n:
            arr.append(n % k)
            n //= k
        return sum(arr)

    # Divide and Mod (Accepted + Top Voted), O(log n) time, O(1) space
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n:
            res += n % k
            n //= k
        return res
