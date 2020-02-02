import unittest

from day6 import Body, calculate_orbits, calculate_orbits_from_map


class MyTestCase(unittest.TestCase):

    def test_two_bodies(self):
        body1 = Body("1")
        body2 = Body("2")
        body1.add_orbitor(body2)
        self.assertEqual(
            1,
            calculate_orbits(body1)
        )

    def test_simple_chain(self):
        body1 = Body("1")
        body2 = Body("2")
        body3 = Body("3")
        body1.add_orbitor(body2)
        body2.add_orbitor(body3)
        self.assertEqual(
            3,
            calculate_orbits(body1)
        )

    def test_simple_branch(self):
        body1 = Body("1")
        body2 = Body("2")
        body3 = Body("3")
        body4 = Body("4")
        body1.add_orbitor(body2)
        body2.add_orbitor(body3)
        body2.add_orbitor(body4)
        self.assertEqual(
            5,
            calculate_orbits(body1)
        )

    def test_read_input(self):
        self.assertEqual(
            5,
            calculate_orbits_from_map(["COM)2", "2)3", "2)4"])
        )


if __name__ == '__main__':
    unittest.main()
