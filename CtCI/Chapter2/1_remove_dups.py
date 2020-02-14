from LinkedList import LinkedList

def delete_duplication(ll):
    prev = ll.front
    if prev is None:
        return
    now = prev.next
    if now is None:
        return

    S = set()
    S.add(prev.value)
    while now is not None:
        if now.value in S:
            now, prev.next = now.next, now.next
        else:
            S.add(now.value)
            prev, now = now, now.next


ll = LinkedList()
ll.generate(20,0,5)
print(ll)
delete_duplication(ll)
print(ll)
