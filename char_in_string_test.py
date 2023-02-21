import sys
sys.path.append("D:\Python_pgms")

import char_in_string

import unittest
class Test_res(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(char_in_string.totalchar(""),0)
        
    def testcase_2(self):
        self.assertEqual(char_in_string.totalchar("sarala"),6)
        

if __name__=="__main__":
    unittest.main()
