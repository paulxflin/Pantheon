class Solution:
    # Counters (Accepted), O(n) time and space
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res = 0
        cnt1, cnt2 = Counter(words1), Counter(words2)
        for k in cnt1:
            if cnt1[k] == cnt2[k] == 1:
                res += 1
        return res
