import re


class Solution:
    # Translate with dict (Accepted), O(n) time and space
    def reformatNumber(self, number: str) -> str:
        stripped = number.translate({ord(' '): None, ord('-'): None})
        res, i = [], 0
        while i < len(stripped) - 4:
            res.append(stripped[i:i+3])
            i += 3
        if i == len(stripped) - 4:
            res.append(stripped[i:i+2])
            res.append(stripped[i+2:])
        else:
            res.append(stripped[i:])
        return '-'.join(res)

    # Translate with maketrans table (Accepted), O(n) time and space

    def reformatNumber(self, number: str) -> str:
        table = number.maketrans('', '', '- ')
        stripped = number.translate(table)
        res, i = [], 0
        while i < len(stripped) - 4:
            res.append(stripped[i:i+3])
            i += 3
        if i == len(stripped) - 4:
            res.append(stripped[i:i+2])
            res.append(stripped[i+2:])
        else:
            res.append(stripped[i:])
        return '-'.join(res)

    # Regex substitution with lookahead and backreferences (Top Voted), O(n) time and space
    def reformatNumber(self, number: str) -> str:
        return re.sub('(...?(?=..))', r'\1-', re.sub('\D', '', number))
