class Solution:
    # Sort and Iterate (Accepted), O(n log n) time, O(n) space
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        A = sorted(arr)
        d = A[1] - A[0]
        for i in range(1, len(A)-1):
            if A[i+1] - A[i] != d:
                return False
        return True

    # Find Gap and Swap (Top Voted), O(n) time, O(1) space
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        m = min(arr)
        gap = (max(arr) - m) / (len(arr) - 1)
        if gap == 0:
            return True
        i = 0
        while i < len(arr):
            if arr[i] == m + i * gap:
                i += 1
            else:
                dis = arr[i] - m
                if dis % gap != 0:
                    return False
                pos = int(dis / gap)
                if arr[pos] == arr[i]:
                    return False
                arr[pos], arr[i] = arr[i], arr[pos]
        return True
