import sys
sys.path.append("D:\Python_pgms")
import armstrongnum

import unittest
class Test_arm(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(armstrongnum.armstrong(153),"number is armstrong")
    def testcase_2(self):
        self.assertEqual(armstrongnum.armstrong(-153),"not armstrong")
    def testcase_3(self):
        self.assertEqual(armstrongnum.armstrong(0),"not armstrong")
if __name__=="__main__":
    unittest.main()

