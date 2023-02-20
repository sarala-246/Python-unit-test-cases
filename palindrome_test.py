import sys
sys.path.append("D:\Python_pgms")
import palindrome

import unittest


class Test_palindrome(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(palindrome.palindrome("malayalam"),"string is palindrome")


if __name__=="__main__":
    unittest.main()
