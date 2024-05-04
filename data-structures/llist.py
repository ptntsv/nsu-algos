class Pair:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"{self.key}: {self.value}"


class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self) -> str:
        return str(self.value)


class DoublyLinkedList:
    def add_head(self, node):
        if not self.head:
            assert not self.tail
            self.head = node
            self.tail = node
        else:
            self.head.prev_node = node
            node.next_node = self.head
            self.head = node
        self.n += 1

    def add_tail(self, node):
        if not self.head:
            assert not self.tail
            self.head = node
            self.tail = node
        else:
            assert self.tail
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node
        self.n += 1

    def remove(self, node):
        if node != self.head and node != self.tail:
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
        else:
            if node == self.head:
                if node.next_node:
                    node.next_node.prev_node = None
                self.head = node.next_node
            if node == self.tail:
                if node.prev_node:
                    node.prev_node.next_node = None
                self.tail = node.prev_node
        self.n -= 1

    def __init__(self, nodes=None):
        self.head = self.tail = None
        self.n = 0
        if nodes:
            for n in nodes:
                self.add_tail(n)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_node

    def __str__(self):
        string = ""
        for el in self:
            string += str(el)
            if el.next_node:
                string += " -> "
        return string
