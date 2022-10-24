class MagicDictionary:
    # List + Diff (Accepted), O(n * s) time and space
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words.append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(searchWord) == len(word):
                diff = 0
                for i in range(len(word)):
                    if searchWord[i] != word[i]:
                        diff += 1
                if diff == 1:
                    return True
        return False

    # # Python 2 Candidates (Top Voted), O(n * s) time and space
    # def _candidates(self, word):
    #     for i in xrange(len(word)):
    #         yield word[:i] + '*' + word[i+1:]

    # def buildDict(self, words):
    #     self.words = set(words)
    #     self.near = collections.Counter(cand for word in words
    #                                     for cand in self._candidates(word))

    # def search(self, word):
    #     return any(self.near[cand] > 1 or
    #                self.near[cand] == 1 and word not in self.words
    #                for cand in self._candidates(word))

    # # Intuitive + Dictionary (Top Voted), O(n * s) time and space
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.wordsdic={}

    # def buildDict(self, dict):
    #     """
    #     Build a dictionary through a list of words
    #     :type dict: List[str]
    #     :rtype: void
    #     """
    #     for i in dict:
    #         self.wordsdic[len(i)]=self.wordsdic.get(len(i),[])+[i]

    # def search(self, word):
    #     """
    #     Returns if there is any word in the trie that equals to the given word after modifying exactly one character
    #     :type word: str
    #     :rtype: bool
    #     """
    #     for candi in self.wordsdic.get(len(word),[]):
    #             countdiff=0
    #             for j in range(len(word)):
    #                 if candi[j]!=word[j]:
    #                     countdiff+=1
    #             if countdiff==1:
    #                 return True
    #     return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
