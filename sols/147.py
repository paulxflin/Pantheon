# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # # Pure Insertion Sort (Accepted), O(n^2) time, O(1) space
    # def find_and_insert(self, cur, ind, head):
    #     prev = None
    #     node = head
    #     if node.val > cur.val:
    #         cur.next = node
    #         head = cur
    #         return head
    #     for i in range(ind):
    #         if not node:
    #             cur.next = node
    #             prev.next = cur
    #             return head
    #         elif node.next and cur.val < node.next.val:
    #             cur.next = node.next
    #             node.next = cur
    #             return head
    #         prev = node
    #         node = node.next
    #     # No suitable position found
    #     cur.next = node
    #     prev.next = cur
    #     return head

    # def insertionSortList(self, head: ListNode) -> ListNode:
    #     prev = head
    #     cur = head.next
    #     ind = 1
    #     while cur is not None:
    #         if prev:
    #             prev.next = cur.next
    #         head = self.find_and_insert(cur, ind, head)
    #         prev = cur if prev.next == cur else prev
    #         cur = prev.next
    #         ind += 1
    #     return head

    # # Lazy (disorders) Insertion Sort (Accepted), O(n^2) time, O(1) space (10x improvement from above)
    # def find_and_insert(self, cur, ind, head):
    #     prev = None
    #     node = head
    #     if node.val > cur.val:
    #         cur.next = node
    #         head = cur
    #         return head
    #     for i in range(ind):
    #         if not node:
    #             cur.next = node
    #             prev.next = cur
    #             return head
    #         elif node.next and cur.val < node.next.val:
    #             cur.next = node.next
    #             node.next = cur
    #             return head
    #         prev = node
    #         node = node.next
    #     # No suitable position found
    #     cur.next = node
    #     prev.next = cur
    #     return head

    # def insertionSortList(self, head: ListNode) -> ListNode:
    #     prev = head
    #     cur = head.next
    #     ind = 1
    #     while cur is not None:
    #         if prev.val > cur.val:
    #             if prev:
    #                 prev.next = cur.next
    #             head = self.find_and_insert(cur, ind, head)
    #             prev = cur if prev.next == cur else prev
    #         else:
    #             prev = cur
    #         cur = prev.next
    #         ind += 1
    #     return head

    # # Dummy + Predecessors + Disorders (Revisited), O(n^2) time, O(1) space
    # def insertionSortList(self, head: ListNode) -> ListNode:
    #     dummy = ListNode(0, head)
    #     cur = head
    #     while cur.next is not None:
    #         if cur.val > cur.next.val:
    #             to_insert = cur.next
    #             cur.next = cur.next.next

    #             # Find predecessor for insertion
    #             pred = dummy
    #             while pred.next.val < to_insert.val:
    #                 pred = pred.next

    #             # insert in pred
    #             to_insert.next = pred.next
    #             pred.next = to_insert

    #         else:
    #             cur = cur.next

    #     return dummy.next

    # Dummy + Predecessor + Disorders (Top Voted), O(n^2) time, O(1) space
    def insertionSortList(self, head):

        dummyHead = ListNode(0)
        dummyHead.next = nodeToInsert = head

        while head and head.next:
            if head.val > head.next.val:
                # Locate nodeToInsert.
                nodeToInsert = head.next
                # Locate nodeToInsertPre.
                nodeToInsertPre = dummyHead
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next

                head.next = nodeToInsert.next
                # Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next

        return dummyHead.next
