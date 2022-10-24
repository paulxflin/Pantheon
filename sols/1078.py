class Solution:
    # Check previous two with index (Accepted), O(n) time and space
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        li = text.split()
        res = []
        for i in range(2, len(li)):
            if li[i-2] == first and li[i-1] == second:
                res.append(li[i])
        return res

    # Clean solution (Top voted), O(n) time and space
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans, words = [], text.split()
        for a, b, c in zip(words, words[1:], words[2:]):
            if (a, b) == (first, second):
                ans.append(c)
        return ans
