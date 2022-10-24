class Solution:
    # Switch based on op (Accepted + Top Voted), O(n) time and space
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for op in ops:
            if op == "+":
                res.append(res[-1] + res[-2])
            elif op == "C":
                res.pop()
            elif op == "D":
                res.append(res[-1] * 2)
            else:
                res.append(int(op))
        return sum(res)
