import sys
sys.path.append("D:\Python_pgms")

import palindromenum

import unittest
class Test_pallin(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(palindromenum.palindrome(121),"the number is palindrome")
    def testcase_2(self):
        self.assertEqual(palindromenum.palindrome(-4),"negative numbers")
    def testcase_3(self):
        self.assertEqual(palindromenum.palindrome(12),"the number is not palindrome")

if __name__=="__main__":
    unittest.main()
