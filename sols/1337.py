from heapq import heappushpop, heappush, heappop


class Solution:
    # # Search every item in a column (Accepted), O(m * n) time, O(k) space
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     res = []
    #     for col in range(len(mat[0])):
    #         for row in range(len(mat)):
    #             if mat[row][col] == 0 and row not in res:
    #                 res.append(row)
    #             if len(res) == k:
    #                 return res
    #     else:
    #         for row in range(len(mat)):
    #             if row not in res:
    #                 res.append(row)
    #             if len(res) == k:
    #                 return res
    #     return res

    # # Binary Search (Accepted), O(m * (log n + log m) + k) time, O(m + k) space
    # def find_num_soldier(self, row, left=0, right=None):
    #     right = len(row)-1 if right == None else right
    #     if left < right:
    #         mid = (left + right) // 2
    #         if row[mid] == 0:
    #             pos = self.find_num_soldier(row, left, mid)
    #         else:
    #             pos = self.find_num_soldier(row, mid + 1, right)
    #     else:
    #         if row[right] == 0:
    #             pos = right
    #         else:
    #             pos = right + 1
    #     return pos

    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     res = []
    #     num_soldiers = []
    #     for row in range(len(mat)):
    #         num_soldiers.append((self.find_num_soldier(mat[row]), row))
    #     num_soldiers.sort()

    #     for i in range(k):
    #         res.append(num_soldiers[i][1])
    #     return res

    # # One Liner Ordering Index by Sum of Rows (Top Voted), O(m * (n + log m)) time, O(m) space
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]

    # Heap + Binary Search (Top Voted), O(m * (log n + log k) + k log k) time, O(k) space
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []  # Size: O(k)

        # Iterate over the rows in O(m).
        for index, row in enumerate(mat):
            soldier_count = self.soldier_count(row)

            # Push values to the heap in O(log k)
            if len(heap) == k:
                heappushpop(heap, (-soldier_count, -index))
            else:
                heappush(heap, (-soldier_count, -index))

        weakest_rows = []  # Size: O(k)

        # Push the heap values into our result list in O(k log k).
        while heap:
            weakest_rows.append(-heappop(heap)[1])

        # Return the result in reversed order.
        return weakest_rows[::-1]

    # Find the number of soldiers in a row using Binary Search in O(log n).
    def soldier_count(self, row: List[int]) -> int:
        low, high = 0, len(row) - 1

        while low < high:
            mid = (low + high + 1) // 2

            if not row[mid]:
                high = mid - 1
            else:
                low = mid

        # We need to return a count and not an index.
        # Therefore we need to increase the result by one if soldiers have been found.
        if row[0]:
            low += 1

        return low

    # # Optimised One Liner with Heap (Top Voted), O(m * n + (m + k) log k) time, O(k) space
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     return [x[1] for x in heapq.nsmallest(k, ((sum(s), i) for i, s in enumerate(mat)))]

    # # Vertical Traversal + Collect from small index (Top Voted), O(m * n) time, O(k) space
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     m, n = len(mat), len(mat[0])
    #     result = {}
    #     for j in range(n):
    #         for i in range(m):
    #             if mat[i][j] or i in result: continue
    #             result[i] = True
    #             k -= 1
    #             if not k: return result.keys()
    #     for i in range(m):
    #         if i not in result:
    #             result[i] = True
    #             k -= 1
    #             if not k: return result.keys()
