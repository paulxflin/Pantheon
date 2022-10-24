class Solution:
    # Greedy (Accepted), O(g log g + s log s) time, O(g + s) space, where g, s = len(g), len(s)
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i, j = i+1, j+1
            else:
                j += 1
        return i

    # # Greedy (Top Voted), O(g log g + s log s) time, O(g + s) space, where g, s = len(g), len(s)
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     g.sort()
    #     s.sort()

    #     childi = 0
    #     cookiei = 0

    #     while cookiei < len(s) and childi < len(g):
    #         if s[cookiei] >= g[childi]:
    #             childi += 1
    #         cookiei += 1

    #     return childi
