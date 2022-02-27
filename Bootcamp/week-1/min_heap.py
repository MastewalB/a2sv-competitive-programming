import sys
import math


class MinHeap:
    def __init__(self):
        self.Heap = []
        self.size = 0

    def swap(self, old, new):
        self.Heap[old], self.Heap[new] = self.Heap[new], self.Heap[old]

    def parent(self, position):
        return (position - 1) // 2

    def left_child(self, position):
        if not self.is_leaf(position):
            left = (2 * position) + 1
            return left if left < self.size else None
        return

    def right_child(self, position):
        if self.left_child(position):
            right = (2 * position) + 2
            return right if right < self.size else None
        return

    def is_leaf(self, position):
        if position > (self.size // 2) and position <= self.size:
            return True
        return False

    def insert(self, element):

        self.Heap.append(element)
        current = self.size
        self.size += 1
        self.up_heap(current)

    def update(self, index, update_element):
        self.Heap[index] = update_element

        self.up_heap(index)
        self.down_heap(index)

    def remove(self, index):
        self.size -= 1
        print("Removing ", self.Heap[index],
              " by swapping with ", self.Heap[self.size])
        self.swap(index, self.size)

        self.up_heap(index)
        self.down_heap(index)

        self.Heap.pop()

    def get_min(self):
        if not self.Heap:
            return
        return self.Heap[0]

    def up_heap(self, index):

        while index > 0 and self.Heap[index] < self.Heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def down_heap(self, index):

        while not self.is_leaf(index):
            print("Taking ", self.Heap[index], " down the heap")
            min_child = self.min_child(index)
            if min_child and self.Heap[min_child] < self.Heap[index]:
                self.swap(index, min_child)
                index = min_child
            else:
                break

    def min_child(self, index):
        if self.is_leaf(index):
            return
        if self.right_child(index):
            return self.right_child(index) if self.Heap[self.right_child(index)] < self.Heap[self.left_child(index)] else self.left_child(index)
        else:
            return self.left_child(index)

    def Print(self):

        for i in range((self.size//2)):

            if self.right_child(i):
                print(" PARENT : " + str(self.Heap[i])+" LEFT CHILD : " +
                      str(self.Heap[2 * i + 1])+" RIGHT CHILD : " +
                      str(self.Heap[2 * i + 2]))
            else:
                if self.left_child(i):
                    print(
                        " PARENT : " + str(self.Heap[i])+" LEFT CHILD : " + str(self.Heap[2 * i + 1]))


def heap_sort(array):

    heap = MinHeap()

    for i in array:
        heap.insert(i)
        heap.Print()
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

    for i in range(len(array)):
        array[i] = heap.get_min()
        heap.remove(0)

    return array


# array = [2, 33, 1, 3, 5, 4, 2]
array = [0, 3, 5, 4, 6, 7, 3]
print(heap_sort(array))
