from collections import Counter


class Solution:
    # Counter checking all (Accepted + Top Voted), O(n) time, O(1) space
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter, res = Counter(chars), 0
        for word in words:
            word_counter = Counter(word)
            if all(word_counter[ch] <= chars_counter[ch] for ch in word_counter):
                res += len(word)
        return res

    # Counter with For-Else Clause, O(n) time, O(1) space
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum, chars_counter = 0, Counter(chars)
        for word in words:
            word_counter = Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                sum += len(word)
        return sum
