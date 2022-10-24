class Solution:
    # While and For-Else Brute Force (Accepted), O(n^2) time, O(n) space
    def makeGood(self, s: str) -> str:
        while len(s) > 1:
            for i in range(len(s)-1):
                if s[i] == s[i+1].swapcase():
                    s = s[:i] + s[i+2:]
                    break
            else:
                return s
        return s

    # Stack and Swapcase (Accepted), O(n) time and space
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch.swapcase():
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

    # Stack without Swapcase (Top Voted), O(n) time and space
    def makeGood(self, s: str) -> str:
        result = []
        for c in s:
            if not result:
                result.append(c)
            elif result[-1].isupper() and result[-1].lower() == c:
                result.pop()
            elif result[-1].islower() and result[-1].upper() == c:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)
