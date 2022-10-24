# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    # # DFS + Queue (Accepted), O(t1 + t2) time and space
    # def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    #     li = deque([])
    #     res = True

    #     def dfs(node, first):
    #         if node:
    #             if node.left:
    #                 dfs(node.left, first)
    #             elif not node.left and not node.right:
    #                 if first:
    #                     li.append(node.val)
    #                 else:
    #                     if li and li[0] == node.val:
    #                         li.popleft()
    #                     else:
    #                         nonlocal res
    #                         res = False
    #             if node.right:
    #                 dfs(node.right, first)
    #     dfs(root1, True)
    #     dfs(root2, False)
    #     return res if not li else False

    # DFS + List Compare (Modified Solution), O(t1 + t2) time and space
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                else:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
        return list(dfs(root1)) == list(dfs(root2))
