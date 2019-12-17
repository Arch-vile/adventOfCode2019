import unittest

from solutionStep1 import calculate_mass


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_fuel(self):
        self.assertEqual(calculate_mass(30), 8)



if __name__ == '__main__':
    unittest.main()
