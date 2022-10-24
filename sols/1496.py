import operator


class Solution:
    # Coord + Set (Accepted), O(n) time and space
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x, y = 0, 0
        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            else:
                x -= 1
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False

    # List coord + Set (Accepted), O(n) time and space
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        coord = [0, 0]
        d = {'N': (1, 1), 'S': (1, -1), 'E': (0, 1), 'W': (0, -1)}
        for c in path:
            coord[d[c][0]] += d[c][1]
            point = (coord[0], coord[1])
            if point in visited:
                return True
            else:
                visited.add(point)
        return False

    # Concise Tuple coord + Set + Map (Top Voted), O(n) time and space
    def isPathCrossing(self, path: str) -> bool:
        cur = (0, 0)
        seen = {cur}
        dir = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for char in path:
            cur = tuple(map(operator.add, cur, dir[char]))
            if cur in seen:
                return True
            seen.add(cur)
        return False
