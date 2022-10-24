class Solution:
    # Check level inside main (Accepted), O(n) time and space
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for cmd in logs:
            if cmd == '../':
                if level:
                    level -= 1
            elif cmd != './':
                level += 1
        return level

    # Check depth into subfolders (Top Voted), O(n) time and space
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == '../':
                depth = max(0, depth - 1)
            elif log != './':
                depth += 1
        return depth
