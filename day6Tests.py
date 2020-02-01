import unittest

from day5Part1 import Body, calculate_orbits
from intcode_computer import run_program


class MyTestCase(unittest.TestCase):

    def test_foo(self):
        body1 = Body()
        body2 = Body()
        body1.add_orbitor(body2)
        self.assertEqual(
            1,
            calculate_orbits(body1)
        )


if __name__ == '__main__':
    unittest.main()
