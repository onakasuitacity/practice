# time O(N), space O(N)

def is_unique(data):
    # ascii と仮定。0<=ord(s)<128
    if len(data)>128:
        return False
    used=[0]*128
    for s in data:
        idx = ord(s)
        if used[idx]:
            return False
        else:
            used[idx] = 1
    return True

import unittest
class Test(unittest.TestCase):
    dataT = ['abcd', 's4fad', '']
    dataF = ['23ds2', 'hb 627jh=j ()']

    def test1(self):
        for string in self.dataT:
            self.assertTrue(is_unique(string))
        for string in self.dataF:
            self.assertFalse(is_unique(string))

unittest.main()
