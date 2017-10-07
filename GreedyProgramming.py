class HuffManNode:
    def __init__(self, freq: float, character: str, left=None, right=None):
        self.left = left
        self.freq = freq
        self.character = character
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq


def HuffmanCoding(table: dict) -> HuffManNode:
    from PriorityQueue import MinPriorityQueue
    huffman = MinPriorityQueue()
    for item in table.items():
        huffman.insert(HuffManNode(*item))
    # Initialisze
    for i in range(len(table) - 1):
        a = huffman.extractMin()
        b = huffman.extractMin()
        newNode = HuffManNode(a.freq + b.freq, "mid", a, b)
        huffman.insert(newNode)
    return huffman.extractMin()  # give an entry of huffmanCodingTree

