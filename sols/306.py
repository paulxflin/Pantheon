class Solution:
    # Test All Pairs (Accepted), O(n^2) time, O(n) space
    def isAdditiveNumber(self, num: str) -> bool:
        def is_additive(a, b, s):
            if s == '':
                return True
            target = str(int(a) + int(b))
            n = len(target)
            if s[:n] == target:
                return is_additive(b, target, s[n:])

        for pair_len in range(2, len(num)):
            for pair_ind in range(1, pair_len):
                a, b = num[:pair_ind], num[pair_ind:pair_len]
                if not (len(a) > 1 and a[0] == '0') and not(len(b) > 1 and b[0] == '0'):
                    if is_additive(a, b, num[pair_len:]):
                        return True
        return False

    # Test All Pairs + Itertool Combintations (Top Voted), O(n^2) time, O(n) space
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            a, b = num[:i], num[i:j]
            if a != str(int(a)) or b != str(int(b)):
                continue
            while j < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, j):
                    break
                j += len(c)
                a, b = b, c
            if j == n:
                return True
        return False
