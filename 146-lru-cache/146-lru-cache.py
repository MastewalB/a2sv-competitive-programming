class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order = OrderedDict()

    def get(self, key: int) -> int:
        if self.order.get(key) != None:
            temp = self.order[key]
            del self.order[key]
            self.order[key] = temp
            return temp
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.order.get(key) != None:
            del self.order[key]
        elif len(self.order) == self.capacity:
            val = next(iter(self.order))
            del self.order[val]
        self.order[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)