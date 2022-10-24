import re


class Solution:
    # Manual Parse and Build (Accepted), O(n) time and space
    def interpret(self, command: str) -> str:
        res, i = "", 0
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
                i += 1
            else:
                if command[i+1] == ')':
                    res += 'o'
                    i += 2
                else:
                    res += 'al'
                    i += 4
        return res

    # In-Built String Replace (Top Voted), O(n) time and space
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')

    # Regex Substitution (Top Voted), O(n) time and space
    def interpret(self, command: str) -> str:
        return re.sub('\(\)', 'o', re.sub('\(al\)', 'al', command))
