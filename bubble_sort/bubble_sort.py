A = [3, 8, 12, 25, 6, 23, 7, 1, 15, 4, 9, 17]

n = len(A)
for i in range(n-1):
    for j in range(n-1,i,-1):
        if A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]

print(A)
