from collections import Counter

def check_permutation(str1, str2):
    if len(str1)!=len(str2): return False
    counter = Counter()
    for s in str1:
        counter[s] += 1
    for s in str2:
        if counter[s]==0:
            return False
        else:
            counter[s]-=1
    return True

import unittest
class Test(unittest.TestCase):
    def test(self):
        dataT = (
            ('abcd', 'bacd'),
            ('3563476', '7334566'),
            ('wef34f', 'wffe34'),
        )
        dataF = (
            ('abcd', 'd2cba'),
            ('2354', '1234'),
            ('dcw4f', 'dcw5f'),
        )
        for data in dataT:
            self.assertTrue(check_permutation(*data))
        for data in dataF:
            self.assertFalse(check_permutation(*data))

if __name__=="__main__":
    unittest.main()
