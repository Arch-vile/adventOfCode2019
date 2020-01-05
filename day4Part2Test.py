import re
import unittest

from day4Part2 import check_adjacent_digits_even


class Day4Part1Tester(unittest.TestCase):

    def test_check_adjacent_digits(self):
        self.assertEqual(
            False, check_adjacent_digits_even(123444)
        )
        self.assertEqual(
            True, check_adjacent_digits_even(12344)
        )
        self.assertEqual(
            False, check_adjacent_digits_even(11234445)
        )


    if __name__ == '__main__':
        unittest.main()
