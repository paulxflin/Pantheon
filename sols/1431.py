class Solution:
    # Max and add extra candies (Accepted), O(n) time and space
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        return [candies[i] + extraCandies >= max_ for i in range(len(candies))]

    # Gauge (Top Voted), O(n) time and space
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        gauge = max(candies) - extraCandies
        return [candy >= gauge for candy in candies]
