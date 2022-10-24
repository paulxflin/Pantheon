class Solution:
    # Take difference between inbound and outbound sets (Accepted), O(n) time and space
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing, inbound = set(), set()
        for src, dst in paths:
            outgoing.add(src)
            inbound.add(dst)
        return list(inbound-outgoing)[0]

    # Use zip to unravel paths into A and B + map to set + pop item (Top Voted), O(n) time and space
    def destCity(self, paths: List[List[str]]) -> str:
        A, B = map(set, zip(*paths))
        return (B - A).pop()
