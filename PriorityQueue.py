def parent(i):
    return int(i // 2)


def left(i):
    return i * 2


def right(i):
    return i * 2 + 1


class MaxPriorityQueue:

    def exchange(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __init__(self, a):
        self.array = [0] + a
        self.heapSize = len(a)
        self.buildHeap()

    def buildHeap(self):
        for i in range(self.heapSize, 1, -1):
            self.maxHeapify(i)

    def getMax(self):
        return self.array[1]

    def extractMax(self):
        self.exchange(1, self.heapSize)
        self.maxHeapify(1)
        self.heapSize -= 1
        return self.array[self.heapSize + 1]

    def increaseKey(self, i, key):
        if i < 1 or i > self.heapSize:
            raise IndexError("this beyond the heapSize!")
        elif key < self.array[i]:
            raise KeyError("you should increase the key!")
        else:
            self.array[i] = key
            self.swim(i)

    def swim(self, i):
        while self.array[parent(i)] < self.array[i]:
            self.exchange(i, parent(i))
            i = parent(i)

    def insert(self, key):
        self.array += [key]
        self.heapSize += 1
        self.swim(key)

    def maxHeapify(self, i):
        max = 0
        if left(i) < len(self.array) and self.array[i] < self.array[left(i)]:
            max = left(i)
        else:
            max = i
        if right(i) < len(self.array) and self.array[right(i)] > self.array[max]:
            max = right(i)
        if max != i:
            self.exchange(max, i)
            self.maxHeapify(i)

    def __str__(self):
        return self.array.__str__()


def heapSort(a):
    pq = MaxPriorityQueue(a)
    i = len(a) - 1
    while pq.heapSize != 0:
        a[i] = pq.extractMax()
        i -= 1