import sys
sys.path.append("D:\Python_pgms")
import second_largest

import unittest
class Test_largestnumbers(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(second_largest.secondlargest([10,25,600,509,525]),525)

if __name__=="__main__":
    unittest.main()
