# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative (Accepted), O(n) time and space
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        level = [root]
        while level != []:
            total = 0
            new_level = []
            for node in level:
                total += node.val
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            res.append(total / len(level))
            level = new_level
        return res

    # DFS (Top Voted), O(n) time and space
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        info = []

        def dfs(node, depth=0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]
