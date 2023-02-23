import sys
sys.path.append("D:\Python_pgms")
import sortingnestedlist

import unittest
class Test_sort(unittest.TestCase):
    def testcase_1(self):
        self.assertListEqual(sortingnestedlist.sorting([[20,88],[57,18],[65,26],[13,84]]),[[57, 18], [65, 26], [13, 84], [20, 88]])

if __name__=="__main__":
    unittest.main()
