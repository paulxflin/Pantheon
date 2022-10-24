class Solution:
    # One Pass (Accepted), O(n) time, O(1) space
    def average(self, salary: List[int]) -> float:
        max_, min_, sum_ = -float('inf'), float('inf'), 0
        for n in salary:
            sum_ += n
            if n > max_:
                max_ = n
            if n < min_:
                min_ = n
        return (sum_ - max_ - min_) / (len(salary)-2)

    # Inbuilt Functions (Top Voted), O(n) time, O(1) space
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
