class Solution:
    # Greedy (Accepted), O(n) time and space
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        for i in range(len(s)):
            if s[i] == '6':
                s = s[:i] + '9' + s[i+1:]
                return int(s)
        return num

    # # Greedy One Liner (Top Voted), O(n) time and space
    # def maximum69Number (self, num: int) -> int:
    #     return int(str(num).replace('6', '9', 1))
