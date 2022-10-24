# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # Brute Force (Accepted), O(n^2) time, O(n) space
    # res = 0
    # def findTilt(self, root: TreeNode) -> int:
    #     def get_sum(node, res):
    #         if node:
    #             res += node.val
    #             res = get_sum(node.left, res)
    #             res = get_sum(node.right, res)
    #         return res

    #     def tilt(root):
    #         if root:
    #             return abs(get_sum(root.left, 0) - get_sum(root.right, 0))
    #         return 0

    #     def dfs(node):
    #         if node:
    #             self.res += tilt(node)
    #             dfs(node.left)
    #             dfs(node.right)

    #     if not root:
    #         return 0

    #     dfs(root)
    #     return self.res

    # # Brute Force with Memo (Accepted), O(n) time and space
    # res = 0
    # memo = {}
    # def findTilt(self, root: TreeNode) -> int:
    #     def get_sum(node):
    #         if node in self.memo:
    #             return self.memo[node]
    #         s = 0
    #         if node:
    #             s += node.val + get_sum(node.left) + get_sum(node.right)
    #         self.memo[node] = s
    #         return s

    #     def tilt(root):
    #         if root:
    #             return abs(get_sum(root.left) - get_sum(root.right))
    #         return 0

    #     def dfs(node):
    #         if node:
    #             self.res += tilt(node)
    #             dfs(node.left)
    #             dfs(node.right)

    #     if not root:
    #         return 0

    #     dfs(root)
    #     return self.res

    # # Single Function DFS, tilt, sum (Top Voted), O(n) time and space
    # def findTilt(self, root: TreeNode) -> int:
    #     self.ans = 0
    #     def _sum(node):
    #         if not node: return 0
    #         left, right = _sum(node.left), _sum(node.right)
    #         self.ans += abs(left - right)
    #         return node.val + left + right
    #     _sum(root)
    #     return self.ans

    # Post-Order DFS Traversal (Solution), O(n) time and space
    def findTilt(self, root: TreeNode) -> int:
        total_tilt = 0

        def valueSum(node):
            nonlocal total_tilt

            if not node:
                return 0

            left_sum = valueSum(node.left)
            right_sum = valueSum(node.right)
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt

            return left_sum + right_sum + node.val

        valueSum(root)

        return total_tilt
