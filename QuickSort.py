"""
快速排序:
优点：简单，好写，容易理解，速度快，维持效率在O(NlgN)
缺点:不稳定,同是O(NlgN)，不同的分割方法带来的效果完全不同。
快速排序的可拓展性也很好(在于算法比较简单)
有很多的改写比如Dijkstra(?)的三向快速排序
一般前期都有Shuffle，主要是为了防止有序数组排序导致的最坏情况，那时即为O(N^2)
快速排序还有的partition方法是最初的方法，但是那个方法看上去效率不高，于是就没写
"""


def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]


def partition(a, l, r):
    i = l
    x = a[r - 1]

    for j in range(l, r - 1):
        if x > a[j]:
            exchange(a, i, j)
            i += 1

    exchange(a, i, r - 1)
    return i


def QuickSortPart(a, l, r):
    if l < r:
        i = partition(a, l, r)
        QuickSortPart(a, l, i)
        QuickSortPart(a, i + 1, r)


def QuickSort(a):
    QuickSortPart(a, 0, len(a))




# 三向排序，快速排序的一个变式
def ThreeWayPartition(a, lo, hi):

    lt = lo
    i = lo + 1
    x = a[lo]
    gt = hi
    while gt >= i:
        if a[i] < x:
            exchange(a, lt, i)
            lt += 1
            i += 1
        elif a[i] > x:
            exchange(a, i, gt)
            gt -= 1
        else:
            i += 1
    return lt - 1, gt + 1


def ThreeWayQuickSort(a):
    ThreeWayQuickSortPart(a, 0, len(a) - 1)


def ThreeWayQuickSortPart(a, p, q):
    if q >= p:
        (m, n) = ThreeWayPartition(a, p, q)

        ThreeWayQuickSortPart(a, p, m)
        ThreeWayQuickSortPart(a, n, q)
if __name__ == '__main__':

    b = [5, 3, 8, 5, 8, 1, 5, 1, 9, 10, 9, 8, 4, 2, 4, 1, 5]

    c = []
    for i in range(len(b)):
        c += [i]
    print(c)

    ThreeWayQuickSort(b)
    print(b)
    #ThreeWayPartition(b, 0, 7)
    #print(b)

    #ThreeWayQuickSort(b)
