def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]


def partition(a, l, r):
    i = l
    x = a[r-1]
    print("partition element x is", x)
    for j in range(l, r-1):
        if x > a[j]:
            exchange(a, i, j)
            i += 1

    exchange(a, i, r-1)
    print("left Part", a[l:i])
    print("right Part", a[i+1:r])
    print(a)
    print()
    return i


def QuickSortPart(a, l, r):
    if l < r:

        i = partition(a, l, r)
        QuickSortPart(a, l, i)
        QuickSortPart(a, i+1, r)

def QuickSort(a):
    QuickSortPart(a, 0, len(a))


a = [6, 1, 2, 7, 3, 8, 5, 9, 4]

QuickSort(a)
print(a)