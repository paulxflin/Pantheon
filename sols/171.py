class Solution:
    # One Liner List Comprehension (Accepted), O(n) time and space
    def titleToNumber(self, s):
        return sum((ord(s[i])-ord('A')+1) * (26**(len(s)-i-1)) for i in range(len(s)))

    # Constant Space (Accepted), O(n) time, O(1) space
    def titleToNumber(self, s):
        sum_ = 0
        for i in range(len(s)):
            sum_ += (ord(s[i])-ord('A')+1) * (26**(len(s)-i-1))
        return sum_

    # Concise (Top Voted), O(n) time, O(1) space
    def titleToNumber(self, s):
        res = 0
        for c in s:
            res = res*26 + ord(c)-ord('A')+1
        return res
