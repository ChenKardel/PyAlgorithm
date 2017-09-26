class Node:
    def __init__(self, key=None, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# TODO:DEBUG THE FUNCTION 'insert' AND THE FUNCTION 'delete'

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, value):
        node = self.root
        if node is None:
            self.root = Node(key=key, value=value, left=None, right=None, parent=None)
        while node is not None:
            if key < node.key:
                if node.left is not None:
                    node.left = Node(key=key, value=value, left=None, right=None, parent=node)
                else:
                    node = node.left
            elif key > node.key:
                if node.right is not None:
                    node.right = Node(key=key, value=value, left=None, right=None, parent=node)
                node = node.right
            else:
                node.value = value
                # 多种解决方法

    def delete(self, key):
        node = self.searchNode(key, self.root)
        if node.left is None:
            self.transform(node, node.right)
        elif node.right is None:
            self.transform(node, node.left)
        else:
            y = self.minimumRecursionPart(node.right)
            if y.parent == node:
                self.transform(y, y.right)
                y.right = node.right
                y.right.parent = y
            y.left = node.left
            y.left.parent = y

    def transform(self, v, u):
        if v.parent is None:
            self.root = u
        elif v == v.parent.left:
            v.parent.left = u
        elif v == v.parent.right:
            v.parent.right = u
        if v is not None:
            v.parent = u.parent

    def searchNode(self, key, node):
        if node.key == key:
            return node
        elif node.key > key:
            if node.left is not None:
                return self.searchNode(key, node.left)
            else:
                return None
        else:
            if node.right is not None:
                return self.searchNode(key, node.right)
            else:
                return None

    def search(self, key):
        a = self.searchNode(key, self.root)
        return a.value

    def successor(self, key):
        node = self.searchNode(key, self.root)
        if node.right is not None:
            return self.maximumRecursionPart(node.right)
        y = node.parent
        while y is not None and y.right == node:
            y = y.parent
            node = y.right
        return y

    def predecessor(self, key):
        node = self.searchNode(key, self.root)
        if node.left is not None:
            return self.minimumRecursionPart(node.left)
        y = node.parent
        while y is not None and y.left == node:
            y = y.parent
            node = y.left
        return y

    def maximum(self):
        return self.maximumRecursionPart(self.root)

    def maximumRecursionPart(self, node):
        if node.right is not None:
            return self.maximumRecursionPart(node=node.right)
        else:
            return node.key

    def minimum(self):
        self.minimumRecursionPart(self.root)

    def minimumRecursionPart(self, node):
        if node.left is not None:
            return self.minimumRecursionPart(node.left)
        else:
            return node.key

    def inorderPrint(self):
        self.inorderPrintRecursionPart(self.root)

    def inorderPrintRecursionPart(self, node):
        if node is None:
            return
        self.inorderPrintRecursionPart(node.left)
        print(node.key, end=" ")
        self.inorderPrintRecursionPart(node.right)

    def preorderPrint(self):
        self.preorderPrintRecursionPart(self.root)

    def preorderPrintRecursionPart(self, node):
        if node is None:
            return
        print(node.key, end=" ")
        self.inorderPrintRecursionPart(node.left)
        self.inorderPrintRecursionPart(node.right)

    def prorderPrint(self):
        self.proderPrintRecursionPart(self.root)

    def proderPrintRecursionPart(self, node):
        if node is None:
            return
        self.proderPrintRecursionPart(node.left)
        self.proderPrintRecursionPart(node.right)
        print(node.key, end=" ")

    def __str__(self):

        string = ""

        def inorderStr(node):
            if node is None:
                return
            inorderStr(node.left)

            inorderStr(node.right)

        inorderStr(self.root)
        return string

    def __len__(self):
        return self.size


if __name__ == '__main__':
    b = BinarySearchTree()
    b.insert(5, "l")
    b.insert(4, "e")
    b.insert(7, "o")
    b.insert(3, "h")
    b.insert(6, "l")
    b.inorderPrint()
