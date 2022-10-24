import itertools


class Solution:
    # Two Pointer (Accepted), O(n) time, O(1) space
    def backspaceCompare(self, s: str, t: str) -> bool:
        hash_s = hash_t = 0
        i, j = len(s)-1, len(t)-1
        while i >= 0 or j >= 0:
            if i >= 0 and s[i] == '#':
                hash_s += 1
                i -= 1
            elif hash_s > 0:
                hash_s -= 1
                i -= 1
            elif j >= 0 and t[j] == '#':
                hash_t += 1
                j -= 1
            elif hash_t > 0:
                hash_t -= 1
                j -= 1
            else:
                if i < 0 or j < 0 or s[i] != t[j]:
                    return False
                i, j = i-1, j-1

        return True

    # Generator (Accepted), O(n) time, O(1) space
    def backspaceCompare(self, s: str, t: str) -> bool:
        def back(s):
            h, i = 0, len(s)-1
            while i >= 0:
                if s[i] == '#':
                    h += 1
                elif h > 0:
                    h -= 1
                else:
                    yield s[i]
                i -= 1
            while True:
                yield None

        gen1, gen2 = back(s), back(t)
        a, b = next(gen1), next(gen2)
        while a or b:
            if a != b:
                return False
            a, b = next(gen1), next(gen2)

        return True

    # Two Pointer + Itertools Zip Longest (Solution), O(n) time, O(1) space
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))

    # Two Pointer (Top Voted), O(n) time, O(1) space
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1
