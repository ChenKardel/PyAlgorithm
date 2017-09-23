"""
链表嘛~~~我懒得写了
在这里对比一下链表和数组
链表的好处在于大小任意
数组的好处在于随机存取
大部分情况下链表适用于树和图，因为他们并不需要随机存储
数组会带来的一些麻烦包括浪费大量内存空间(我以前见过计数排序+计数排序递归生成256大小的char数组，看看就可怕）而且resize的成本其实非常高
而一些涉及随机存储的比如堆和一些需要许多随机存储的算法比如二分查找法，和各种排序法都需要数组
这也说明了一个问题，就是链表的排序我认为没有很合适的，我认为比较适用插排和选排，但是都是O(N^2)
"""


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class LinkList:
    def __init__(self):
        self.first = None
        self.length = 0
        self.tail = None

    def append(self, item):
        node = Node(item)
        if self.length == 0:
            self.first = node
            self.tail = node
        else:
            self.first.next = node
            self.first = node
        self.length += 1

    def __radd__(self, other):
        self.append(other)

    def remove(self, item):
        if self.length == 0:
            return None
        else:
            temp = self.tail
            if temp.item == item:
                self.tail = temp.next
                self.length -= 1
            while temp.next is not None:
                if temp.next.item == item:
                    temp.next = temp.next.next
                    self.length -= 1
                    return
                temp = temp.next

    def __str__(self):
        a = self.tail
        result = ""
        while a.next != None:
            result += str(a.item) + "->"
            a = a.next
        result += str(a.item)
        return result

    def __len__(self):
        return self.length

    @staticmethod
    def defaultMatchFunc(key, item):
        return key == item

    def search(self, key, *, matchFunc=defaultMatchFunc):
        a = self.tail
        while a.next is not None:
            if matchFunc(key, a.item):
                return a.item
            a = a.next
        if matchFunc(key, a.item):
            return a.item
        else:
            return None


if __name__ == '__main__':
    l = LinkList()
    l.append(1)
    l.append(3)
    l.append(2)

    print(len(l))
