"""
动态规划，分治思想的子集
都是将大问题分为两个小问题解决
差别在于当分治思想要处理很多重复的小问题时，动态规划可以通过查表的方式减少操作量
对于分治，由于它有的时候要建立决策树，所以可能到a^n(a > 1)的效率，这不是个多项式时间(NP问题标准时间)
通过动态规划，我们可以将效率提升到多项式时间，比如n^a(a > 1)
动态规划大多需要个表记录之前所操作过的小问题的结果/方法
动态规划有两个要求:
1.小问题之间相互独立
    我认为这是所有分治思想都要满足的（其实不然），但是大多分治思想最好要做到小问题互相独立（比如矩阵乘法，矩阵与矩阵之间，小矩阵和小矩阵之间都是互相独立的）
    不然可参照最长路径问题(效率不是多项式)
2.小问题重叠，即重复了小问题的解决
    比如矩阵乘法就没有做到这点，小矩阵相乘之间是没有重叠的
"""


def cutRod(p, n):
    """
    无脑分治的钢筋截取，求价值最大值
    :param p: 价值表
    :param n: 现有钢筋的长度
    :return: 切法
    """
    if n == 0:
        return 0
    q = float("-inf")
    for i in range(1, n + 1):
        q = max(q, p[i] + cutRod(p, n - i))
    return q


def cutRodFromBottom(p, n):
    recorder = [0] * (n + 1)
    for i in range(0, n + 1):
        q = float("-inf")

        for j in range(i + 1):
            q = max(q, p[i - j] + recorder[j])
        recorder[i] = q
    return recorder[n]


def cutRodWithRecord(p: list, n: int):
    recorder = [float("-inf")] * (n + 1)
    return cutRodWithRecordRecursionPart(p, recorder, n)


def cutRodWithRecordRecursionPart(p: list, recorder: list, l: int):
    if recorder[l] >= 0:
        return recorder[l]
    if l == 0:
        q = 0
    else:
        q = float("-inf")
        for i in range(1, l + 1):
            q = max(q, p[i] + cutRodWithRecordRecursionPart(p, recorder, l - i))
    recorder[l] = q
    return q


def cutRodFromBottomGivenSolution(p, n):
    recorder = [0] * (n + 1)
    solutionMatrix = [[0].copy()] * (n + 1)
    print(solutionMatrix)
    for i in range(0, n + 1):
        q = float("-inf")
        solution = []
        maxIndex = 0
        maxSubIndex = 0
        # 挑选最大的赋给q i 是子问题（钢条）的规模（大小）， j是在子问题中如何截取一次（街区一次后将右边换成另一个子问题）
        for j in range(i + 1):
            if q < p[i - j] + recorder[j]:
                q = p[i - j] + recorder[j]
                maxIndex = i - j
                maxSubIndex = j
        print(maxIndex)
        print(maxSubIndex)
        solution = solutionMatrix[maxIndex].copy() + solutionMatrix[maxSubIndex].copy()
        recorder[i] = q
        solutionMatrix[i] = solution
        # print(solutionMatrix)
    return recorder[n], solutionMatrix[n]


def cutRodMain():
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def MatrixMultiOrder(sizes: list):
    """
    sizes是矩阵的规模，比如矩阵有n个，len(sizes) 就是 n + 1（第一个矩阵要算两个规模（长和宽））
    :type sizes: list
    """
    n = len(sizes) - 1
    m = [[0] * n for i in range(n)]

    for length in range(1, len(sizes)):  # for length=1 to sizes.length-1
        endOfStart = len(sizes) - length  # the end of the left pod
        for start in range(1, endOfStart + 1):  # for start(startPoint)=1 to endOfStart
            if float(m[start][start + length - 1]) < float("inf"):  # TODO
                pass
            if start == start + length:
                m[start][start + length - 1] = 0
            m[start][start + length - 1] = float("inf")
            for k in range(start, start + length):  # k is the partition element
                # for k=start to start+length
                q = m[start][k] + m[k][start + length - 1] + sizes[start - 1] * sizes[k] * sizes[start + length - 1]
                if q < m[start][start + length - 1]:
                    m[start][start + length - 1] = q
    return m[1][sizes.__len__()]


def MatrixChainOrder():
    pass


print(MatrixMultiOrder([5, 10, 3, 12, 5, 50]))
