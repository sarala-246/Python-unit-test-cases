import sys
sys.path.append("D:\Python_pgms")
import divi_by_three_and_four_pgm

 
import unittest

class Test_divisible(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(divi_by_three_and_four_pgm.divis(100),"yes")
    def testcase_2(self):
        self.assertEqual(divi_by_three_and_four_pgm.divis(50),"yes")


if __name__=="__main__":
    unittest.main()
