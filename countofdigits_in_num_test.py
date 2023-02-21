import sys
sys.path.append("D:\Python_pgms")

import countofdigits_in_num

import unittest
class Test_total(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(countofdigits_in_num.digitcount(452356),6)
    def testcase_2(self):
        self.assertEqual(countofdigits_in_num.digitcount(-4321),"cant count negative numbers")
    def testcase_3(self):
        self.assertEqual(countofdigits_in_num.digitcount(0),0)

if __name__=="__main__":
    unittest.main()
