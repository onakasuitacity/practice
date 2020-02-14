def is_convertible(str1, str2)->bool:
    if len(str1) < len(str2):
        str1, str2 = str2, str1 # len(str1) >= len(str2)

    if len(str1) - len(str2) >= 2:
        return False

    if len(str1) - len(str2) == 1:
        i = 0
        diff = 0
        for i in range(len(str2)):
            if str1[i+diff] != str2[i]:
                diff += 1
                if diff>=2 or str1[i+diff] != str2[i]:
                    return False
        return True

    if len(str1) == len(str2):
        diff = sum(s1 != s2 for s1, s2 in zip(str1, str2))
        return diff <= 1

import unittest
class Test(unittest.TestCase):
    dataT = [
    ("pale", "ple"),
    ("pales", "pale"),
    ("pale", "bale"),
    ("hooge", "hoge"),
    ("hhoge", "hoge"),
    ("fhoge", "hoge"),
    ]
    dataF = [
    ("pale", "bake"),
    ("hoge", "huga"),
    ("hoge", "hogeho")
    ]

    def test1(self):
        for data in self.dataT:
            self.assertTrue(is_convertible(*data))
        for data in self.dataF:
            self.assertFalse(is_convertible(*data))

    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test2(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = is_convertible(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
