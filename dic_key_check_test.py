import sys
sys.path.append("D:\Python_pgms")
import dic_key_check

import unittest
class keycheck(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(dic_key_check.checkkey({'apple':10,'b':20,'name':'sarala'},'apple'),True)

if __name__=="__main__":
    unittest.main()
