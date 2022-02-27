class InPlaceHeap:
    heap_size = 0

    def __init__(self, array):
        self.length = len(array)
        self.heap_size = 0

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def swap(array, new, old):
        array[new], array[old] = array[old], array[new]

    @staticmethod
    def is_leaf(array, index):
        if index > len(array) // 2 and index <= len(array):
            return True
        return False

    @staticmethod
    def left_child(array, index):
        if InPlaceHeap.is_leaf(array, index):
            return
        left = (2 * index) + 1
        return left if left < len(array) else None

    @staticmethod
    def right_child(array, index):
        if InPlaceHeap.left_child(array, index):
            return
        right = (2 * index) + 2
        return right if right < len(array) else None

    @staticmethod
    def min_child(array, index):
        if InPlaceHeap.is_leaf(array, index):
            return
        if InPlaceHeap.right_child(array, index):
            return InPlaceHeap.right_child(array, index) if array[InPlaceHeap.right_child(array, index)] < array[InPlaceHeap.left_child(array, index)] else InPlaceHeap.left_child(array, index)
        else:
            return InPlaceHeap.left_child(array, index)

    @staticmethod
    def up_heap(array, index):
        while index > 0 and array[index] < array[InPlaceHeap.parent(index)]:
            InPlaceHeap.swap(array, index, InPlaceHeap.parent(index))
            index = InPlaceHeap.parent(index)

    @staticmethod
    def down_heap(array, index):
        while not InPlaceHeap.is_leaf(array, index):
            min_child = InPlaceHeap.min_child(array, index)
            if min_child and array[min_child] < array[index]:
                InPlaceHeap.swap(array, index, minchild)
                index = min_child
            else:
                break
