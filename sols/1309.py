import collections
import re


class Solution:
    # Chr + Ord + Iterative + Deque (Accepted), O(n) time and space
    def freqAlphabets(self, s: str) -> str:
        queue = collections.deque()
        i = len(s)-1
        while i >= 0:
            if s[i] == '#':
                queue.appendleft(chr(ord('a') + int(s[i-2:i]) - 1))
                i -= 3
            else:
                queue.appendleft(chr(ord('a') + int(s[i]) - 1))
                i -= 1
        return ''.join(queue)

    # Chr + Ord + Regex + Listcomp (Top Voted), O(n) time and space
    def freqAlphabets(self, s: str) -> str:
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall('\d\d#|\d', s))
