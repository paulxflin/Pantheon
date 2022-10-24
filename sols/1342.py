class Solution(object):
    # Binary Representation (Accepted + Top Voted), O(bits) time and space, O(1) in problem
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_str = "{0:b}".format(num)
        s = len(bin_str) - 1
        for c in bin_str:
            if c == '1':
                s += 1
        return s
