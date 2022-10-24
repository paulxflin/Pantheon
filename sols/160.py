# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Two Pointers Two Passes, O(n) time, O(1) space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        a_runs = 0
        b_runs = 0
        while a_runs < 2 and b_runs < 2:
            if a == b:
                return a
            if a.next == None:
                a_runs += 1
                a = headB
            else:
                a = a.next
            if b.next == None:
                b_runs += 1
                b = headA
            else:
                b = b.next
        return None

    # Concise two pointers (Top Voted), O(n) time, O(1) space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        pa, pb = headA, headB

        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa
