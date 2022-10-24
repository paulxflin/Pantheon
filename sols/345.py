import re


class Solution:
    # Two Pointers (Accepted), O(n) time and space
    def reverseVowels(self, s: str) -> str:
        A = list(s)
        l, r = 0, len(A)-1
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        while l < r:
            if A[l] not in vowels:
                l += 1
            elif A[r] not in vowels:
                r -= 1
            else:
                A[l], A[r] = A[r], A[l]
                l, r = l+1, r-1
        return "".join(A)

    # Two Pointers with Lower (Accepted), O(n) time and space
    def reverseVowels(self, s: str) -> str:
        A = list(s)
        l, r = 0, len(A)-1
        vowels = ('a', 'e', 'i', 'o', 'u')
        while l < r:
            if A[l].lower() not in vowels:
                l += 1
            elif A[r].lower() not in vowels:
                r -= 1
            else:
                A[l], A[r] = A[r], A[l]
                l, r = l+1, r-1
        return "".join(A)

    # Regex findall and sub (Top Voted), O(n) time and space
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
