import unittest

from day3Part1 import calculate_coordinates, calculate_steps, \
    determine_crosspoints, find_smallest_distance, \
    find_closest_crosspoint, find_shortest_wire_distance


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
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (-1, 2),
             (-1, 1), (-1, 0), (-1, -1)],
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

    def test_manhattan(self):
        self.assertEqual(
            9, find_smallest_distance({(4, 5)})
        )

    def test_n_manhattan(self):
        self.assertEqual(
            5, find_smallest_distance({(4, 5), (2, 3), (55, 21)})
        )

    def test_find_closest_crosspoint(self):
        self.assertEqual(
            159, find_closest_crosspoint(
                ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"])
        )

    def test_find_closest_crosspoint_test2(self):
        self.assertEqual(
            6, find_closest_crosspoint(
                ["R8", "U5", "L5", "D3"],
                ["U7", "R6", "D4", "L4"])
        )

    def test_find_closest_crosspoint_test3(self):
        self.assertEqual(
            135, find_closest_crosspoint(
                ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33",
                 "U53", "R51"],
                ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6",
                 "R7"])
        )

    def test_find_shortest_wire_distance(self):
        self.assertEqual(
            30, find_shortest_wire_distance(
                ["R8", "U5", "L5", "D3"],
                ["U7", "R6", "D4", "L4"])
        )

    if __name__ == '__main__':
        unittest.main()
