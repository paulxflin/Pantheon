from functools import lru_cache


class Solution:
    # # Top Down DP (Top Voted), O(2^n) time and space
    # # n = maxChoosableInteger
    # def canIWin(self, maxChoosableInteger, desiredTotal):
    #     """
    #     :type maxChoosableInteger: int
    #     :type desiredTotal: int
    #     :rtype: bool
    #     """
    #     seen = {}

    #     def can_win(choices, remainder):
    #         # if the largest choice exceeds the remainder, then we can win!
    #         if choices[-1] >= remainder:
    #             return True

    #         # if we have seen this exact scenario play out, then we know the outcome
    #         seen_key = tuple(choices)
    #         if seen_key in seen:
    #             return seen[seen_key]

    #         # we haven't won yet.. it's the next player's turn.
    #         for index in range(len(choices)):
    #             if not can_win(choices[:index] + choices[index + 1:], remainder - choices[index]):
    #                 seen[seen_key] = True
    #                 return True

    #         # uh-oh if we got here then next player won all permutations, we can't force their hand
    #         # actually, they were able to force our hand :(
    #         seen[seen_key] = False
    #         return False

    #     # let's do some quick checks before we journey through the tree of permutations
    #     summed_choices = (maxChoosableInteger + 1) * maxChoosableInteger / 2

    #     # if all the choices added up are less then the total, no-one can win
    #     if summed_choices < desiredTotal:
    #         return False

    #     # if the sum matches desiredTotal exactly then you win if there's an odd number of turns
    #     if summed_choices == desiredTotal:
    #         return maxChoosableInteger % 2

    #     # slow: time to go through the tree of permutations
    #     choices = list(range(1, maxChoosableInteger + 1))
    #     return can_win(choices, desiredTotal)

    # Top Down DP (Revisited), O(2^n) time and space
    def canIWin(self, M: int, D: int) -> bool:
        memo = {}

        def can_win(choices, remainder):
            if not choices:
                return False

            if choices[-1] >= remainder:
                return True

            k = tuple(choices)
            if k in memo:
                return memo[k]

            for i in range(len(choices)):
                if not can_win(choices[:i] + choices[i+1:], remainder-choices[i]):
                    memo[k] = True
                    return True

            memo[k] = False
            return False

        sm = (1 + M) * M / 2
        if D > sm:
            return False
        elif D == sm:
            return M % 2  # Don't need to return == 1 because 1 is True in Python

        return can_win(list(range(1, M+1)), D)

    # # LRU Cache (Sample), O(2^n) time and space, where n = maxChoosableInteger
    # def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
    #     # if you don't use functools lru_cache(None)
    #     # The code below is two times slower
    #     maxValue = (maxChoosableInteger * (1 + maxChoosableInteger)) // 2
    #     if maxValue < desiredTotal:
    #         return False
    #     if maxValue == desiredTotal:
    #         return maxChoosableInteger % 2

    #     @lru_cache(maxsize=None)
    #     def helper(target, mask):
    #         for x in range(maxChoosableInteger, 0, -1):  # CAREFUL
    #             if (mask >> x) & 1 == 0 \
    #                     and (x >= target or not helper(target - x, mask | (1 << x))):
    #                 return True  # CAREFUL with "not"
    #         return False

    #     return helper(desiredTotal, 0)
