class Solution:
    # Brute Force (Accepted), O(n^3) time, O(1) space
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def good(i, j, v):
            return abs(arr[i]-arr[j]) <= v

        ans = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if good(i, j, a) and good(j, k, b) and good(i, k, c):
                        ans += 1
        return ans

    # Generator Expression (Top Voted), O(n^3) time, O(1) space
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def is_good(i, j, k):
            return abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c

        n = len(arr)

        return sum(1 for i in range(n-2) for j in range(i+1, n-1) for k in range(j+1, n) if is_good(i, j, k))
