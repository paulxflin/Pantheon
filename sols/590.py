"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # Recursion (Accepted), O(n) time and space
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res

        def po_traversal(node):
            for n in node.children:
                po_traversal(n)
            res.append(node.val)

        po_traversal(root)
        return res

    # Recursion (Top Voted), O(n) time and space
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None:
            return res

        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)

        recursion(root, res)
        return res

    # Iterative (Top Voted), O(n) time and space
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None:
            return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)

        return res[::-1]
