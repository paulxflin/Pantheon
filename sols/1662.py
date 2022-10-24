class Solution:
    # Join the arrays (Accepted), O(n+m) time and space
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

    # Compare every char manually (Accepted), O(min(n, m)) time, O(1) space
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_ind1 = char_ind1 = word_ind2 = char_ind2 = 0
        l1, l2 = len(word1), len(word2)
        wl1, wl2 = len(word1[word_ind1]), len(word2[word_ind2])

        while word_ind1 < l1 and word_ind2 < l2:
            if word1[word_ind1][char_ind1] != word2[word_ind2][char_ind2]:
                return False
            else:
                if wl1 == None:
                    wl1 = len(word1[word_ind1])
                if wl2 == None:
                    wl2 = len(word2[word_ind2])

            char_ind1 += 1
            if char_ind1 == wl1:
                word_ind1 += 1
                char_ind1 = 0
                wl1 = None

            char_ind2 += 1
            if char_ind2 == wl2:
                word_ind2 += 1
                char_ind2 = 0
                wl2 = None

        return word_ind1 == l1 and word_ind2 == l2

    # Generator compare every char (Top Voted), O(min(n, m)) time, O(1) space
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.gen(word1), self.gen(word2)):
            if c1 != c2:
                return False
        return True

    def gen(self, word: List[str]):
        for s in word:
            for c in s:
                yield c
        # Ensure False when len(word1) != len(word2)
        yield None
