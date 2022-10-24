class Solution:
    # # Count Wrong Positions (Accepted), O(n) time, O(1) space
    # def minSwaps(self, s: str) -> int:
    #     num_ones = 0
    #     num_zeroes = 0
    #     cur = True if s[0] == '1' else False
    #     disorders = 0
    #     for c in s:
    #         if c == '1':
    #             num_ones += 1
    #         elif c == '0':
    #             num_zeroes += 1

    #         if (cur and c == '0') or (not cur and c == '1'):
    #             disorders += 1

    #         cur = not cur

    #     if num_ones - num_zeroes == 0:
    #         return min(disorders // 2, (len(s) - disorders) // 2)
    #     elif abs(num_ones - num_zeroes) == 1:
    #         if (s[0] == '0' and num_zeroes < num_ones) or num_ones < num_zeroes and s[0] == '1':
    #             return (len(s) - disorders) // 2
    #         return disorders // 2
    #     else:
    #         return -1

    # Count Wrong Positions (Top Voted), O(n) time, O(1) space
    def minSwaps(self, s: str) -> int:
        def countSwaps(start):
            cntWrongPos = 0
            for c in s:
                if start != c:
                    cntWrongPos += 1
                start = '1' if start == '0' else '0'
            return cntWrongPos // 2

        cntOne = s.count('1')
        cntZero = len(s) - cntOne
        if abs(cntOne - cntZero) > 1:  # Invalid
            return -1
        if cntZero > cntOne:  # zero must be on even position
            return countSwaps('0')
        if cntZero < cntOne:  # One must be on even position
            return countSwaps('1')
        # get min swaps between 2 case (zero start first or one start first)
        return min(countSwaps('0'), countSwaps('1'))
