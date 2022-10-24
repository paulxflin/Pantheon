class Solution:
    # Set + Ord Transform (Solution), O(S) time and space, S is the sum of length of words in words.
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        def transform(word):
            l = []
            for c in word:
                l.append(codes[ord(c) - ord('a')])
            return ''.join(l)

        S = set()
        for word in words:
            S.add(transform(word))
        return len(S)

    # Set + Ord Transform + List Comprehension (Solution), O(S) time and space
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        seen = {"".join(MORSE[ord(c) - ord('a')]
                        for c in word) for word in words}
        return len(seen)
