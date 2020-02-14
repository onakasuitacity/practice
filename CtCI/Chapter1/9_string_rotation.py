def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 *= 2
    return str1.count(str2) > 0

import unittest
class Test(unittest.TestCase):
    dataT = [
    ("waterbottle", "erbottlewat"),
    ("hoge", "hoge"),
    ("hoge", "geho")
    ]
    dataF = [
    ("hoge", "huga"),
    ("onaka", "suitayo")
    ]

    def test(self):
        for data in self.dataT:
            self.assertTrue(is_rotation(*data))
        for data in self.dataF:
            self.assertFalse(is_rotation(*data))

if __name__ == "__main__":
    unittest.main()
