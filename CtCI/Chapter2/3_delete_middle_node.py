from LinkedList import LinkedList

def delete_node(node):
    node.value, node.next = node.next.value, node.next.next


ll = LinkedList()
ll.add_multiple([1,2,3,4])
node = ll.add(5)
ll.add_multiple([6,7,8])

print(ll)
delete_node(node)
print(ll)
