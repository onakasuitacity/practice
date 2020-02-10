A = [3, 8, 12, 25, 6, 23, 7, 1, 15, 4, 9, 17]

def descend(A, i, k = len(A)): # i: target node, k: sub tree A[:k]
    now = i
    while(1):
        if now*2+1 >= k: break # no child
        if now*2+1 == k-1: # only one child
            if A[now] < A[now*2+1]:
                A[now], A[now*2+1] = A[now*2+1], A[now]
            break
        else: # two children
            if max(A[now], A[2*now+1], A[2*now+2]) == A[now]: break
            next = max((A[2*now+1],2*now+1), (A[2*now+2],2*now+2))[1]
            A[now], A[next] = A[next], A[now]
            now = next

def heapsort(A):
    # heapify (O(n))
    for i in range(n//2-1,-1,-1):
        descend(A, i)
    # sort (O(nlogn))
    for k in range(len(A)-1,0,-1):
        A[0], A[k] = A[k], A[0]
        descend(A, 0, k)
    return A
