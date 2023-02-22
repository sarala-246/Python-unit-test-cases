import sys
sys.path.append("D:\Python_pgms")
import even_odd_list

import unittest
class Test_numbers(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(even_odd_list.evenodd([3,25,10,14,2,8,17,5]),([10, 14, 2, 8], [3, 25, 17, 5]))

if __name__=="__main__":
    unittest.main()
