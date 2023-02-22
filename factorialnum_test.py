import sys
sys.path.append("D:\Python_pgms")

import factorialnum

import unittest


class Test_Fact(unittest.TestCase):
     def testcase_1(self):
         self.assertEqual(factorialnum.factorial(5),120)

if __name__=="__main__":
    unittest.main()
