import sys
sys.path.append("D:\Python_pgms")

import ith_occurance

import unittest
class Test_occurance(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(ith_occurance.ithoccurance(['hi','hello','python','hi','hello','hi']),['hi','hello','python','hello','hi'])

if __name__=="__main__":
    unittest.main()
