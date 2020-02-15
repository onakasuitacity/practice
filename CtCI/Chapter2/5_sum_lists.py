from LinkedList import LinkedList

def add(ll1, ll2):
    res = LinkedList()
    now1 = ll1.front()
    now2 = ll2.front()
    carry = 0
    while now1 or now2:
        if now1 and now2:
            carry, digit = divmod(now1.value + now2.value + carry, 10)
            now1 += 1; now2 += 1
        elif now1:
            carry, digit = divmod(now1.value + carry, 10)
            now1 += 1
        else:
            carry, digit = divmod(now2.value + carry, 10)
            now2 += 1
        res.append(digit)
    if carry:
        res.append(1)
    return res

def add_from_right(ll1, ll2):
    d = len(ll1) - len(ll2)
    # 0-padding
    if d > 0:
        for _ in range(d):
            ll2.appendleft(0)
    else:
        for _ in range(-d):
            ll1.appendleft(0)

    res = LinkedList()
    def add_recursively(node1, node2): # return carry
        # base case
        if node1 is None: # also node2 is None
            return 0
        # recursive
        carry, digit = divmod(node1.value + node2.value + add_recursively(node1.next, node2.next), 10)
        res.appendleft(digit)
        return carry

    if add_recursively(ll1.front(), ll2.front()):
        res.appendleft(1)

    return res

ll1 = LinkedList([8,3,6,4,9])
ll2 = LinkedList([4,2,9,6,3])
print(ll1)
print(ll2)
print(add(ll1,ll2))
print(add_from_right(ll1, ll2))
