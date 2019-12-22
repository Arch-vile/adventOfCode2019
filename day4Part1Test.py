import unittest

from day4Part1 import check_adjacent_digits


class Day4Part1Tester(unittest.TestCase):

    def test_check_adjacent_digits(self):
        self.assertEqual(
            True, check_adjacent_digits(4566789)
        )
        self.assertEqual(
            True, check_adjacent_digits(1111111)
        )
        self.assertEqual(
            True, check_adjacent_digits(11234)
        )
        self.assertEqual(
            True, check_adjacent_digits(12344)
        )
        self.assertEqual(
            False, check_adjacent_digits(1234)
        )


    if __name__ == '__main__':
        unittest.main()
