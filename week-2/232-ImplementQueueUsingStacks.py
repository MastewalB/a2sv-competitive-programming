class MyQueue:

    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, x):
        if len(self.stack_a) != 0:
            for i in range(len(self.stack_a)):
                self.stack_b.append(self.stack_a.pop())
            self.stack_a.append(x)
            for i in range(len(self.stack_b)):
                self.stack_a.append(self.stack_b.pop())

    def pop(self):
        if self.empty():
            return False
        return self.stack_a.pop()

    def peek(self):
        if self.empty():
            return False
        return self.stack_a[-1]

    def empty(self):
        if len(self.stack_a) == 0:
            return True
        return False
