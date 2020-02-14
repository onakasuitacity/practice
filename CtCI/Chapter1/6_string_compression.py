from itertools import groupby
def run_length_encoding(string):
    res = []
    for key, iter in groupby(string):
        res.append(key)
        res.append(str(sum(1 for _ in iter)))
    res = ''.join(res)
    return res if len(res) < len(string) else string

import unittest
class Test(unittest.TestCase):
    data = [
    ("aabcccccaaa", "a2b1c5a3"),
    ("aabcd", "aabcd"),
    ("", "")
    ]

    def test(self):
        for string, expected in self.data:
            self.assertEqual(run_length_encoding(string), expected)

if __name__ == "__main__":
    unittest.main()
