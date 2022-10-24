import copy


class Solution:
    # # Backtracking with candidates (Accepted), O(n * 2^n) time and space
    # def partition(self, s: str) -> List[List[str]]:
    #     def is_palin(s):
    #         return s == s[::-1]

    #     def add_children(node):
    #         cur_str = node[1]
    #         for l in range(1, len(cur_str)+1):
    #             if is_palin(cur_str[:l]):
    #                 child = (cur_str[:l], cur_str[l:], [])
    #                 node[2].append(child)
    #                 add_children(child)

    #     def dfs(node, arr, res):
    #         if len(node[0]):
    #             arr.append(node[0])
    #         children = node[2]
    #         if not children:
    #             res.append(arr)
    #             return res
    #         for n in children:
    #             res = dfs(n, copy.deepcopy(arr), res)

    #         return res

    #     root = ("", s, []) #Contains the value, remainder, and children
    #     add_children(root)
    #     res = dfs(root, [], [])
    #     return res

    # # Backtracking (Revisited), O(n * 2^n) time, O(n) space
    # def is_palin(self, s):
    #     return s == s[::-1]

    # def dfs(self, s, palins):
    #     if not s:
    #         self.res.append(palins)
    #         return
    #     for i in range(1, len(s) + 1):
    #         if self.is_palin(s[:i]):
    #             self.dfs(s[i:], palins + [s[:i]])

    # def partition(self, s: str) -> List[List[str]]:
    #     self.res = []
    #     self.dfs(s, [])
    #     return self.res

    # Backtracking (Top Voted), O(n * 2^n) time, O(n) space
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]
