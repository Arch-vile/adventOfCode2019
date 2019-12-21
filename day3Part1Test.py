import re
import unittest

from day3Part1 import calculate_coordinates, calculate_steps


class MyTestCase(unittest.TestCase):

    def test_tuple(self):
        self.assertEqual(
            (3, 5)[1], (3, 5)[1]
        )


    def test_one_step(self):
        self.assertEqual(
            [(0, 0), (1, 0), (2, 0)], calculate_coordinates(["R2"])
        )


    def test_step_conversion(self):
        self.assertEqual(
            [(1, 0), (1, 0)], calculate_steps("R2")
        )

    def test_step_conversion_UP(self):
        self.assertEqual(
            [(0, 1), (0, 1), (0, 1)], calculate_steps("U3")
        )


if __name__ == '__main__':
    unittest.main()
