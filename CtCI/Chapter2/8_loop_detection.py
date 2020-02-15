from LinkedList import LinkedList

def detect_loop(ll):
    if ll.back().next is None:
        return False

    slow = fast = ll.front()
    while 1:
        slow += 1
        fast += 2
        if slow is fast:
            break

    slow = ll.front()
    while slow is not fast:
        slow += 1
        fast += 1

    return slow
