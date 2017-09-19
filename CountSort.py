"""
对任意数组都有效的排序方法的效率是sigma(NlgN)
但是对于一些条件下的数组，这个效率可以提升到sigma(N)
在这种满足的条件是已知上界
"""


def CountSort(a, k):
    C = [0]
    B = [0]
    for i in range(k):
        C += [0]

    for i in range(len(a)):
        B += [0]

    for i in a:
        C[i] += 1

    for i in range(k):
        C[i + 1] += C[i]

    for i in a:
        B[C[i]] = i
        C[i] -= 1

    return B


a = [1, 3, 2, 5, 5, 4, 2, 3, 1, 4, 1, 2, 5]
print(CountSort(a, 5))