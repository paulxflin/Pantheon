# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # Recursive (Accepted), O(n) time and space
    # def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    #     if root:
    #         targetSum -= root.val
    #         if not root.left and not root.right:
    #             return targetSum == 0
    #         else:
    #             return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    #     return False

    # Recursive Solution (Top Voted), O(n) time and space
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
