import sys
sys.path.append("D:\Python_pgms")
import first_largest

import unittest
class Test_largestnumbers(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(first_largest.largest([20,590,13,595]),595)
   
if __name__=="__main__":
    unittest.main()
