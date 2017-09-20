class LimitationQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.content = []
        for i in range(maxSize):
            self.content += [None]
        self.tail = 0
        self.front = 0
        self.size = 0

    def enqueue(self, s):
        if self.size == self.maxSize:
            raise Exception("Queue Overflow")
        self.content[self.front] = s
        if self.front == self.maxSize - 1:
            self.front = 0
        else:
            self.front += 1
        self.size += 1


    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue underflow")
        x = self.content[self.tail]
        if self.tail == self.maxSize - 1:
            self.tail = 0
        else:
            self.tail += 1
        self.size -= 1
        return x

    def __len__(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def __getattr__(self, item):
        return None

    def __iter__(self):
        if self.tail <= self.front:
            if self.front != self.maxSize - 1:
                return self.content[self.tail:self.front + 1]
            else:
                return self.content[self.tail:self.front] + self.content[0]
        else:
            return self.content[self.tail:self.maxSize] + self[0:self.front+1]

    def __str__(self):
        return self.__iter__()


if __name__ == '__main__':
    q = LimitationQueue(10)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.dequeue()
    print(q.__str__())
