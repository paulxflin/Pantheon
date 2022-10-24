class Solution(object):
    # Empty list + join (Accepted + Top Voted), O(n) space and time
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ret = [None] * len(s)
        for i in range(len(s)):
            ret[indices[i]] = s[i]
        return "".join(ret)
