class Solution:
    # Get digit with string (Accepted), O(n*l) time, O(n + l) space (n = L - R, l = digits in R)
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_dividing(n):
            s = str(n)
            for c in s:
                if int(c) == 0 or n % int(c) != 0:
                    return False
            return True
        res = []
        for i in range(left, right+1):
            if self_dividing(i):
                res.append(i)
        return res

    # Optimised One Liner (Top Voted), O(n*l) time, O(n + l) space
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right+1) if all((i and (x % i == 0) for i in map(int, str(x))))]
