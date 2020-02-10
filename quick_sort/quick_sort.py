A = [3, 8, 12, 25, 6, 23, 7, 1, 15, 4, 9, 17]

from random import randint
def quick_sort(A, l=0, r=len(A)-1):
    # base case
    if l>=r: return A
    # swap
    i, j = l, r
    piv = A[randint(l,r)]
    while(1):
        while(A[i]<piv): i+=1
        while(A[j]>piv): j-=1
        if i>=j: break
        A[i], A[j] = A[j], A[i]
        i+=1; j-=1
    # divide
    if i-1-l<=r-j-1:
        quick_sort(A, l, i-1)
        quick_sort(A, j+1, r)
    else:
        quick_sort(A, j+1, r)
        quick_sort(A, l, i-1)
    return A

print(quick_sort(A))
