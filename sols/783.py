# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # In Order Traversal (Accepted), O(n) time and space
    # def minDiffInBST(self, root: TreeNode) -> int:
    #     res = math.inf
    #     li = []

    #     def dfs(root):
    #         if root.left:
    #             dfs(root.left)
    #         li.append(root.val)
    #         if root.right:
    #             dfs(root.right)
    #     dfs(root)
    #     for i in range(len(li)-1):
    #         diff = li[i+1] - li[i]
    #         if diff < res:
    #             res = diff
    #     return res

    # # In Order Traversal (Sample), O(n) time and space
    # def minDiffInBST(self, root: TreeNode) -> int:
    #     vals = []

    #     def inorder(node):
    #         if node:
    #             inorder(node.left)
    #             vals.append(node.val)
    #             inorder(node.right)

    #     inorder(root)
    #     print(vals)
    #     min_ = 999999999
    #     # return vals[1] - vals[0]
    #     for i in range(1, len(vals)):
    #         if min_ > (vals[i]-vals[i-1]):
    #             min_ = vals[i]-vals[i-1]

    #     return min_

    # In Order Traversal (Top Voted), O(n) time, O(h) space
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res
