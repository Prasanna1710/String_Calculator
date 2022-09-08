# This file will be used to test the code written in String_Calculator.py 
# This is the file at initial commit

import unittest
import String_Calculator


class TestString_Calculator(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_addString(self):
        # test case where we return zero for blanck input string
        self.assertEqual(String_Calculator.addString(''), 0)
        self.assertEqual(String_Calculator.addString('1'), 1)
        self.assertEqual(String_Calculator.addString('2'), 2)

      
      
if __name__ == '__main__':
    unittest.main()
