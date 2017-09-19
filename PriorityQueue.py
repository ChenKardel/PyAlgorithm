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

#Use Priority Queue To Establish a Stack


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

#establish a queue can use the similar way but use a MinProrityQueue instead of a MaxProrityQueue