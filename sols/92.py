# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # Iterative with new linked list (Accepted), O(n) time, O(n) space
    # def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    #     def insert_after(prev, node):
    #         new_node = ListNode(node.val, prev.next)
    #         prev.next = new_node
    #         return new_node

    #     if left == right:
    #         return head

    #     dummy = ListNode(0, head)
    #     prior = dummy
    #     after = None
    #     cur = dummy
    #     ind = 0
    #     new_dummy = None
    #     new_tail = None
    #     # One pass to find prior and after
    #     while cur:
    #         if ind == left - 1:
    #             prior = cur
    #             new_dummy = ListNode(0, None)
    #         if left == ind:
    #             new_tail = insert_after(new_dummy, cur)
    #         if left < ind <= right:
    #             insert_after(new_dummy, cur)
    #         if ind == right + 1:
    #             after = cur
    #         ind += 1
    #         cur = cur.next

    #     prior.next = new_dummy.next
    #     new_tail.next = after

    #     return dummy.next

    # # Iterative In Place Approach (Top Voted), O(n) time, O(1) space
    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    #     if not head or m == n: return head
    #     p = dummy = ListNode(None) # p is elem prior to the left
    #     dummy.next = head
    #     for i in range(m-1): p = p.next # Iterates to prior without the fancy ind
    #     tail = p.next # The next element which is left will be the tail

    #     for i in range(n-m):
    #         tmp = p.next                  # a) Set elem after prior as tmp
    #         p.next = tail.next            # b) insert next elem after prior
    #         tail.next = tail.next.next    # c) iterate tail.next
    #         p.next.next = tmp             # d) set the moved node's next elem
    #     return dummy.next

    # Iterative In Place Approach (Sample), O(n) time, O(1) space
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        p = dummy = ListNode(0)
        dummy.next = head

        for _ in range(left-1):
            p = p.next
        cur = p.next
        prev = None

        for _ in range(right - left + 1):
            cur.next, cur, prev = prev, cur.next, cur
        p.next.next = cur
        p.next = prev
        return dummy.next
