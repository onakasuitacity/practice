class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self, A):
        self._len = 0
        self._root = None
        for a in A:
            self.append(a)

    def __len__(self):
        return self._len

    def __bool__(self):
        return bool(self._len)

    def append(self, x):
        self._len += 1
        # tree が空なら root として保持
        if self._root is None:
            self._root = Node(x)
            return

        now = self._root
        while(1):
            # 根から順に、x が左か右かを考えて移動
            if x < now.val:
                if now.left is None:
                    now.left = Node(x)
                    return
                else:
                    now = now.left
            else:
                if now.right is None:
                    now.right = Node(x)
                    return
                else:
                    now = now.right

    def find(self, x):
        now = self._root
        while(now is not None):
            if x < now.val:
                now = now.left
            elif x > now.val:
                now = now.right
            else:
                return True
        return False
