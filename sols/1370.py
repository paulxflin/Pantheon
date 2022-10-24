class Solution:
    # Counter with Tuples and no removal of key (Accepted), O(n) time and space
    def sortString(self, s: str) -> str:
        cnt, n = 0, len(s)
        li = list(collections.Counter(sorted(s)).items())
        res = []
        while cnt != n:
            for i in range(len(li)):
                if li[i][1] > 0:
                    res.append(li[i][0])
                    cnt += 1
                    li[i] = (li[i][0], li[i][1]-1)
            for i in range(len(li))[::-1]:
                if li[i][1] > 0:
                    res.append(li[i][0])
                    cnt += 1
                    li[i] = (li[i][0], li[i][1]-1)
        return ''.join(res)

    # Counter removal of key (Top Voted), O(n) time and space
    def sortString(self, s: str) -> str:
        cnt, ans, asc = collections.Counter(s), [], True
        while cnt:
            for c in sorted(cnt) if asc else reversed(sorted(cnt)):
                ans.append(c)
                cnt[c] -= 1
                if cnt[c] == 0:
                    del cnt[c]
            asc = not asc
        return ''.join(ans)
