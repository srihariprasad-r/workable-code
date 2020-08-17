import unittest
from employee import  Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        print('setup')
        self.emp1 = Employee('John', 'Doe', 50000)
        self.emp2 = Employee('Jack', 'Mars', 40000)

    def tearDown(self):
        print('teardown')
        pass

    @unittest.skip
    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp1.email, 'John.Doe@email.com')

        self.emp1.first = 'Jones'

        self.assertEqual(self.emp1.email, 'Jones.Doe@email.com')
        self.assertEqual(self.emp2.email, 'Jack.Mars@email.com')

        self.assertIsInstance(self.emp1, Employee)

if __name__ == '__main__':
    unittest.main()