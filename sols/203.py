# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Single Pointer, Dummy Head (Accepted), O(n) time, O(1) space
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        cur = dummy = ListNode(0, head)
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

    # # Single Pointer, Dummy Head (Top Voted), O(n) time, O(1) space
    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     dummy_head = ListNode(-1)
    #     dummy_head.next = head

    #     current_node = dummy_head
    #     while current_node.next != None:
    #         if current_node.next.val == val:
    #             current_node.next = current_node.next.next
    #         else:
    #             current_node = current_node.next

    #     return dummy_head.next
