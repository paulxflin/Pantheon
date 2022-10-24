from collections import deque


class Solution:
    # # Deque (Accepted), O(n) time and space
    # def diStringMatch(self, s: str) -> List[int]:
    #     queue = deque(range(len(s)+1))
    #     res = []
    #     for c in s:
    #         if c == 'I':
    #             res.append(queue.popleft())
    #         else:
    #             res.append(queue.pop())
    #     if queue:
    #         res.append(queue.pop())
    #     return res

    # Ad-Hoc (Solution), O(n) time and space
    def diStringMatch(self, S: str) -> List[int]:
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]
