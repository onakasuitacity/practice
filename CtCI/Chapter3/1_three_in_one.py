class Multistack(object):
    def __init__(self, length):
        self._length = length
        self._stack = [None]*(3*length)
        self._first = 0
        self._second = length
        self._third = 2*length

    def __str__(self):
        return str(self._stack)

    def is_full(self, index):
        if index == 0:
            return self._first == self._length
        elif index == 1:
            return self._second == 2 * self._length
        elif index == 2:
            return self._third == 3 * self._length
        else:
            raise ValueError()

    def is_empty(self, index):
        if index == 0:
            return self._first == 0
        elif index == 1:
            return self._second == self._length
        elif index == 2:
            return self._third == 2 * self._length
        else:
            raise ValueError()

    def append(self, index, value):
        assert not self.is_full(index)
        if index == 0:
            self._stack[self._first] = value
            self._first += 1
        elif index == 1:
            self._stack[self._second] = value
            self._second += 1
        elif index == 2:
            self._stack[self._third] = value
            self._third += 1

    def pop(self, index):
        assert not self.is_empty(index)
        if index == 0:
            res = self._stack[self._first]
            self._first -= 1
            self._stack[self._first] = None
        elif index == 1:
            res = self._stack[self._second]
            self._second -= 1
            self._stack[self._second] = None
        elif index == 2:
            res = self._stack[self._third]
            self._third += 1
            self._stack[self._third] = None
        return res


A = Multistack(10)
for i in range(3):
    for j in range(5):
        A.append(i,i*j)
print(A)
print(A.pop(1))
print(A)
