# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # # Iterative (accepted), Time: O(m + n), Space: O(1)
    # def insert(self, pos_node, node):
    #     node.next = pos_node.next
    #     pos_node.next = node

    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     # Handle Base Case
    #     if l1 is None:
    #         return l2
    #     elif l2 is None:
    #         return l1

    #     root = l1 if l1.val < l2.val else l2
    #     other = l2 if root is l1 else l1
    #     cur = root

    #     while cur.next:
    #         if other and other.val < cur.next.val:
    #             self.insert(cur, ListNode(other.val, other.next))
    #             other = other.next
    #         cur = cur.next
    #     while other:
    #         self.insert(cur, ListNode(other.val, other.next))
    #         cur = cur.next
    #         other = other.next
    #     return root

    # # Recursive (Top Voted), Time: O(m + n), Space: O(m + n)
    # def mergeTwoLists(self, l1, l2):
    #     if not l1 or not l2:
    #         return l1 or l2
    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

    # Iterative (Top Voted), Time: O(m + n), Space: O(1)
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
