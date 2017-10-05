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


def cutRodMain():
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(cutRod(p, 7))
    print(cutRodFromBottom(p, 7))
    print(cutRodWithRecord(p, 7))

