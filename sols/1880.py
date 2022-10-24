class Solution:
    # Use functions to convert all to numerical value (Accepted), O(n) time and space
    def isSumEqual(self, a: str, b: str, t: str) -> bool:
        def letter_val(letter):
            return ord(letter) - ord('a')

        def numerical_val(word):
            s = ''
            for c in word:
                s += str(letter_val(c))
            return int(s)

        return numerical_val(a) + numerical_val(b) == numerical_val(t)

    # Minus 49 (Top Voted), O(n) time and space
    def isSumEqual(self, first: str, second: str, target: str) -> bool:
        def op(s: str): return "".join(chr(ord(ch) - 49) for ch in s)
        return int(op(first)) + int(op(second)) == int(op(target))
