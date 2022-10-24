# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # Reversed Second Half == First Half (Accepted), O(n) time, O(1) space
    # def isPalindrome(self, head: ListNode) -> bool:
    #     if not head or not head.next:
    #         return True

    #     slow = head
    #     fast = head.next
    #     length = 2

    #     while fast and fast.next:
    #         slow = slow.next
    #         if fast.next:
    #             fast = fast.next.next
    #             if fast:
    #                 length += 2
    #             else:
    #                 length += 1
    #         else:
    #             fast = fast.next

    #     prev = None
    #     slow = slow.next

    #     while slow.next:
    #         n = slow.next
    #         slow.next = prev
    #         prev = slow
    #         slow = n

    #     slow.next = prev

    #     end = slow
    #     start = head
    #     for i in range(length // 2):
    #         if start.val != end.val:
    #             return False
    #         start = start.next
    #         end = end.next
    #     return True

    # Reversed First Half == Second Half (Top Voted), O(n) time, O(1) space
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
