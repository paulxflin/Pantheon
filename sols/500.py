class Solution:
    # # Set and compare all chars (Accepted), O(n) time and space
    # def findWords(self, words: List[str]) -> List[str]:
    #     row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
    #     res = []
    #     for word in words:
    #         lower = word.lower()
    #         if all(ch in row1 for ch in lower) or all(ch in row2 for ch in lower) or all(ch in row3 for ch in lower):
    #             res.append(word)
    #     return res

    # Set of both lines and lowercase word (Top Voted), O(n) time and space
    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = set('qwertyuiop'), set(
            'asdfghjkl'), set('zxcvbnm')
        ret = []
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                ret.append(word)
        return ret
