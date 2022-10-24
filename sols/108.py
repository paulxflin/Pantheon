# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # Recursively build left right subtree (Accepted), O(n) time and space
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     if not nums:
    #         return None
    #     mid = len(nums) // 2
    #     head = TreeNode(nums[mid])
    #     if mid > 0:
    #         head.left = self.sortedArrayToBST(nums[:mid])
    #     if mid+1 < len(nums):
    #         head.right = self.sortedArrayToBST(nums[mid+1:])
    #     return head

    # Recursively build left right subtree (Top Voted), O(n) time and space
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
