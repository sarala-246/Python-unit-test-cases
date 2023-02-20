import sys
sys.path.append("D:\Python_pgms")
import Fibonacci

import unittest

class Test_Fibonacci(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Fibonacci.fibonacci(10),[0,1,1,2,3,5,8,13,21,34])
    def testcase_1(self):
        self.assertEqual(Fibonacci.fibonacci(5),[0,1,1,2,3])
    def testcase_1(self):
        self.assertEqual(Fibonacci.fibonacci(7),[0,1,1,2,3,5,8])


if __name__=="__main__":
    unittest.main()
