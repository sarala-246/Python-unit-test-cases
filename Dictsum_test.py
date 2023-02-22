import sys
sys.path.append("D:\Python_pgms")

import Dictsum

import unittest
class Test_sumofdict(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(Dictsum.sumdict({'A':10,'B':30,'C':50}),90)

if __name__=="__main__":
    unittest.main()
