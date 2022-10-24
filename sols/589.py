"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # Recursive Traversal (Accepted), O(n) time and space
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        res = []

        def preorder_traversal(node):
            res.append(node.val)
            for child in node.children:
                preorder_traversal(child)
        preorder_traversal(root)
        return res

    # Iterative Stack Pop Extend (Top Voted), O(n) time and space
    def preorder(self, root: 'Node') -> List[int]:
        ret, q = [], root and [root]
        while q:
            node = q.pop()
            ret.append(node.val)
            q += [child for child in node.children[::-1] if child]
        return ret
