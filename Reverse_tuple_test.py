import sys
sys.path.append("D:\Python_pgms")
import unittest

import Reverse_tuple
class Test_Dict(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Reverse_tuple.reverse((10,20,30,40,50,60)),((60, 50, 40, 30, 20, 10)))

if __name__ == "__main__":
    unittest.main()
