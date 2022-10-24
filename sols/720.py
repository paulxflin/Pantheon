from collections import defaultdict
from functools import reduce


class Node:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Solution(object):

    # # Trie + Sort (Accepted), O(n log n + n * s) time, O(n * s) space
    # class Trie:
    #     def __init__(self):
    #         self.root = Node()
    #         self.max = ""

    #     def has_prefix(self, word):
    #         cur_node = self.root
    #         for c in word[:-1]:
    #             if c in cur_node.children:
    #                 cur_node = cur_node.children[c]
    #             else:
    #                 return False
    #         return cur_node

    #     def insert(self, word):
    #         cur_node = self.has_prefix(word)
    #         if len(word) == 1:
    #             self.root.children[word] = Node()
    #         elif cur_node:
    #             cur_node.children[word[-1]] = Node()
    #         else:
    #             return False
    #         self.max = word if len(self.max) < len(word) else self.max

    # def longestWord(self, words):
    #     """
    #     :type words: List[str]
    #     :rtype: str
    #     """
    #     words.sort()
    #     trie = self.Trie()
    #     for word in words:
    #         trie.insert(word)
    #     return trie.max

    # # Trie + DFS (Solution), O(sum(len(w[i]))) time and space
    # def longestWord(self, words):
    #     def Trie(): return defaultdict(Trie)
    #     trie = Trie()
    #     END = True

    #     for i, word in enumerate(words):
    #         reduce(dict.__getitem__, word, trie)[END] = i

    #     stack = trie.values()
    #     ans = ""
    #     while stack:
    #         cur = stack.pop()
    #         if END in cur:
    #             word = words[cur[END]]
    #             if len(word) > len(ans) or len(word) == len(ans) and word < ans:
    #                 ans = word
    #             stack.extend([cur[letter] for letter in cur if letter != END])

    #     return ans

    # Sets (Top Voted), O(n log n) time, O(sum(len(w[i]))) space
    def longestWord(self, words):
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word
