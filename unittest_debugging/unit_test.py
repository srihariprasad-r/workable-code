import unittest
from prd_code import add_multiply, division

class Simpletest(unittest.TestCase):

    @unittest.skip('demonstrated skipping')
    def doing_nothing(self):
        pass

    @unittest.expectedFailure
    def test_add(self):
        self.assertEqual(add_multiply(7,3), 10)
        self.assertEqual(add_multiply(-7,3), -4)

    def test_division(self):
        #self.assertEqual(division(6,0), 0)
        self.assertEqual(division(6,3), 2)
        self.assertRaises(ValueError, division, 3, 0)            

if __name__ == '__main__':
    unittest.main()