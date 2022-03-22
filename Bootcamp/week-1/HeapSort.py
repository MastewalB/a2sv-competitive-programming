# User function Template for python3

class Solution:
    def swap(self, index1, index2, arr):
        arr[index1], arr[index2] = arr[index2], arr[index1]

    def leftChild(self, index, n):
        left = (2 * index) + 1
        return left

    def rightChild(self, index, n):
        right = (2 * index) + 2
        return right

    def parent(self, index):
        if index == 0:
            return 0
        return (index - 1) // 2

    def upHeap(self, arr, n, index):
        parent = self.parent(index)
        while index > 0 and arr[index] < arr[parent]:
            self.swap(index, parent, arr)
            index = parent
            parent = self.parent(index)

    def downHeap(self, arr, n, index):
        while self.leftChild(index, n) < n:
            minChild = self.leftChild(index, n)
            right = self.rightChild(index, n)
            if right < n and arr[right] < arr[minChild]:
                minChild = self.rightChild(index, n)
            if arr[minChild] < arr[index]:
                self.swap(index, minChild, arr)
                index = minChild
            else:
                break

    def getMin(self, arr):
        if not arr:
            return
        return arr[0]

    def Print(self, arr, n):
        for i in range((n // 2)):
            if self.rightChild(i, n):
                print(" PARENT : " + str(arr[i])+" LEFT CHILD : " +
                      str(arr[2 * i + 1])+" RIGHT CHILD : " +
                      str(arr[2 * i + 2]))
            else:
                if self.leftChild(i, n):
                    print(
                        " PARENT : " + str(arr[i])+" LEFT CHILD : " + str(arr[2 * i + 1]))

    def reverse(self, arr, n):
        start, end = 0, n-1
        while start < end:
            self.swap(start, end, arr)
            start += 1
            end -= 1

    def heapify(self, arr, n, i):
        self.upHeap(arr, n, i)
        self.downHeap(arr, n, i)

    def buildHeap(self, arr, n):
        for i in range(n):
            self.upHeap(arr, n, i)

    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        temp = n
        # for i in range(n, 0, -1):
        #     self.swap(0, i-1, arr)
        #     self.heapify(arr, i-1, 0)
        while temp > 0:
            self.swap(0, temp-1, arr)
            self.downHeap(arr, temp-1, 0)
            temp -= 1
        # self.Print(arr, n)
        self.reverse(arr, n)
        return arr
