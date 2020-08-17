import unittest
from prd_code import add_multiply, division
from unittest.mock import Mock, patch

class Simpletest(unittest.TestCase):

    @patch('prd_code.multiply')   
    def test_add(self, mock_multiply):

        x = 3
        y = 6

        mock_multiply.return_value = 1

        addition, multiply = add_multiply(x, y)

        mock_multiply.assert_called_once_with(x, y)
        self.assertEqual(9, addition)
        self.assertEqual(18, multiply)


if __name__ == '__main__':
    unittest.main()