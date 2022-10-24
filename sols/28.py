class Solution:
    # Library Find (Accepted), O(n + m) time, O(1) space
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # Brute force find (Top Voted), O(n + m) time, O(1) space
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
