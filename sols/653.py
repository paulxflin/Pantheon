# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS (Accepted), O(n) time and space
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()

        def dfs(node):
            if node:
                nonlocal s
                if k - node.val in s:
                    return True
                else:
                    s.add(node.val)
                return dfs(node.left) or dfs(node.right)

        return dfs(root)

    # BFS (Top Voted), O(n) time and space
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s:
                return True
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False
