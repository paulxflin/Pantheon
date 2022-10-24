class Solution:
    # Right to Left Max (Accepted + Top Voted), O(n) time, O(1) space
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], greatest = greatest, max(arr[i], greatest)
        return arr
