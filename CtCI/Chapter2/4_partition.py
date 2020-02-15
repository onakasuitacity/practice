from LinkedList import LinkedList

def divide(ll, x):
    now = ll.front()
    front = LinkedList()
    back = LinkedList()
    for node in ll:
        value = node.value
        if value < x:
            front.append(value)
        else:
            back.append(value)
    return front + back

ll = LinkedList()
ll.generate(10)
print(ll)
print(divide(ll, 4))
