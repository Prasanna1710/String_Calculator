# This file will be used to test the code written in String_Calculator.py 
# This is the file at initial commit

import unittest
import String_Calculator


class TestString_Calculator(unittest.TestCase):

    def setUp(self):
        pass
    def test_add_N(self):
        with self.assertRaises(Exception):
            String_Calculator.add(['1','2','-1'])
        self.assertEqual(String_Calculator.add(['1','2']),3)
        # Added for Testcase 5
        with self.assertRaises(Exception):
            String_Calulator.add(['1','2','-1','-2','-3'])

      
      
if __name__ == '__main__':
    unittest.main()
