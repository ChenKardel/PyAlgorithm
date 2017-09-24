class Node:
    def __init__(self, key=None, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        pass

    def delete(self, key):
        pass

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
        self.inorderPrintRecursionPart(node.left)
        print(node.key)
        self.inorderPrintRecursionPart(node.right)

    def preorderPrint(self):
        self.preorderPrintRecursionPart(self.root)

    def preorderPrintRecursionPart(self, node):
        print(node.key)
        self.inorderPrintRecursionPart(node.left)
        self.inorderPrintRecursionPart(node.right)

    def prorderPrint(self):
        self.proderPrintRecursionPart(self.root)

    def proderPrintRecursionPart(self, node):
        self.proderPrintRecursionPart(node.left)
        self.proderPrintRecursionPart(node.right)
        print(node.key)

    def __str__(self):
        global string
        string = ""

        def inorderStr(node):
            inorderStr(node.left)
            string += str(node.key)
            inorderStr(node.right)
        inorderStr(self.root)
        return string

    def __len__(self):
        return self.size
