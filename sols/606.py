# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Inner Function (Accepted), O(n) time and space
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def expand_node(node):
            if node != None:
                res = str(node.val)
                if node.left == node.right == None:
                    return res
                else:
                    res += f'({expand_node(node.left)})'
                    if node.right:
                        res += f'({expand_node(node.right)})'
                return res
            return ''
        return expand_node(root)

    # Format class function recursion (Top Voted), O(n) time and space
    def tree2str(self, t: Optional[TreeNode]) -> str:
        if not t:
            return ''
        left = '({})'.format(self.tree2str(t.left)) if (
            t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)

    # F-String class function recursion (Top Voted + Accepted), O(n) time and space
    def tree2str(self, t: Optional[TreeNode]) -> str:
        if not t:
            return ''
        left = f'({self.tree2str(t.left)})' if (t.left or t.right) else ''
        right = f'({self.tree2str(t.right)})' if t.right else ''
        return f'{t.val}{left}{right}'
