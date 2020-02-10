A = [3, 8, 12, 25, 6, 23, 7, 1, 15, 4, 9, 17]

def merge_sort(A, l=0, r=len(A)):
    # base case
    if r-l==1: return A[l:r]
    # divide
    m = (l+r)//2
    left, right = merge_sort(A, l, m), merge_sort(A, m, r)
    # conquer
    l, r = 0, 0
    res = []
    while(l<len(left) or r<len(right)):
        if (l<len(left) and r<len(right) and left[l]<=right[r]) or r==len(right):
            res.append(left[l])
            l+=1
        else:
            res.append(right[r])
            r+=1
    return res

print(merge_sort(A))
