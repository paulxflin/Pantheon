# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive DFS (Accepted), O(n) time and space
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def dfs(node, path):
            if node:
                if path != "":
                    path += "->"
                path += str(node.val)
                if not node.left and not node.right:
                    res.append(path)
                dfs(node.left, path)
                dfs(node.right, path)
        if root:
            dfs(root, "")
        return res

    # Recursive DFS (Top Voted), O(n) time and space
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)
