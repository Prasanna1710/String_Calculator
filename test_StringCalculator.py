# This file will be used to test the code written in String_Calculator.py 
# This is the file at initial commit

import unittest
import String_Calculator


class TestString_Calculator(unittest.TestCase):

    def setUp(self):
        pass
    def test_add_str(self):
        self.assertEqual(String_Calculator.add(['1', '2', '4', '8','1','1000']), 1016)
        self.assertEqual(String_Calculator.add(['6', '21', '3', '11','10000']), 41)
        self.assertEqual(String_Calculator.add(['1', '26', '4', '8', '1','1009','3827','21718']), 40)

      
if __name__ == '__main__':
    unittest.main()
