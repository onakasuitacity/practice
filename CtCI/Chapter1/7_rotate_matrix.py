def rotate_plus_half_of_pi(A):
    return [list(a) for a in zip(*A)][::-1]
def rotate_minus_half_of_pi(A):
    return [list(a) for a in zip(*A[::-1])]
def transpose(A):
    return [list(a) for a in zip(*A)]

def rotate_directly(A):
    n = len(A)
    for ofs in range(n//2):
        k = n-2*ofs
        for i in range(n-2*ofs-1):
            A[0+ofs][i+ofs], A[k-i-1+ofs][0+ofs], A[k-1+ofs][k-i-1+ofs], A[i+ofs][k-1+ofs] = \
            A[i+ofs][k-1+ofs], A[0+ofs][i+ofs], A[k-i-1+ofs][0+ofs], A[k-1+ofs][k-i-1+ofs]
    return A

import unittest
from random import randint
class Test(unittest.TestCase):
    def test(self):
        for n in range(1,100):
            n = 5
            A = [[randint(0,5) for _ in range(n)] for _ in range(n)]
            self.assertEqual(rotate_plus_half_of_pi(A), rotate_directly(A))

if __name__ == "__main__":
    unittest.main()
