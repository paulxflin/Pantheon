class Solution:
    # Defaultdict (Accepted), O(1) time and space
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(int)
        for u, v in edges:
            d[u] += 1
            d[v] += 1
            if d[u] > 1:
                return u
            if d[v] > 1:
                return v

    # Set (Top Voted), O(1) time and space
    def findCenter(self, e):
        return (set(e[0]) & set(e[1])).pop()

    # Contains (Top Voted), O(1) time and space
    def findCenter(self, e):
        return e[0][e[0][1] in e[1]]
