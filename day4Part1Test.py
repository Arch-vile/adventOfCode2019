import unittest


def check_adjacent_digits(param):
    pass


class Day4Part1Tester(unittest.TestCase):

    def test_check_adjacent_digits(self):
        self.assertEqual(
            True, check_adjacent_digits(4566789)
        )

    if __name__ == '__main__':
        unittest.main()
