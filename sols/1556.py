class Solution:
    # While loop join, O(n) time and space
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        l = []
        if len(s) <= 3:
            return s
        i = 0
        r = len(s) % 3
        if r == 0:
            l.append(s[:3])
            i = 3
        else:
            l.append(s[:r])
            i = r
        while i != len(s):
            l.append(s[i:i+3])
            i += 3
        return '.'.join(l)

    # Conditional + List Comprehension (Accepted), O(n) time and space
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        r = len(s) % 3
        return '.'.join(([s[:r]] if r else []) + [s[i:i+3] for i in range(r, len(s), 3)])

    # Reverse (Top Voted), O(n) time and space
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        s = s[::-1]
        res = '.'.join(s[i:i + 3] for i in range(0, len(s), 3))
        return res[::-1]
