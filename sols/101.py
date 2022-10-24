# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive (Accepted), O(n) time and space
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_sym(L, R):
            if L == R == None:
                return True
            if L and R:
                if L.val != R.val:
                    return False
                return is_sym(L.left, R.right) and is_sym(L.right, R.left)
            return False
        return is_sym(root.left, root.right)

    # Simple Recursive (Top Voted), O(n) time and space
    def isSymmetric(self, root):
        def isSym(L, R):
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R
        return not root or isSym(root.left, root.right)

    # Iterative Stack (Top Voted), O(n) time and space
    def isSymmetric(self, root):
        if root is None:
            return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])

                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True

    # Iterative Queue (Top Voted), O(n) time and space
    def isSymmetric(self, root):
        queue = [root]
        while queue:
            values = [i.val if i else None for i in queue]
            if values != values[::-1]:
                return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True
