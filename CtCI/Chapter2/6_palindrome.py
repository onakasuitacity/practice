from LinkedList import LinkedList

def is_palindrome(ll)->bool:
    values = [node.value for node in ll]
    return values == values[::-1]

ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))
