class Solution:
    # Codes (Accepted), O(n) time and space
    def replaceDigits(self, s: str) -> str:
        li, n = [], len(s)
        for i in range(0, n, 2):
            if i+1 < n:
                code = ord(s[i]) + int(s[i+1])
                li += [s[i], chr(code)]
            else:
                li.append(s[i])
        return "".join(li)

    # Straight Forward Codes (Top Voted), O(n) time and space
    def replaceDigits(self, s: str) -> str:
        a = list(s)
        for i in range(1, len(a), 2):
            a[i] = chr(ord(a[i - 1]) + int(a[i]))
        return ''.join(a)
