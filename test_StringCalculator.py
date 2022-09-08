# This file will be used to test the code written in String_Calculator.py 
# This is the file at initial commit

import unittest
import String_Calculator


class TestString_Calculator(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_addString(self):
        # test case 1
        # test case where we return zero for blanck input string
        self.assertEqual(String_Calculator.addString(''), 0)
        self.assertEqual(String_Calculator.addString('1'), 1)
        self.assertEqual(String_Calculator.addString('2'), 2)
    def test_add(self):
        # test case 2 and part 3 of test case 1
        # test case where we add 2 numbers together
        self.assertEqual(String_Calculator.add(['1', '2']), 3)
        self.assertEqual(String_Calculator.add(['1', '2', '4', '8']), 15)
        self.assertEqual(String_Calculator.add(['1', '2', '-3','6']), 6)
        self.assertEqual(String_Calculator.add(['-1', '-2']), -3)

    # test case 3
    def test_add_str(self):
        self.assertEqual(String_Calculator.add(['1', '2', '4', '8', 'a']), 16)
        self.assertEqual(String_Calculator.add(['f', 'u', 'c', 'k']), 41)
        self.assertEqual(String_Calculator.add(['1', 'z', '4', '8', 'a']), 40)
        self.assertEqual(String_Calculator.add(['a', 'b', 'c', '8', 'a']), 15)
        with self.assertRaises(Exception):
            StringCal.add(['b', 'c', 'd', 'F', 'a'])

    # test case 4 and 5
    # single and multiple negatives
    def test_add_N(self):
        with self.assertRaises(Exception):
            StringCal.add(['1','2','-1'])
        self.assertEqual(StringCal.add(['1','2']),3)
        with self.assertRaises(Exception):
            StringCal.add(['1','2','-1','-2','-3'])

    # test case 6
    def test_add_1000(self):
        self.assertEqual(String_Calculator.add(['1', '2', '4', '8','1000']), 1015)
        self.assertEqual(String_Calculator.add(['1', '2', '4', '8','2234']), 15)
        self.assertEqual(String_Calculator.add(['1', '2', '4', '8','1233','1220202','999']), 1014)
    
    # tets case 7
    # test case for n numbers - newline separated
    def test_addstr_newline(self):
        self.assertEqual(String_Calculator.addString('1','\n2'), 3)

      
      
if __name__ == '__main__':
    unittest.main()
