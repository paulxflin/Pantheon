class Solution:
    # Sort and sum abs diff (Accepted), O(n log n) time, O(n) space
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        return res

    # Sum abs diff with zip (Top Voted), O(n log n) time, O(n) space
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(e - t) for e, t in zip(seats, students))
