class Solution:
    # Builds Prefix String and Compare (Accepted), O(n) time, O(n) space
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ''
        for word in words:
            if len(prefix) < len(s):
                prefix += word
                if prefix != s[:len(prefix)]:
                    return False
            else:
                return len(s) == len(prefix) and s == prefix
        return len(s) == len(prefix) and s == prefix

    # Move Along s (Top Voted), O(n) time, O(1) space
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for word in words:
            if s[i:i+len(word)] != word:
                return False
            i += len(word)
            if i == len(s):
                return True
        return False
