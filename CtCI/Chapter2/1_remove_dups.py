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

ll = LinkedList()
ll.generate(20,0,5)
print(ll)
delete_duplication(ll)
print(ll)
