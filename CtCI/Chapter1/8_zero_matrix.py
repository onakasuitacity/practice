def annihilator(A):
    m = len(A)
    n = len(A[0])
    zero_row = [0]*m
    zero_col = [0]*n
    for i in range(m):
        zero_row[i] = any(A[i][j]==0 for j in range(n))
    for j in range(n):
        zero_col[j] = any(A[i][j]==0 for i in range(m))

    for i in range(m):
        if zero_row[i]:
            for j in range(n):
                A[i][j]=0

    for j in range(n):
        if zero_col[j]:
            for i in range(m):
                A[i][j]=0

    return A

import unittest
class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = annihilator(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
