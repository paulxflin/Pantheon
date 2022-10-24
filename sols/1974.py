class Solution:
    # Greedy Special First Case (Accepted), O(n) time, O(1) space
    def minTimeToType(self, word: str) -> int:
        def diff(a, b):
            diff = (ord(a)-ord(b)) % 26
            return min(diff, 26-diff)
        res = len(word) + diff(word[0], 'a')
        for i in range(len(word)-1):
            res += diff(word[i], word[i+1])
        return res

    # Greedy (Top Voted), O(n) time, O(1) space
    def minTimeToType(self, word: str) -> int:
        ans = len(word)
        prev = "a"
        for ch in word:
            val = (ord(ch) - ord(prev)) % 26
            ans += min(val, 26 - val)
            prev = ch
        return ans
