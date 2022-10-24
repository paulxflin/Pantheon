# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # # Dummy + DFS (Accepted), O(n^2) time (traversing new tree every insert!), O(n) space
    # def append_node(self, node, root):
    #     curnode = root
    #     while curnode.right != None:
    #         curnode = curnode.right
    #     curnode.right = TreeNode(node.val)

    # def dfs(self, node, dummy):
    #     if node.left:
    #         self.dfs(node.left, dummy)
    #     self.append_node(node, dummy)
    #     if node.right:
    #         self.dfs(node.right, dummy)

    # def increasingBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     dummy = TreeNode()
    #     if root:
    #         self.dfs(root, dummy)
    #     return dummy.right

    # # Dummy + DFS Optimised (Accepted), O(n) time and space
    # def append_node(self, node):
    #     self.last_node.right = TreeNode(node.val)
    #     self.last_node = self.last_node.right

    # def dfs(self, node, dummy):
    #     if node.left:
    #         self.dfs(node.left, dummy)
    #     self.append_node(node)
    #     if node.right:
    #         self.dfs(node.right, dummy)

    # def increasingBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     dummy = TreeNode()
    #     self.last_node = dummy
    #     if root:
    #         self.dfs(root, dummy)
    #     return dummy.right

    # # Traversal with Relinking (Solution), Time O(n), Space O(h)
    # def increasingBST(self, root):
    #     def inorder(node):
    #         if node:
    #             inorder(node.left)
    #             node.left = None
    #             self.cur.right = node
    #             self.cur = node
    #             inorder(node.right)

    #     ans = self.cur = TreeNode(None)
    #     inorder(root)
    #     return ans.right

    # Traversal (Top Voted), Time O(n), Space O(h)
    def increasingBST(self, root, tail=None):
        if not root:
            return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
