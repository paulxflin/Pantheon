# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # # Recursion (Accepted), time O(n), space worst O(n), average O(log n)
    # def add_children(self, r, node):
    #     if node.left is not None:
    #         self.add_children(r, node.left)
    #     r.append(node.val)
    #     if node.right is not None:
    #         self.add_children(r, node.right)

    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     r = []
    #     if root is not None:
    #         self.add_children(r, root)
    #     return r

    # # Iterative (Accepted), O(n) time, O(n) space
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     r = []
    #     stack = []
    #     visited = []
    #     if root is not None:
    #         stack.append(root)
    #         cur_node = root
    #         visited.append(cur_node)
    #         while stack:
    #             visited.append(cur_node)
    #             if cur_node.left is not None and cur_node.left not in visited:
    #                 stack.append(cur_node.left)
    #                 cur_node = cur_node.left
    #             elif cur_node.right is not None and cur_node.right not in visited:
    #                 r.append(stack.pop(-1).val)
    #                 stack.append(cur_node.right)
    #                 cur_node = cur_node.right
    #             else:
    #                 r.append(stack.pop(-1).val)
    #                 if stack:
    #                     cur_node = stack[-1]
    #                 else:
    #                     return r

    #     return r

    # # Iterative (Solution), O(n) time, O(n) space
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     res = []
    #     stack = []
    #     curr = root
    #     while curr is not None or len(stack) != 0:
    #         while curr is not None:
    #             stack.append(curr)
    #             curr = curr.left
    #         curr = stack.pop(-1)
    #         res.append(curr.val)
    #         curr = curr.right
    #     return res

    # Iterative (Top Voted), O(n) time, O(n) space
    def inorderTraversal(self, root):
        ans = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans.append(tmpNode.val)
                root = tmpNode.right

        return ans
