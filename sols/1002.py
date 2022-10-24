from collections import Counter


class Solution:
    # Counters with set of common_chs (Accepted), O(n) time, O(l) space where l = longest_str
    def commonChars(self, words: List[str]) -> List[str]:
        res_counter, common_chs = Counter(), None
        first = True
        for s in words:
            counter = Counter(s)
            if first:
                common_chs = set(counter.keys())
                first = False
            else:
                common_chs &= set(counter.keys())

            if not res_counter:
                res_counter = counter
            else:
                for ch in common_chs:
                    res_counter[ch] = min(res_counter[ch], counter[ch])

        res = []
        for ch in common_chs:
            for _ in range(res_counter[ch]):
                res.append(ch)
        return res

    # Counter Intersection and elements (Top Voted), O(n) time, O(l) space
    def commonChars(self, A: List[str]) -> List[str]:
        res = Counter(A[0])
        for a in A:
            res &= Counter(a)
        return list(res.elements())
