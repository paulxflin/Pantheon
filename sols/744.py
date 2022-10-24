import bisect


class Solution:
    # # Binary Search (Accepted), O(log n) time, O(1) space
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     if not letters:
    #         return None
    #     low, high = 0, len(letters)-1
    #     while low < high:
    #         mid = (low + high) // 2
    #         if letters[mid] > target:
    #             high = mid
    #         else:
    #             low = mid+1
    #     return letters[low] if letters[low] > target else letters[0]

    # Binary Search with Bisect (Top Voted), O(log n) time, O(1) space
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        pos = bisect.bisect_right(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]
