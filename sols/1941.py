from collections import Counter


class Solution:
    # Take first letter count, iterate through all key and values (Accepted), O(n) time and space
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)

        cnt = c[s[0]]
        for _, val in c.items():
            if val != cnt:
                return False
        return True

    # Length of values set in Counter (Top Voted), O(n) time and space
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
