import sys
sys.path.append("D:\Python_pgms")
import primetest

import unittest


class Test_prime(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(primetest.prime(3),"yes it is prime")
    def testcase_2(self):
        self.assertEqual(primetest.prime(4),"it is not prime")
    def testcase_3(self):
        self.assertEqual(primetest.prime(-1),"zero")
    def testcase_4(self):
        self.assertEqual(primetest.prime(1),"neither prime nor composite")
    def testcase_5(self):
        self.assertEqual(primetest.prime(0),"zero")

if __name__=="__main__":
    unittest.main()
