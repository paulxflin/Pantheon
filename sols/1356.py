class Solution:
    # Sorting key function (Accepted), O(n log n) time, O(n) space
    def sortByBits(self, arr: List[int]) -> List[int]:
        def tup(n):
            return (bin(n).count('1'), n)
        return sorted(arr, key=tup)

    # One Liner (Top Voted), O(n log n) time, O(n) space
    def sortByBits(self, A):
        return sorted(A, key=lambda a: (bin(a).count('1'), a))
