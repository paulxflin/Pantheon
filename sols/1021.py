class Solution(object):
    # # Open = Closed (Accepted), O(n) time and space
    # def removeOuterParentheses(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     n = 0
    #     ret_str = ""
    #     sub_str = ""
    #     for c in s:
    #         sub_str += c
    #         if c == '(':
    #             n += 1
    #         elif c == ')':
    #             n -= 1
    #         if n == 0:
    #             ret_str += sub_str[1:-1]
    #             sub_str = ""
    #     return ret_str

    # String Join (Top Voted), O(n) time and space
    def removeOuterParentheses(self, s):
        res, opened = [], 0
        for c in s:
            if c == '(' and opened > 0:
                res.append(c)
            if c == ')' and opened > 1:
                res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)
