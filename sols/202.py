class Solution:
    # Recursive with Set (Accepted), O(l*d) time, O(l) space, l = calls of helper, d = digits in n
    def isHappy(self, n: int) -> bool:
        seen = set()

        def helper(n):
            s = str(n)
            res = 0
            for c in s:
                res += int(c) ** 2
            if res == 1:
                return True
            elif res in seen:
                return False
            else:
                seen.add(res)
                return helper(res)
        seen.add(n)
        return helper(n)

    # Succinct Iterative with Set (Top Voted), # Recursive with Set (Accepted), O(l*d) time, O(1) space
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1
