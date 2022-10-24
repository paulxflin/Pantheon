from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # BFS (Accepted), O(n) time, O(n) space
    def minDepth(self, root: TreeNode) -> int:
        queue = deque()
        if root:
            queue.append((root, 1))
        else:
            return 0
        while queue:
            cur_node, depth = queue.popleft()
            if not cur_node.left and not cur_node.right:
                return depth
            if cur_node.left:
                queue.append((cur_node.left, depth + 1))
            if cur_node.right:
                queue.append((cur_node.right, depth + 1))

    # # BFS (Top Voted), O(n) time, O(n) space
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     queue = collections.deque([(root, 1)])
    #     while queue:
    #         node, level = queue.popleft()
    #         if node:
    #             if not node.left and not node.right:
    #                 return level
    #             else:
    #                 queue.append((node.left, level+1))
    #                 queue.append((node.right, level+1))

    # # DFS (Top Voted), O(n) time, O(n) space
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root: return 0
    #     d = list(map(self.minDepth, (root.left, root.right)))
    #     return 1 + (min(d) or max(d))
