from itertools import accumulate


class Solution:
    # Append to res (Accepted), O(n) time and space
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for v in encoded:
            res.append(res[-1] ^ v)
        return res

    # In Place (Accepted), O(n) time, O(1) space
    def decode(self, A, first):
        A = [first] + A
        for i in range(1, len(A)):
            A[i] = A[i-1] ^ A[i]
        return A

    # Accumulate (Top Voted), O(n) time and space
    def decode(self, A, first):
        return list(accumulate([first] + A, lambda x, y: x ^ y))
