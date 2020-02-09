class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self, A):
        self._len = 0
        self._root = None
        for a in A: self.add(a)

    def __len__(self):
        return self._len

    def __bool__(self):
        return bool(self._len)

    def add(self, x):
        self._len += 1
        # tree が空なら root として保持
        if self._root is None:
            self._root = Node(x)
            return
        # そうでなければ根から順に、x が左か右かを考えて移動
        now = self._root
        while(1):
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
            if x < now.val: now = now.left
            elif x > now.val: now = now.right
            else: return True
        return False

    def remove(self, x):
        # 効率はよくないが、先に存在するかどうかを判定する
        if not self.find(x):
            raise ValueError("Value not found.")
        # 該当 node と parent の情報が必要
        self._len -= 1
        node, par = self._root, -1
        while(node.val != x):
            node, par = node.left if x < node.val else node.right, node
        self._replace(node, par, par.right is node if par!=-1 else -1)
        del node

    def _replace(self, node, par, direction): # direction: left=0, right=1, node==root:-1
        # recusion is called at most 2 times
        # base case (No children)
        if node.left is None and node.right is None:
            if direction==0: par.left = None
            elif direction==1: par.right = None
            else: tree._root = None

        # base case (only 1 child)
        elif (node.left is None) ^ (node.right is None):
            child = node.left if node.right is None else node.right
            if direction==0: par.left = child
            elif direction==1: par.right = child
            else: self._root = child

        # node を node 以下の最大の値と入れ替える
        else:
            next, npar = node.left, node
            while(next.right is not None):
                next, npar = next.right, next
            self._replace(next, npar, npar.right is next)
            if direction==0: par.left = next
            elif direction==1: par.right = next
            else: self._root = next
            next.left, next.right = node.left, node.right

    def show(self):
        res = []
        self._traverse(self._root, res)
        return res

    def _traverse(self, node, arr):
        # base case
        if node is None: return
        # inorder DFS
        self._traverse(node.left, arr)
        arr.append(node.val)
        self._traverse(node.right, arr)


A = [3, 8, 12, 25, 6, 23, 7, 1, 15, 4, 9, 17]
tree = BinarySearchTree(A)
print(tree.show())
tree.add(23) # duplication is okay (but tend to be unbalanced)
print(tree.show())
tree.remove(8)
print(tree.show())
