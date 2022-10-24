class OrderedStream:
    # Use append for each element (Accepted), O(n) time and space insert
    def __init__(self, n: int):
        self.l = [None] * n
        self.index = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey-1] = value
        res = []
        while self.index < len(self.l) and self.l[self.index] != None:
            res.append(self.l[self.index])
            self.index += 1
        return res


class OrderedStream:
    # Update Pointer and Slice (Top Voted), O(n) time and space insert
    def __init__(self, n: int):
        self.data = [None]*n
        self.ptr = 0  # 0-indexed

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1  # 0-indexed
        self.data[id] = value
        if id > self.ptr:
            return []  # not reaching ptr

        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1  # update self.ptr
        return self.data[id:self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
