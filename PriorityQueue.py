"""
不说二叉堆，先说优先队列
优先队列是非常棒的存储结构，在Prim算法，Dijkstra最短路径算法和Huffman编码中都有广泛的应用。
优先队列的要求是弹出最大/最小值
因为使用的是Python，这里我的优点队列是没有maxSize的，但是有些算法有
我是希望尽量使用算法导论上的算法，即大小没有限制
其实无所谓了
还有就是这种实现方法是不适用链表实现的，因为涉及到大量的随机存储
但是树形结构是非常适合链表的，所以可能以后会考虑到链表的实现方法
"""


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
        if len(self.array) - 1 > self.heapSize:  # 减去数组头
            self.array[self.heapSize + 1] = key
            self.heapSize += 1
        else:
            self.array += [key]
            self.heapSize += 1
        self.swim(self.heapSize)

    def maxHeapify(self, i):
        # maxItem = 0
        if left(i) < len(self.array) and self.array[i] < self.array[left(i)]:
            maxItem = left(i)
        else:
            maxItem = i
        if right(i) < len(self.array) and self.array[right(i)] > self.array[maxItem]:
            maxItem = right(i)
        if maxItem != i:
            self.exchange(maxItem, i)
            self.maxHeapify(maxItem)

    def __str__(self):
        return self.array.__str__()


class MinPriorityQueue:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = [float("-inf")] + array
        self.size = 0
        self.buildHeap()

    def exchange(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def getSize(self):
        return self.size

    def getMin(self):
        return self.array[1]

    def extractMin(self):
        if self.size == 0:
            raise IndexError("UnderFlow")
        a = self.array[1]
        self.exchange(self.size, 1)
        self.size -= 1
        self.minHeapify(1)
        return a

    def minHeapify(self, i):
        if left(i) > self.size:
            minItem = i
        elif self.array[i] > self.array[left(i)]:
            minItem = left(i)
        else:
            minItem = i
        if right(i) > self.size:
            minItem = minItem
        elif self.array[minItem] > self.array[right(i)]:
            minItem = right(i)
        if minItem != i:

            self.exchange(i, minItem)
            self.minHeapify(minItem)

    def insert(self, key):
        if len(self.array) - 1 > self.size:
            self.array[self.size + 1] = key
            self.size += 1
        else:
            self.array += [key]
            self.size += 1
        self.swim(self.size)

    def swim(self, i):
        if self.array[i] < self.array[parent(i)]:
            self.exchange(i, parent(i))
            self.swim(parent(i))

    def buildHeap(self):
        for i in range(self.size, 0):
            self.minHeapify(i)

    def __str__(self):
        return self.array[1: self.size + 1].__str__()


def heapSort(a):
    pq = MaxPriorityQueue(a)
    i = len(a) - 1
    while pq.heapSize != 0:
        a[i] = pq.extractMax()
        i -= 1


# Use Priority Queue To Establish a Stack


class Stack:
    def __init__(self):
        self.pq = MaxPriorityQueue([])
        self.values = []
        self.size = 0

    def push(self, val):
        self.size += 1
        self.pq.insert(self.size)
        self.values += [val]

    def pop(self):
        self.size -= 1
        return self.values[self.pq.extractMax()]

    def __len__(self):
        return self.size

        # establish a queue can use the similar way but use a MinProrityQueue instead of a MaxProrityQueue


if __name__ == '__main__':
    pass