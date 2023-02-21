import sys
sys.path.append("D:\Python_pgms")
import alternate_fifth_ele
import unittest

class Test_Alternate(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(alternate_fifth_ele.alter(10),[5,10])
    def testcase_2(self):
        self.assertEqual(alternate_fifth_ele.alter(50),[5, 10, 15, 20, 25, 30, 35, 40, 45, 50])


if __name__=="__main__":
    unittest.main()
