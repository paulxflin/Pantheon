class Solution:
    # Enumerate shortest length (Accepted), O(n*l) time, O(l) space (n = len(strs), l = len(shortest str))
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        res = ""
        for i in range(min_len):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return res
            res += c
        return res

    # Enumerate shortest (Top Voted), O(n*l) time, O(l) space
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
