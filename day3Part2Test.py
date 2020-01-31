import unittest

from day3Part2 import find_shortest_wire_distance


class MyTestCase(unittest.TestCase):

    def test_find_shortest_wire_distance(self):
        self.assertEqual(
            30, find_shortest_wire_distance(
                ["R8", "U5", "L5", "D3"],
                ["U7", "R6", "D4", "L4"])
        )

    if __name__ == '__main__':
        unittest.main()
