class Solution:
    # One Pass (Accepted), O(n log n) time, O(n) space
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_diff = float(inf)
        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                res.append([arr[i], arr[i+1]])
        return res

    # Three Liner (Top Voted), O(n log n) time, O(n) space
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]
