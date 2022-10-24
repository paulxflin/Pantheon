class Solution:
    # # Simple Solution (Accepted), O(min(len(a), len(b))) time, O(1) space
    # def findLUSlength(self, a: str, b: str) -> int:
    #     if len(b) > len(a):
    #         return len(b)
    #     elif len(a) > len(b):
    #         return len(a)

    #     if a == b:
    #         return -1
    #     else:
    #         return len(a)

    # Simple Solution (Top Voted), O(min(len(a), len(b))) time, O(1) space
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))
