"""
一个普通的归并排序，使用的是分治思想
这种思想在解决树的问题很常见
因为树的链接的特性（也因为不可随机存取）
一般都是将大问题化小
"""


def mergeSort(a):
    mergeSortPart(a, 0, len(a))


def mergeSortPart(a, n, l):
    if n < l:

        mid = int((n+l)/2)

        mergeSortPart(a, n, mid)
        mergeSortPart(a, mid+1, l)
        merge(a, n, mid, l)


def merge(a, p, q, r):
    def less(m, n):
        if m < n:
            return m
        else:
            return n
    i = p
    L = a[p:q]
    R = a[q:r]
    Lindex = 0
    Rindex = 0

    print("L is: " + str(L))
    print("R is: " + str(R))

    while Lindex != len(L) or Rindex != len(R):
        if Lindex == len(L):
            print("Type3 " + str(R[Rindex]))
            a[i] = R[Rindex]
            i += 1
            Rindex += 1
        elif Rindex == len(R):
            print("Type4 " + str(L[Lindex]))
            a[i] = L[Lindex]
            i += 1
            Lindex += 1
        elif L[Lindex] < R[Rindex]:
            a[i] = L[Lindex]
            i += 1
            Lindex += 1

        else:
            print("Type2 " + str(R[Rindex]))
            a[i] = R[Rindex]
            i += 1
            Rindex += 1


a = [1, 2, 5, 7, 3, 4, 6, 8]
mergeSort(a)
print(a)