from collections import Counter
def is_perm_palindrome(string):
    counter = Counter()
    for c in string:
        counter[c.lower()] += 1
    odd = 0
    for key, val in counter.items():
        if key==' ': continue
        odd += val&1
    return odd<=1

import unittest
class Test(unittest.TestCase):
    dataT = ["Tact Coa"]
    dataF = ["hog ehu ga"]

    def test(self):
        for data in self.dataT:
            self.assertTrue(is_perm_palindrome(data))
        for data in self.dataF:
            self.assertFalse(is_perm_palindrome(data))

    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = is_perm_palindrome(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
