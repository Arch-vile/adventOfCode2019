import unittest

from solutionPart2 import calculate_mass


class MyTestCase(unittest.TestCase):

    def test_one_extra_fuel(self):
        self.assertEqual(22, calculate_mass(60))

    def test_fuel2(self):
        self.assertEqual(2, calculate_mass(14))

    def test_several_extras(self):
        self.assertEqual(966, calculate_mass(1969))

    def test_more_extras(self):
        self.assertEqual(50346, calculate_mass(100756))


if __name__ == '__main__':
    unittest.main()
