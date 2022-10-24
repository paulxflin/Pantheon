from collections import Counter


class Solution:
    # Stop when nobody wants top (Accepted), O(n) time, O(1) space
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        for i, s in enumerate(sandwiches):
            if cnt[s] > 0:
                cnt[s] -= 1
            else:
                return len(sandwiches) - i
        return 0

    # Concise (Top Voted), O(n) time, O(1) space
    def countStudents(self, A: List[int], B: List[int]) -> int:
        count = Counter(A)
        n, k = len(A), 0
        while k < n and count[B[k]]:
            count[B[k]] -= 1
            k += 1
        return n - k
