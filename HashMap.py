"""
散列表（HashMap）
效率高的一匹
日翻红黑树和二叉查找树
就是占空间
效率大概是O(N / self.R)
好吧其实效率在元素量不多的时候才高的一匹
就是
N / M > NlgN
N < 2^M
也就是 N < 2 ^ M时还是散列表快的
我这里的M是19(最好选个质数)
2^19 = 524288
我估计你的Hash表中存不到这么多的数据（笑）
"""
import ArrayList

"""
这是链接
最坏情况下是所有元素哈希值相同
那么就是一条链表
存有N个元素，self.R = M时，最低效率是search->O(N) append->O(1) delete -> O(1)
最快效率是每个槽中放的元素个数都相同，此时查找的效率为search->O(1 + N / M)
"""
import copy


class LinkedHashMap:
    def __init__(self):
        self.R = 19
        # 最好是个质数
        a = ArrayList.LinkList()
        self.tableHeader = []
        for i in range(self.R):
            self.tableHeader.append(copy.deepcopy(a))

    def getHashCode(self, key, use=0):
        # 不同的hashCode方式
        if use == 0:
            if type(key) == int:
                return key % self.R

    def append(self, key, value):
        val = self.getHashCode(key=key)
        self.tableHeader[val].append(item=(key, value))

    def search(self, key):
        val = self.getHashCode(key=key)
        m = self.tableHeader[val].search(key=key, matchFunc=lambda k, t: k == t[0])
        if m is not None:
            return m[1]
        return None

    def remove(self, key):
        a = self.search(key)
        """
        这种做法有点蠢，可以用传Func的方法
        """
        val = self.getHashCode(key=key)
        self.tableHeader[val].remove((val, a))
        return a

    def __len__(self):
        return sum(len(x) for x in self.tableHeader)


"""
Hash值得取法和探查的方法是种艺术
一般图简便用线性探测法，就是一个一个向下查
但是其实这种方法效率非常之低
还可以用二次探查法，就是 hash(next) = c1 * i ^ 2 + c0 * i + hash(now) 虽然有点蠢,其实感觉还是线性探测法换汤不换药
还有高端点的比如说双函数探测
其实就那意思
其实我认为这个只需要用统一的变换方式就够了，其他的不重要
"""


def doubleSearch(Hash, m=2, c1=5, c2=3):
    return c1 * m * m + c2 * m + Hash

class OpenHashMap:
    class DELETED:
        def __init__(self):
            pass

    def __init__(self, R=256, M=19, searchHashFunc=lambda i: (i + 1)):
        self.R = R
        self.hashScale = M
        self.keys = [None] * self.R
        self.values = [None] * self.R
        self.DELELTED = OpenHashMap.DELETED()
        self.searchHashFunc = searchHashFunc

    def getHashCode(self, value, hashFunc=None):
        if hashFunc is None:
            return value % self.hashScale
        else:
            return hashFunc(value)

    def insert(self, key, value):
        hashCode = self.getHashCode(key)
        insertPtr = hashCode
        while self.keys[insertPtr] is not None:
            insertPtr = self.getHashCode(self.searchHashFunc(insertPtr))
        self.keys[insertPtr] = key
        self.values[insertPtr] = value

    def search(self, key):
        hashCode = self.getHashCode(key)
        insertPtr = hashCode
        while self.keys[insertPtr] != key and self.keys[insertPtr] is not None:
            insertPtr = self.getHashCode(self.searchHashFunc(insertPtr))
        if self.values[insertPtr] == self.DELETED:
            return None
        else:
            return self.values[insertPtr]

    def remove(self, key):
        hashCode = self.getHashCode(key)
        insertPtr = hashCode
        while self.keys[insertPtr] != key and self.keys[insertPtr] is not None:
            insertPtr = self.getHashCode(self.searchHashFunc(insertPtr))
        self.values[insertPtr] = self.DELETED

"""
不敢写全域散列表（瑟瑟发抖）
"""
if __name__ == '__main__':
    a = []
    for i in range(100):
        a.append((i, 100 - i))
    linkList = OpenHashMap()
    for i in a:
        linkList.insert(i[0], i[1])
    print(linkList.search(5))
