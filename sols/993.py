from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # # BFS (Accepted), O(n) time, O(n) space
    # def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    #     def update_res(node, level):
    #         if node:
    #             queue.append((node, level))
    #             if node.val == x:
    #                 res[0] = level
    #                 return True
    #             elif node.val == y:
    #                 res[1] = level
    #                 return True
    #         return False

    #     queue = deque()
    #     queue.append((root, 0)) #append (node, level)
    #     res = [None] * 2
    #     update_res(root, 0)
    #     while queue:
    #         cur_node, level = queue.popleft()
    #         ret1 = update_res(cur_node.left, level+1)
    #         ret2 = update_res(cur_node.right, level+1)
    #         if ret1 and ret2:
    #             return False
    #     return res[0] == res[1]

    # # BFS (Top Voted), O(n) time, O(n) space
    # def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    #     nodes = collections.defaultdict(list)
    #     queue = [(root,0,0)]
    #     while queue:
    #         node,level,parent = queue.pop(0)
    #         nodes[node.val] = [level,parent]

    #         if node.left:
    #             queue.append((node.left,level+1,node.val))
    #         if node.right:
    #             queue.append((node.right,level+1,node.val))

    #     if nodes[x][0]==nodes[y][0] and nodes[x][1] != nodes[y][1]:
    #         return True

    #     return False

    # DFS (Top Voted), O(n) time, O(h) space
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, parent, depth, mod):
            if node:
                if node.val == mod:
                    return depth, parent
                return dfs(node.left, node, depth + 1, mod) or dfs(node.right, node, depth + 1, mod)
        dx, px, dy, py = dfs(root, None, 0, x) + dfs(root, None, 0, y)
        return dx == dy and px != py
