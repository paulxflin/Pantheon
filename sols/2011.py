class Solution:
    # If-else (Accepted), O(n) time, O(1) space
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if op[1] == '+':
                x += 1
            else:
                x -= 1
        return x

    # One Liner (Top Voted), O(n) time, O(1) space
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(('+' in s) - ('-' in s) for s in operations)
