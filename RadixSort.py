import CountSort
def RadixSort(a):
    #checkoutTheBitOfNumber
    for i in range(len(a)):
        if len(str(a[i - 1])) != len(str(a[i])):
            raise TypeError("can not fit this error")
    length = len(str(a[0]))
    N = 10
    for i in range(length-1, -1, -1):
        #改造版计数排序
        pass



