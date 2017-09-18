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