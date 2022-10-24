class Solution:
    # # Map the reversed row (Accepted), O(n) time, O(n) space
    # def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    #     for i in range(len(image)):
    #         image[i] = map(lambda x: 0 if x == 1 else 1, image[i][::-1])
    #     return image

    # Direct In Place (Solution), O(n) time, O(1) additional space, n is total number of elems in A
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for i in range((len(row) + 1) // 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
