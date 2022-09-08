# This file will be used to test the code written in String_Calculator.py 
# This is the file at initial commit

import unittest
import String_Calculator


class TestString_Calculator(unittest.TestCase):

    def setUp(self):
        pass
    # tests for test case 3
    def test_add_str(self):
        self.assertEqual(String_Calculator.add(['1', '2', '4', '8','a']), 16)
        self.assertEqual(String_Calculator.add(['f', 'u', 'c', 'k']), 41)
        self.assertEqual(String_Calculator.add(['1', 'z', '4', '8', 'a']), 40)
        self.assertEqual(String_Calculator.add(['a', 'b', 'c', '8', 'a']), 15)
        with self.assertRaises(Exception):
            StringCalculator.add(['b', 'c', 'd', 'F', 'a'])

      
      
if __name__ == '__main__':
    unittest.main()
