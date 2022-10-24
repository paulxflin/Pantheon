class Solution:
    # Split and Compare against prev (Accepted), O(n) time and space
    def areNumbersAscending(self, s: str) -> bool:
        prev = -float('inf')
        for part in s.split():
            if part.isnumeric():
                if int(part) > prev:
                    prev = int(part)
                else:
                    return False
        return True

    # Two Liner (Top Voted), O(n) time and space
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(w) for w in s.split() if w.isdigit()]
        return all(nums[i-1] < nums[i] for i in range(1, len(nums)))
