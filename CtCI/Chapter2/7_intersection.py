from LinkedList import LinkedList

def intersection(ll1, ll2):
    if ll1.back() is not ll2.back():
        return False

    d = len(ll1) - len(ll2)
    node1 = ll1.front()
    node2 = ll2.front()
    if d > 0:
        node1 += d
    else:
        node2 += -d

    while node1 is not node2:
        node1 += 1
        node2 += 1

    return node1
