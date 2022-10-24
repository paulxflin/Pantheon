from collections import Counter


class Solution:
    # Counter Keys (Accepted), O(n) time and space
    def checkIfPangram(self, sentence: str) -> bool:
        return len(Counter(sentence).keys()) == 26

    # Set (Top Voted), O(n) time and space
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
