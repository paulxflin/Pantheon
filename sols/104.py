# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion (Accepted), O(n) time and space
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(cur, level):
            if cur == None:
                return level-1
            return max(dfs(cur.left, level + 1), dfs(cur.right, level + 1))
        return dfs(root, 1)

    # # One Liner (Top Voted), O(n) time and space
    # def maxDepth(self, root: TreeNode) -> int:
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
