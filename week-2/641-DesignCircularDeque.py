class MyCircularDeque:

    def __init__(self, k: int):
        self.circular_deque = [None] * k
        self.element_count = 0
        self.begin_index = 0
        self.end_index = 0

    def insertFront(self, value: int) -> bool:
        if self.element_count < len(self.circular_deque):
            self.element_count += 1
            if self.element_count > 1:
                self.begin_index = (self.begin_index -
                                    1) % len(self.circular_deque)

            self.circular_deque[self.begin_index] = value
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.element_count < len(self.circular_deque):
            self.element_count += 1
            if self.element_count > 1:
                self.end_index = (
                    self.end_index + 1) % len(self.circular_deque)
            self.circular_deque[self.end_index] = value

            return True
        return False

    def deleteFront(self) -> bool:
        if self.element_count == 0:
            return False
        self.circular_deque[self.begin_index] = None
        self.element_count -= 1
        if self.element_count >= 1:
            self.begin_index = (self.begin_index +
                                1) % len(self.circular_deque)

        return True

    def deleteLast(self) -> bool:
        if self.element_count == 0:
            return False
        self.circular_deque[self.end_index] = None
        self.element_count -= 1
        if self.element_count >= 1:
            self.end_index = (self.end_index - 1) % len(self.circular_deque)
        return True

    def getFront(self) -> int:
        if self.element_count == 0:
            return -1
        return self.circular_deque[self.begin_index]

    def getRear(self) -> int:
        if self.element_count == 0:
            return -1
        return self.circular_deque[self.end_index]

    def isEmpty(self) -> bool:
        return self.element_count == 0

    def isFull(self) -> bool:
        return self.element_count == len(self.circular_deque)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
