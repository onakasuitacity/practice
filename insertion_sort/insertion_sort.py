A = [3, 8, 12, 25, 6, 23, 7, 1, 15, 4, 9, 17]

n = len(A)
for i in range(1,n):
    for j in range(i+1,n):
        while(j>0 and A[j-1]>A[j]):
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1

print(A)
