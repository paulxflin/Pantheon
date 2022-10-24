class Solution:
    # Get Index for Key + Count Matching Items (Accepted), O(n) time, O(1) space
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ind = res = 0
        if ruleKey == "color":
            ind = 1
        elif ruleKey == "name":
            ind = 2
        for item in items:
            if item[ind] == ruleValue:
                res += 1
        return res

    # Two Liner (Top Voted), O(n) time, O(1) space
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type': 0, 'color': 1, 'name': 2}
        return sum(1 for item in items if item[d[ruleKey]] == ruleValue)
