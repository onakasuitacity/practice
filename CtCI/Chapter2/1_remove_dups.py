from LinkedList import LinkedList

def delete_duplication(ll):
    now = ll.front
    if now is None:
        return
    used = set()
    used.add(now.value)

    while now.next is not None:
        if now.next.value in used:
            now.next = now.next.next
        else:
            used.add(now.next.value)
            now = now.next

def without_buffer(ll):
    if ll.front is None: return
    now = ll.front
    while now:
        iter = now
        while iter.next:
            if iter.next.value == now.value:
                iter.next = iter.next.next
            else:
                iter = iter.next
        now = now.next

ll = LinkedList()
ll.generate(20,0,5)
print(ll)
delete_duplication(ll)
print(ll)
