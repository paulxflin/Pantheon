class MinStack:
    # Update Min every pop (Accepted), O(1) push, pop, top, min
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.stack:
            self.min = min(self.min, val)
            self.stack.append((val, self.min))
        else:
            self.min = val
            self.stack.append((val, self.min))

    def pop(self) -> None:
        val, min_ = self.stack.pop()
        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min


class MinStack:
    # Find min in last elem (Top Voted), O(1) push, pop, top, min
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    def getMin(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
