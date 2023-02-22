import sys
sys.path.append("D:\Python_pgms")

import filter_dict
import unittest
class Test_filter(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(filter_dict.filterdict({'Jack': 12000, 'Max': 20000, 'Hack': 19000, 'Nack': 80000}),{'Jack': 12000,'Hack': 19000})

if __name__=="__main__":
    unittest.main()
