class Solution:
    # Increment and compare (Accepted), O(n) time and space
    def buildArray(self, target: List[int], n: int) -> List[str]:
        cur = 1
        res = []
        for val in target:
            while cur != val:
                res += ["Push", "Pop"]
                cur += 1
            res.append("Push")
            cur += 1
        return res

    # Create a Set (Top Voted), O(n) time and space
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        s = set(target)
        for i in range(1, target[-1] + 1):
            res.append("Push")
            if i not in s:
                res.append("Pop")
        return res
