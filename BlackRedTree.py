"""
对方不想理你
并向你扔了一棵红黑树
要求你写出它的实现
"""
from BinarySearchTree import BinarySearchTree

BLACK = True
RED = False
"""
红黑树维持五个性质：
1.每个节点或是红色的，或是黑色的；
2.根节点是黑色的
3，每个叶节点是黑色的（对于NIL，视其为黑色）
4.如果一个节点是红色的，则它的两个子节点是黑色的
5.对于每个节点，从该节点到其所有后代叶节点的简单路径上，均包含相同数目的黑色节点

对于3性质，我们将所有的NIL以常量 self.NIL = Node(None, None, None, None, None, Black)代替而不是简单的NIL，为了简化算法
红黑树可以看做是2-3树的一种具体实现
"""


class BlackRedTree:
    def __init__(self):

        self.NIL = BlackRedTree.Node(None, None, None, None, None, BLACK)
        self.size = 0
        self.root = self.NIL

    class Node:
        def __init__(self, key, value, parent, left, right, color=BLACK):
            self.key = key
            self.value = value
            self.parent = parent
            self.left = left
            self.right = right
            self.color = color

    def insert(self, key, value):
        # 插入某个点，插入之后进行颜色补正
        z = BlackRedTree.Node(key, value, self.NIL, self.NIL, self.NIL, BLACK)
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            elif z.key > x.key:
                x = x.right
            else:
                x.value = value
                return
        z.parent = y
        if y == self.NIL:
            self.root = z
            return
        elif z.key > y.key:
            y.right = z
        elif z.key < y.key:
            y.left = z
        else:
            y.value = z.value
        z.color = RED
        # 当完成插入的时候，需要进行颜色的补正
        # 可能违背的性质：性质2或4，并且在补正的情况下也可能不断地违背。
        self.insertFixUp(z)

    def insertFixUp(self, node):
        """
        插入时颜色补正
        :type node: BlackRedTree.Node
        """
        while node.color == RED:
            y = node.parent.parent
            if node.parent == y.left:
                if y.right.color == RED:
                    # case1
                    y.right.color = BLACK
                    y.left.color = BLACK
                    y.color = RED
                    node = y
                elif node.parent.right == node:
                    # case2
                    # case2是个转变的过程，将这种情形转化到case3并且用case3处理
                    node = node.parent
                    self.rotateLeft(node)
                # case 3
                y = node.parent.parent
                self.rotateRight(y)
                y.color = RED
                node.parent.color = BLACK
            else:  # 与上面是镜像关系
                if y.left.color == RED:
                    y.left.color = BLACK
                    y.right.color = BLACK
                    y.color = RED
                    node = y
                elif node.parent.left == node:
                    node = node.parent
                    self.rotateRight(node)
                y = node.parent.parent
                self.rotateLeft(y)
                y.color = RED
                node.parent.color = BLACK
        self.root.color = BLACK

    def rotateRight(self, node):
        """
        向右旋转
        :type node: BlackRedTree.Node
        """
        y = node.left
        if y.right != self.NIL:
            node.left = y.right
        if node.parent == self.NIL:
            self.root = y
        elif node.parent.left == node:
            node.parent.left = y
        else:
            node.parent.right = y
        node.parent = y
        y.right = node

    def rotateLeft(self, node):
        """
        向左旋转
        :type node: BlackRedTree.Node
        """
        y = node.right
        if y.left != self.NIL:
            node.right = y.left
        if node.parent == self.NIL:
            self.root = y
        elif node.parent.left == node:
            node.parent.left = y
        else:
            node.parent.right = y
        node.parent = y
        y.left = node

    def remove(self, key):
        pass
