class Solution:
    # # Add relevant pixes to an array and fill all, O(n) time and space
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    #     if not image:
    #         return None
    #     m, n = len(image), len(image[0])
    #     col = image[sr][sc]
    #     to_fill = []

    #     def add_pix(r, c):
    #         if (r, c) not in to_fill:
    #             to_fill.append((r, c))
    #         else:
    #             return
    #         if r-1 >= 0 and image[r-1][c] == col:
    #             add_pix(r-1, c)
    #         if r+1 < m and image[r+1][c] == col:
    #             add_pix(r+1, c)
    #         if c-1 >= 0 and image[r][c-1] == col:
    #             add_pix(r, c-1)
    #         if c+1 < n and image[r][c+1] == col:
    #             add_pix(r, c+1)

    #     add_pix(sr, sc)

    #     for r, c in to_fill:
    #         image[r][c] = newColor

    #     return image

    # DFS (Top Voted), O(n) time and space
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]

        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y)
             for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
        if orig_color != newColor:
            traverse(sr, sc)
        return image
