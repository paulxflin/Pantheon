class Solution:
    # Two Pointers (Accepted), O(n) time, O(n) space
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                if i == 0 or (i > 0 and typed[j] != name[i-1]):
                    return False
                else:
                    j += 1
            else:
                i, j = i+1, j+1
        if i < len(name):
            return False
        elif j < len(typed):
            return all(x == name[i-1] for x in typed[j:])
        else:
            return True

    # Two Pointers (Top Voted), O(n) time, O(1) space
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)
