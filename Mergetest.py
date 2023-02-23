import sys
sys.path.append("D:\Python_pgms")
import Merge

import unittest


class Test_merge(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Merge.merge([5,6,3,4,2,1]),([0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 8, 10]))
    def testcase_2(self):
        self.assertEqual(Merge.merge([10,8,3,6,0,1]),([0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 8, 10]))


if __name__=="__main__":
    unittest.main()
