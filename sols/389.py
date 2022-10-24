from collections import Counter

class Solution:
    # Counter (Accepted), O(n) time, O(1) space
    def findTheDifference(self, s: str, t: str) -> str:
        c1, c2 = Counter(s), Counter(t)
        c = c2-c1
        for k in c:
            return k

    # Difference (Top Voted), O(n) time, O(1) space
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)

    # XOR (Top Voted), O(n) time, O(1) space
    def findTheDifference(self, s: str, t: str) -> str:
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)