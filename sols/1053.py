class Solution:
    # Nested for loops (Accepted), O(n) time, O(1) space
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                swp1 = i
                swp2 = i+1
                for j in range(i+2, len(arr)):
                    if arr[swp2] < arr[j] < arr[i]:
                        swp2 = j
                arr[swp1], arr[swp2] = arr[swp2], arr[swp1]
                return arr
        return arr

    # Easy Linear (Top Voted), O(n) time, O(1) space
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        i = len(A) - 2
        while i >= 0 and A[i] <= A[i+1]:
            i -= 1
        if i >= 0:
            max_ = i + 1
            # max number greater on right that less than A[i]
            for j in range(max_ + 1, len(A)):
                if A[max_] < A[j] < A[i]:
                    max_ = j
            A[max_], A[i] = A[i], A[max_]
        return A
