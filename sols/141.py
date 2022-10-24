# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # # Hashmap (Accepted), O(n) time, O(n) space
    # def hasCycle(self, head: ListNode) -> bool:
    #     visited = {}
    #     cur = head
    #     while cur != None:
    #         if cur not in visited:
    #             visited[cur] = True
    #         else:
    #             return True
    #         cur = cur.next
    #     return False

    # # Tortoise and Hare two checks (Accepted), O(n) time, O(1) space
    # def hasCycle(self, head: ListNode) -> bool:
    #     if not head or head.next == None:
    #         return False
    #     slow = head
    #     fast = head.next.next

    #     while fast and fast.next:
    #         if fast == slow or fast == slow.next:
    #             return True
    #         slow = slow.next
    #         fast = fast.next.next
    #     return False

    # Tortoise and Hare + Except (Top Voted), O(n) time, O(1) space
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
