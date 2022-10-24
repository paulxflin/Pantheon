class Solution:
    # Track x, y (Accepted), O(n) time, O(1) space
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
            else:
                x += 1
        return x == y == 0

    # One Liner (Top Voted), O(n) time, O(1) space
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
