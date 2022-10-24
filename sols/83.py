# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # Two pointer solution (Accepted), O(n) time, O(1) space
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return None
    #     elif not head.next:
    #         return head
    #     prev = head
    #     cur = prev.next
    #     while cur != None:
    #         if cur.val == prev.val:
    #             prev.next = cur.next
    #             cur = cur.next
    #         else:
    #             prev = cur
    #             cur = cur.next
    #     return head

    # One pointer (Top Voted), O(n) time, O(1) space
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
