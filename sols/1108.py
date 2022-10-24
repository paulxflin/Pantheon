class Solution(object):
    # Replace (Accepted + Top Voted), O(1) time, O(1) space (Question specifically for IP address)
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')

    # # Join and Split (Top Voted), O(1) time and space
    # def defangIPaddr(self, address):
    #     return '[.]'.join(address.split('.'))

    # # Regex Substitute (Top Voted), O(1) time and space
    # def defangIPaddr(self, address):
    #     return re.sub('\.', '[.]', address)

    # # No library join and replace (Top Voted), O(1) time and space
    # def defangIPaddr(self, address):
    #     return ''.join('[.]' if c == '.' else c for c in address)
