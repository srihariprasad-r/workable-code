import unittest
from prd_code import add_multiply, division, add_multiply_subtract
from unittest.mock import Mock, patch

class Simpletest(unittest.TestCase):

    @patch('prd_code.multiply')   
    def test_add_multiply(self, mock_multiply):

        x = 3
        y = 6

        mock_multiply.return_value = 18

        addition, multiply = add_multiply(x, y)

        mock_multiply.assert_called_once_with(x, y)
        self.assertEqual(9, addition)
        self.assertEqual(18, multiply)


    def test_add_multiply_subtract(self):     
        with patch('prd_code.multiply') as mock_multiply:
            with patch('prd_code.subtract') as mock_subtract:
                mock_subtract.return_value = 3
                addition, subtract = add_multiply_subtract(3, 6)
                self.assertEqual(3, subtract) 
                self.assertEqual(9, addition)                   
                mock_multiply.return_value = 18
                addition, multiply = add_multiply_subtract(6, 3)
                self.assertEqual(18, multiply)                 
                self.assertEqual(9, addition)                
            

if __name__ == '__main__':
    unittest.main()