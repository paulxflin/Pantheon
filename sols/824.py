class Solution:
    # Apply rules in order (Accepted), O(n) time and space
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        for i in range(len(words)):
            word = words[i]
            if word[0].lower() in 'aeiou':
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a'*(i+1)
            words[i] = word
        return ' '.join(words)

    # Straightforward (Top Voted), O(n) time and space
    def toGoatLatin(self, S):
        vowel = set('aeiouAEIOU')

        def latin(w, i):
            if w[0] not in vowel:
                w = w[1:] + w[0]
            return w + 'ma' + 'a' * (i + 1)
        return ' '.join(latin(w, i) for i, w in enumerate(S.split()))
