import unittest
from prd_code import add, division

class Simpletest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(7,3), 10)
        self.assertEqual(add(-7,3), -4)

    def test_division(self):
        self.assertEqual(division(6,0), 0)
        self.assertEqual(division(6,3), 2)
        self.assertRaises(ValueError, division, 10, 1)

if __name__ == '__main__':
    unittest.main()