class Solution:
    # Track Max Altitude (Accepted), O(n) time, O(1) space
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = max_ = 0
        for n in gain:
            altitude += n
            max_ = max(altitude, max_)
        return max_

    # One liner (Top Voted), O(n) time, O(1) space
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(accumulate(gain)))
