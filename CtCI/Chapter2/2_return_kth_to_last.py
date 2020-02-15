from LinkedList import LinkedList

# recursion
def kth_node1(node, k):
    if node is None:
        return 0

    res = kth_node1(node.next, k)
    if isinstance(res, int):
        if res < k-1:
            return res + 1
        else:
            return node
    else:
        return res

# iterate
def kth_node2(ll, k):
    kth_next = ll.front()
    for _ in range(k):
        if kth_next is None:
            return None
        kth_next = kth_next.next

    now = ll.front()
    while kth_next:
        now, kth_next = now.next, kth_next.next
    return now

ll = LinkedList()
ll.generate(10)
print(ll)
print(kth_node1(ll.front(), 3))
print(kth_node2(ll, 3))
