import collections


class Solution:
    # Default Dict (Accepted), O(n) time and space
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)
        for item in cpdomains:
            count, dom = item.split()
            counts[dom] += int(count)
            subdoms = dom.split('.')
            for i in range(1, len(subdoms)):
                counts[".".join(subdoms[i:])] += int(count)

        return [f"{str(count)} {subdom}" for subdom, count in counts.items()]

    # Counter (Top Voted), O(n) time and space
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = collections.Counter()
        for cd in cpdomains:
            n, s = cd.split()
            count[s] += int(n)
            for i in range(len(s)):
                if s[i] == '.':
                    count[s[i + 1:]] += int(n)
        return ["%d %s" % (count[k], k) for k in count]
