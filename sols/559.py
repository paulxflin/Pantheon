from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    # # Recursive DFS (Accepted), O(n) time, O(n) space
    # def dfs(self, node, depth):

    #     depth += 1
    #     max_depth = depth
    #     for n in node.children:
    #         ret = self.dfs(n, depth)
    #         if ret > max_depth:
    #             max_depth = ret
    #     return max_depth

    # def maxDepth(self, root):
    #     """
    #     :type root: Node
    #     :rtype: int
    #     """
    #     if not root:
    #         return 0
    #     return self.dfs(root, 0)

    # # Recursive DFS (Top Voted), O(n) time, O(n) space
    # def maxDepth(self, root):
    #     # Base case
    #     if root == None:
    #         return 0
    #     # Depth level of the tree
    #     depth = 0

    #     # Loops through children array
    #     for child in root.children:
    #         # Compares current depth of depth with a new level of depth
    #         # Sets the biggest value to variable depth
    #         depth = max(depth, self.maxDepth(child))

    #     # As going deeper into the tree increases depth by 1
    #     print('root ' + str(root.val) + ' depth ' + str(depth + 1))
    #     return depth + 1

    # BFS (Sample), O(n) time and space
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        cur_depth = 0
        q = deque()
        if root is None:
            return cur_depth
        q.append(root)
        while len(q) > 0:
            cur_depth += 1
            for i in range(len(q)):
                s = q.popleft()
                for child in s.children:
                    if child is not None:
                        q.append(child)
        return cur_depth
