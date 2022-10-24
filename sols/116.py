"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # Set Each Level (Accepted), O(n) time and space
    def connect(self, root: 'Node') -> 'Node':
        cur_level = [root]
        while cur_level[0] != None:
            new_level = []
            for i in range(len(cur_level)-1):
                cur_level[i].next = cur_level[i+1]
            if cur_level[0].left == None:
                return root
            for node in cur_level:
                new_level += [node.left, node.right]
            cur_level = new_level
        return root

    # Use Next (Top Voted), O(n) time, O(1) space
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node and node.left:
            next_ = node.left
            while node:
                node.left.next = node.right
                node.right.next = node.next and node.next.left
                node = node.next
            node = next_
        return root
