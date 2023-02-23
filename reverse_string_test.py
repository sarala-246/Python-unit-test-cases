import sys
sys.path.append("D:\Python_pgms")
import reverse_string

import unittest
class Test_rev(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(reverse_string.reverse("python"),'nohtyp')

if __name__=="__main__":
    unittest.main()
