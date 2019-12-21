import re
import unittest

from day3Part1 import calculate_coordinates, calculate_steps, determine_crosspoints


class MyTestCase(unittest.TestCase):

    def test_tuple(self):
        self.assertEqual(
            (3, 5)[1], (3, 5)[1]
        )

    def test_one_step(self):
        self.assertEqual(
            [(0, 0), (1, 0), (2, 0)], calculate_coordinates(["R2"])
        )

    def test_n_steps(self):
        self.assertEqual(
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (-1, 2), (-1, 1), (-1, 0), (-1, -1)],
            calculate_coordinates(["R2", "U2", "L3", "D3"])
        )

    def test_step_conversion(self):
        self.assertEqual(
            [(1, 0), (1, 0)], calculate_steps("R2")
        )

    def test_step_conversion_UP(self):
        self.assertEqual(
            [(0, 1), (0, 1), (0, 1)], calculate_steps("U3")
        )

    def test_one_crosspoint(self):
        self.assertEqual(
            {(1, 0)}, determine_crosspoints([(0, 0), (1, 0)], [(0, 0), (1, 0)])
        )

    def test_n_crospoints(self):
        self.assertEqual(
            {(1, 0), (2, 5)}, determine_crosspoints(
                [(0, 0), (1, 0), (4, 6), (2, 5)],
                [(0, 0), (2, 5), (1, 0), (1, 2)])
        )


if __name__ == '__main__':
    unittest.main()
