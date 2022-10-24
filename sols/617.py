# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Merge nodes recursively (Accepted), O(n + m) time and space, n = num_nodes(root1), m = num_nodes(root2)
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_node(node1, node2):
            if node1 and node2:
                left = merge_node(node1.left, node2.left)
                right = merge_node(node1.right, node2.right)
                return TreeNode(node1.val + node2.val, left, right)
            elif node1:
                return node1
            elif node2:
                return node2

        return merge_node(root1, root2)

    # Concise (Top voted), O(n + m) time and space
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2
