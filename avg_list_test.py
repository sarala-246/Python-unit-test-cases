import sys
sys.path.append("D:\Python_pgms")

import Avg_list

import unittest
class Test_avg(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Avg_list.average([10,20,30,40,50]),30)

if __name__=="__main__":
    unittest.main()
