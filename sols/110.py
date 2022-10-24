# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive with Class Variable (Accepted), O(n) time and space
    res = True

    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(node, level):
            if node:
                h1 = get_height(node.left, level+1)
                h2 = get_height(node.right, level+1)
                if abs(h1 - h2) > 1:
                    self.res = False
                return max(h1, h2)
            else:
                return level-1

        get_height(root, 0)
        return self.res

    # # Recursively Propagating -1 (Top Voted), O(n) time and space
    # def isBalanced(self, root: TreeNode) -> bool:
    #     def check(root):
    #         if root is None:
    #             return 0
    #         left = check(root.left)
    #         right = check(root.right)
    #         if left == -1 or right == -1 or abs(left - right) > 1:
    #             return -1
    #         return 1 + max(left, right)

    #     return check(root) != -1
