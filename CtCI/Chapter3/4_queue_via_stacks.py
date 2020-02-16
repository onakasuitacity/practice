class MyQueue(object):
    def __init__(self, values=[]):
        self._front = values[::-1]
        self._back = []

    def __bool__(self):
        return bool(self._front) or bool(self._back)

    def __len__(self):
        return len(self._front) + len(self._back)

    def __str__(self):
        return str(self._front[::-1] + self._back)

    def append(self, value):
        self._back.append(value)

    def popleft(self):
        assert self
        if not self._front:
            while self._back:
                self._front.append(self._back.pop())
        return self._front.pop()


queue = MyQueue([1,2,3,4,5])
print(queue)
print(queue.popleft())
print(queue)
queue.append(6)
print(queue)
