# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # # Build String + Convert to int (Accepted), O(n) time, O(n) space
    # def getDecimalValue(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: int
    #     """
    #     bin_str = ""
    #     curnode = head
    #     while curnode != None:
    #         bin_str += str(curnode.val)
    #         curnode = curnode.next
    #     return int(bin_str, 2)

    # # Bit Shift Left (Accepted), O(n) time, O(1) space
    # def getDecimalValue(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: int
    #     """
    #     res = 0
    #     while head != None:
    #         res <<= 1
    #         res += head.val
    #         head = head.next
    #     return res

    # # Bit shift + bitwise or (Top Voted), O(n) time, O(1) space
    # def getDecimalValue(self, head):
    #     ans = 0
    #     while head:
    #         ans = (ans << 1) | head.val
    #         head = head.next
    #     return ans

    # Python 3 Walrus (assignment) Operator + Bit Shift + bitwise or (Top Voted), O(n) time, O(1) space
    def getDecimalValue(self, head: ListNode) -> int:
        ans = head.val
        while head := head.next:
            ans = ans << 1 | head.val
        return ans
