def urlify(string, length):
    res = [None]*length
    for i in range(length):
        if string[i] != ' ':
            res[i] = string[i]
        else:
            res[i] = "%20"
    return ''.join(res)

import unittest
class Test(unittest.TestCase):
    data = [
        ('much ado about nothing      ', 22, 'much%20ado%20about%20nothing'),
        ('Mr John Smith    ', 13, 'Mr%20John%20Smith')
        ]

    def test_urlify(self):
        for test_string, length, expected in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
