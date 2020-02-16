class MinStack(object):
    def __init__(self, values=[]):
        self._stack = []
        for v in values:
            self.append(v)

    def __bool__(self):
        return bool(self._stack)

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return str(self._stack)

    def top(self):
        assert self
        return self._stack[-1][0]

    def min(self):
        assert self
        return self._stack[-1][1]

    def append(self, value):
        if self:
            self._stack.append((value, min(value, self._stack[-1][1])))
        else:
            self._stack.append((value, value))

    def pop(self):
        assert self
        return self._stack.pop()[0]



stack = MinStack([3,4,6,3,5,3,2,4])
print(stack.min())
print(stack.pop())
print(stack.pop())
print(stack.min())
