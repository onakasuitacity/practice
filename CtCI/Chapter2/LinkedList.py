# cf. https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter2/LinkedList.py
class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)

    def __add__(self, value):
        res = self
        for _ in range(value):
            res = res.next
        return res

    def __sub__(self, value):
        res = self
        for _ in range(value):
            res = res.prev
        return res

class LinkedList(object): # doubly
    def __init__(self, values=[]):
        self._front = None
        self._back = None
        for v in values:
            self.append(v)

    def __iter__(self):
        now = self._front
        while now:
            yield now
            now = now.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        return sum(1 for _ in self)

    def __add__(self, ll):
        if ll._front is None:
            pass
        elif self._front is None:
            self._front, self_back = ll._front, ll._back
        else:
            self._back.next, ll._front.prev = ll._front, self._back
            self._back = ll._back
        return self

    def front(self):
        return self._front

    def back(self):
        return self._back

    def append(self, value):
        if self._front is None:
            self._front = self._back = Node(value)
        else:
            node = Node(value)
            self._back.next, node.prev = node, self._back
            self._back = node
        return self._back

    def appendleft(self, value):
        if self._front is None:
            self._front = self._back = Node(value)
        else:
            node = Node(value)
            self._front.prev, node.next = node, self._front
            self._front = node
        return self._front

    def generate(self, n):
        from random import randint
        self._front = self._back = None
        for _ in range(n):
            self.append(randint(0, 9))
