class Solution(object):
    # # Proven even number wins by mathematical induction (Top Voted), Time and Space O(1)
    # def divisorGame(self, N):
    #     return N % 2 == 0

    # Bottom Up Dynamic Programming (Top Voted), Time O(n * sqrt(n)), Space O(n)
    def divisorGame(self, N):
        dp = [False for i in range(N+1)]  # Create an array 0 to N all false
        for i in range(N+1):
            # We know divisor goes up to i//2 only.
            for j in range(1, i//2 + 1):
                if i % j == 0 and (not dp[i - j]):
                    dp[i] = True  # Found divisor where opponent gets a loss
                    break
        return dp[N]
