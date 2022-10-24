class Solution:
    # Stack (Accepted), O(n) time and space
    def isValid(self, s: str) -> bool:
        l = []
        d = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in d.values():
                l.append(c)
            elif len(l) == 0 or d[c] != l.pop():
                return False
        return len(l) == 0

    # Stack with input check (Top voted), O(n) time and space
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in d.values():
                stack.append(char)
            elif char in d.keys():
                if stack == [] or d[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
