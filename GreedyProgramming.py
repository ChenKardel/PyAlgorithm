class HuffManNode:
    def __init__(self, character: str, freq: float, left=None, right=None, parent=None):
        self.left = left
        self.freq = freq
        self.character = character
        self.right = right
        self.parent = parent

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq


def protravel(node: HuffManNode):
    if node is None:
        return
    protravel(node.left)
    protravel(node.right)


leaves = []


def getLeavesCollection(node: HuffManNode):
    if node is None:
        return
    getLeavesCollection(node.left)
    getLeavesCollection(node.right)
    if node.left is None or node.right is None:
        leaves.append(node)


def HuffmanTreeBuilding(table: dict) -> HuffManNode:
    from PriorityQueue import MinPriorityQueue
    huffman = MinPriorityQueue()
    for item in table.items():
        huffman.insert(HuffManNode(*item))
    # Initialize
    for i in range(len(table) - 1):
        a = huffman.extractMin()
        b = huffman.extractMin()
        newNode = HuffManNode('mid', a.freq + b.freq, a, b)
        a.parent = newNode
        b.parent = newNode
        huffman.insert(newNode)
    return huffman.extractMin()  # give an entry of huffmanCodingTree


def HuffmanCoding(string: str) -> (str, dict):
    table = dict()
    for char in string:
        if char not in table.keys():
            table[char] = 1
        else:
            table[char] += 1
    rootEntry = HuffmanTreeBuilding(table)
    getLeavesCollection(rootEntry)
    stringCollection = dict()
    for leaf in leaves:
        c = leaf.character
        coding = ''
        while leaf.parent != rootEntry:
            if leaf.parent.left == leaf:
                coding = '0' + coding
            else:
                coding = '1' + coding
            leaf = leaf.parent
        if leaf.parent.left == leaf:
            coding = '0' + coding
        else:
            coding = '1' + coding
        stringCollection[c] = coding
    for i in stringCollection:
        string = string.replace(i.key, i.value)
    return string, stringCollection

