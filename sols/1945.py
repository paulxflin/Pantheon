class Solution:
    # Iterate chars in string and sum (Accepted), O(n) time and space
    def getLucky(self, s: str, k: int) -> int:
        transformed = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k):
            s = 0
            for c in transformed:
                s += int(c)
            transformed = str(s)
        return int(transformed)

    # Iterate chars in string and sum with LC (Accepted and Top Voted), O(n) time and space
    def getLucky(self, s: str, k: int) -> int:
        s = "".join(str(ord(x) - ord("a") + 1) for x in s)
        for _ in range(k):
            s = str(sum(int(x) for x in s))
        return s
