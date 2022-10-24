# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative (Accepted), O(n) time, O(1) space
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node != None:
            if node.val == val:
                return node
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return node

    # Recursive (Top Voted), O(n) time and space
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        return root
