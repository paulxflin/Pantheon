# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # Two Pointers (Accepted), O(n) time, O(1) space
    # def middleNode(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return None
    #     slow = fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow

    # Two Pointers (Top Voted), O(n) time, O(1) space
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
