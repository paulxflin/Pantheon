class Solution:
    # Optimised Row by Row (Accepted), O(n) time and space, where n = total elems in pascal triangle
    def generate(self, numRows: int) -> List[List[int]]:
        n, res = 1, [[1]]
        while n < numRows:
            n += 1
            l = [1]*n
            for i in range((n-1)//2):
                l[i+1] = l[n-2-i] = res[n-2][i] + res[n-2][i+1]
            res.append(l)
        return res

    # Map (Top Voted), O(n) time and space
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res.append(
                list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])))
        return res

    # 4 Liner (Top Voted), O(n) time and space
    def generate(self, numRows):
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
