# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # # Recursive DFS (Accepted), O(n) time, O(h) space
    # def dfs(self, node, low, high, total):
    #     if not node:
    #         return total
    #     if node.val >= low:
    #         total = self.dfs(node.left, low, high, total)
    #         if node.val <= high:
    #             total += node.val
    #     if node.val <= high:
    #         total = self.dfs(node.right, low, high, total)
    #     return total

    # def rangeSumBST(self, root, low, high):
    #     """
    #     :type root: TreeNode
    #     :type low: int
    #     :type high: int
    #     :rtype: int
    #     """
    #     return self.dfs(root, low, high, 0)

    # Recursive dfs (Top Voted), O(n) time, O(h) space.
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        sum = 0
        if root.val > low:
            sum += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            sum += self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            sum += root.val
        return sum
