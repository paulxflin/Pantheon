class Solution:
    # One Pass (Accepted), O(n) time, O(1) space
    def maxScore(self, s: str) -> int:
        _max = cur = ones = 0
        for i in range(1, len(s)-1):
            if s[i] == '0':
                cur += 1
                _max = max(cur, _max)
            else:
                cur -= 1
                ones += 1
        return int(s[0] == '0') + ones + int(s[-1]) + _max

    # Simple two pass (Top Voted), O(n) time, O(1) space
    def maxScore(self, s: str) -> int:
        zeros = 1 if s[0] == '0' else 0
        ones = s.count('1', 1)  # count 1s in s[1:]
        score = zeros + ones
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            score = max(zeros + ones,  score)
        return score
