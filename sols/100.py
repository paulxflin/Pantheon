# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # DFS (Accepted), O(n) time and space
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     res = True

    #     def dfs(node1, node2):
    #         nonlocal res
    #         if res:
    #             if node1 and node2:
    #                 dfs(node1.left, node2.left)
    #                 if node1.val != node2.val:
    #                     res = False
    #                 dfs(node1.right, node2.right)
    #             elif node1 or node2:
    #                 res = False

    #     dfs(p, q)
    #     return res

    # Short Simple Recursion (Top Voted), O(n) time and space
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
