class Solution:
    # Map offset lists (Accepted), O(n^2) time, O(n) space
    def getRow(self, rowIndex: int) -> List[int]:
        n, l = 0, [1]
        while n < rowIndex:
            l = list(map(lambda x, y: x+y, [0] + l, l+[0]))
            n += 1
        return l

    # Symmetry Solution (Accepted), O(n^2) time, O(n) space
    def getRow(self, rowIndex: int) -> List[int]:
        l = [1]*(rowIndex+1)
        for n in range(1, rowIndex+1):
            for i in range((n+2)//2-1, 0, -1):
                l[i] = l[n-i] = l[i-1]+l[i]
        return l

    # Zip addition (Top Voted), O(n^2) time, O(n) space
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
