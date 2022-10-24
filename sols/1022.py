# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS and convert binary (Accepted), O(n) time and space
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, cur):
            cur *= 2
            cur += node.val
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
            if not node.left and not node.right:
                self.res += cur
        dfs(root, 0)
        return self.res

    # Recursion (Top Voted), O(n) time and space
    def sumRootToLeaf(self, root: Optional[TreeNode], val=0) -> int:
        if not root:
            return 0
        val = val * 2 + root.val
        if root.left == root.right:
            return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)
