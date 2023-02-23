import sys
sys.path.append("D:\Python_pgms")
import Reverselist


import unittest
class Test_rev(unittest.TestCase):
    def testcase_1(self):
        self.assertListEqual(Reverselist.reverse([2,4,6,8]),[8,6,4,2])

if __name__=="__main__":
    unittest.main()       
