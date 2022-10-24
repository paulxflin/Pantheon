class Solution:
    # Iterative (Accepted), O(n) time, O(1) space
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur != None:
            prev, cur.next, cur = cur, prev, cur.next
        return prev
