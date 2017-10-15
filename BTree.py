"""
B树，二叉搜索树的一个变式，2-3树的一个扩展
真说的话和红黑树有点相似
"""

t = 2


class BTNode:
    def __init__(self, key, parent=None):
        self.children = [None] * t
        self.key = key
        self.parent = parent


class BTree:
    def __init__(self):
        pass

    def insert(self, key):
        pass

    def remove(self, key):
        pass

    def search(self, key):
        pass
