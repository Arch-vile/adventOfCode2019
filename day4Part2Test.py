import unittest

from day4Part2 import check_adjacent_digits_even, find_solution, test_password


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
        self.assertEqual(
            True, check_adjacent_digits_even(22222222)
        )
        self.assertEqual(
            False, check_adjacent_digits_even(222222222)
        )
        self.assertEqual(
            True, check_adjacent_digits_even(1)
        )

    def test_matching(self):
        self.assertEqual(
            True, test_password(112233)
        )
        self.assertEqual(
            False, test_password(123444)
        )
        self.assertEqual(
            True, test_password(111122)
        )
        self.assertEqual(
            True, test_password(8)
        )

    def test_solution(self):
        print(find_solution())

    if __name__ == '__main__':
        unittest.main()
