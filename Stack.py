import copy
class LimitationStack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.content = []
        for i in range(maxSize):
            self.content += [None]
        self.topPtr = 0

    def push(self, a):
        if self.size == self.maxSize:
            raise Exception("stack overflow")
        else:
            self.content[self.topPtr] = a
            self.topPtr += 1
            self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("stack underflow")
        else:
            x = self.content[self.topPtr]
            self.topPtr -= 1
            self.size -= 1
            return x


    def __len__(self):
        return self.size


    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def __getattr__(self, item):
        return None

    def __str__(self):
        return self.content[0:self.size].__str__()

import Queue

class QueueStack:
    def __init__(self, maxSize):
        self.q1 = Queue.LimitationQueue(maxSize)
        self.q2 = Queue.LimitationQueue(maxSize)

    def push(self, a):
        self.q1.enqueue(a)

    def pop(self):
        q3 = copy.deepcopy(self.q1)
        while not q3.isEmpty():
            self.q2.enqueue(q3.dequeue())

        return self.q2.dequeue()


if __name__ == '__main__':
    s = LimitationStack(10)
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    print(s)
