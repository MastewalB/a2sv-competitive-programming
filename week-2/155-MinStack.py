class MinStack:

    def __init__(self):
        self.stack = []
        self.order = []

    def push(self, val):
        self.stack.append(val)
        if len(self.order) != 0:
            if val <= self.order[-1]:
                self.order.append(val)
            else:
                self.order.append(self.order[-1])
        else:
            self.order.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.order.pop()

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def getMin(self):
        if len(self.order) >= 0:
            return self.order[-1]
        return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
val = 12
obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
