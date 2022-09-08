# This file will be used to test the code written in String_Calculator.py 
# This is the file at initial commit

import unittest
import String_Calculator


class TestString_Calculator(unittest.TestCase):

    def setUp(self):
        pass
    # test case 2
    def test_add(self):
        # test case where we add 2 numbers together
        self.assertEqual(String_Calculator.add(['1', '2']), 3)
        self.assertEqual(String_Calculator.add(['1', '2', '4', '8']), 15)
        self.assertEqual(String_Calculator.add(['1', '2', '-3','6']), 6)
        self.assertEqual(String_Calculator.add(['-1', '-2']), -3)

      
      
if __name__ == '__main__':
    unittest.main()
