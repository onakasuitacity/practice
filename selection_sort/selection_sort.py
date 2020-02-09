A = [3, 8, 12, 25, 6, 23, 7, 1, 15, 4, 9, 17]

n = len(A)
for i in range(n-1):
    now, idx = A[i], i
    for j in range(i+1,n):
        if now > A[j]:
            now, idx = A[j], j
    A[i], A[idx] = A[idx], A[i]

print(A)
