class Solution:
    # One Pass (Accepted), O(n) time, O(1) space
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prev, res, longest = 0, None, 0
        for i in range(len(keysPressed)):
            dur = releaseTimes[i] - prev
            if dur > longest or (dur == longest and keysPressed[i] > res):
                longest, res = dur, keysPressed[i]
            prev = releaseTimes[i]
        return res

    # One Pass (Top Voted), O(n) time, O(1) space
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        k, t = keysPressed[0], releaseTimes[0]

        for i in range(1, len(keysPressed)):
            time = releaseTimes[i] - releaseTimes[i-1]
            if time > t or (time == t and keysPressed[i] > k):
                t = time
                k = keysPressed[i]

        return k
