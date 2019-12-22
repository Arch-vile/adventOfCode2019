import unittest

from day4Part1 import check_adjacent_digits, check_increasing_digits, \
    find_solution


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

    def test_check_increasing_digits(self):
        self.assertEqual(
            True, check_increasing_digits(123)
        )
        self.assertEqual(
            True, check_increasing_digits(14557)
        )
        self.assertEqual(
            False, check_increasing_digits(145571)
        )

    def test_solution(self):
        find_solution()

    if __name__ == '__main__':
        unittest.main()
