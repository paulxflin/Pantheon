class Solution:
    # Scan Right to Left for Odd digit and slice (Accepted), O(n) time and space
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) % 2:
                return num[:i+1]
        return ""

    # # Scan Right to Left for Odd digit and slice (Accepted), O(n) time, O(1) space
    # def largestOddNumber(self, num: str) -> str:
    #     for i in range(len(num)-1, -1, -1):
    #         if int(num[i]) % 2:
    #             return num[:i+1]
    #     return ""

    # # Scan Left to Right for rightmost odd digit (Top Voted), O(n) time, O(1) space
    # def largestOddNumber(self, num: str) -> str:
    #     indx = -1
    #     n = len(num)
    #     for i in range(n):
    #         if int(num[i])%2 == 1:
    #             indx = i

    #     if indx == -1:
    #         return ""
    #     return num[:indx+1]
