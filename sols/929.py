class Solution:
    # Set + Find (Accepted), O(n) time and space
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split('@')
            ind = local.find('+')
            if ind >= 0:
                local = local[:ind]
            res.add((local.replace('.', ''), domain))
        return len(res)

    # Set + Split (Top Voted), O(n) time and space
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)
