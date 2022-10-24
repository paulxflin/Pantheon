class Solution:
    # Sweep Lines (Top Voted), O(b + n) time, O(n) space
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)
        for i, j, k in bookings:
            res[i - 1] += k
            res[j] -= k
        for i in range(1, n):
            res[i] += res[i - 1]
        return res[:-1]

    # Sweep Lines (Revisited), O(b + n) time, O(n) space
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)  # Add 1 for the flight n case
        for first, last, seats in bookings:
            ans[first-1] += seats
            ans[last] -= seats
        for i in range(1, n+1):
            ans[i] += ans[i-1]
        return ans[:-1]
