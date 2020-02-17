A = [1,2,3,4,5,6,7]

#     4
#    / \
#   2   6
#  / \ / \
# 1  3 5  7
 
def weave(A, B):
    # base case
    if len(A)==0: return [B]
    if len(B)==0: return [A]
    # recursion: len(A)>=1, len(B)>=1
    res = []
    a = A[0]
    for C in weave(A[1:],B):
        res.append([a]+C)
    b = B[0]
    for C in weave(A,B[1:]):
        res.append([b]+C)
    return res

def BSTarray(A):
    # base case
    if len(A)<=1:
        return [A]
    # recursion
    n = len(A)
    root = A[n//2]
    left, right = BSTarray(A[:n//2]), BSTarray(A[n//2+1:])
    res = []
    for L in left:
        for R in right:
            for C in weave(L,R):
                res.append([root]+C)
    return res

for C in BSTarray(A):
    print(C)
