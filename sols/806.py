class Solution:
    # Track width and lines (Accepted), O(n) time, O(1) space
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        cnt, lines = 0, 1
        for ch in s:
            width = widths[ord(ch)-ord('a')]
            if cnt + width > 100:
                lines += 1
                cnt = width
            else:
                cnt = cnt + width
        return [lines, cnt]

    # 6-Liner (Top Voted), O(n) time, O(1) space
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        res, cur = 1, 0
        for i in S:
            width = widths[ord(i) - ord('a')]
            res += 1 if cur + width > 100 else 0
            cur = width if cur + width > 100 else cur + width
        return [res, cur]
