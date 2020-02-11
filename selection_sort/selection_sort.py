A = [3, 8, 12, 25, 6, 23, 7, 1, 15, 4, 9, 17]

n = len(A)
for i in range(n-1):
    j = min((A[k],k) for k in range(i,n))[1]
    A[i], A[j] = A[j], A[i]

print(A)
