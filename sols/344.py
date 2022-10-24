class Solution:
    # Two Pointers (Accepted), O(n) time, O(1) space
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    # One Pointer with Complement (Accepted), O(n) time, O(1) space
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]

    # One Pointer with manual Complement (Top Voted), O(n) time, O(1) space
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]

    # Libary Reverse (Solution), O(n) time, O(1) space
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
