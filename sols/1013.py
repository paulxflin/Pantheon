class Solution:
    # Greedy Two Pointers (Accepted), O(n) time, O(1) space
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        total = sum(arr)
        target = total / 3
        a, b = 0, len(arr)-1
        a_tot = b_tot = 0
        while a_tot != target or a == 0:
            if a >= len(arr):
                return False
            a_tot += arr[a]
            a += 1

        while b_tot != target or b == len(arr)-1:
            if b < 0:
                return False
            b_tot += arr[b]
            b -= 1

        return a <= b

    # Count Valid Parts (Top Voted), O(n) time, O(1) space
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        average, remainder, part, cnt = sum(A) // 3, sum(A) % 3, 0, 0
        for a in A:
            part += a
            if part == average:
                cnt += 1
                part = 0
        return not remainder and cnt >= 3
