import unittest

from day2.solutionPart1 import run_program


class MyTestCase(unittest.TestCase):

    def test_single_sum(self):
        self.assertEqual(
            [2, 0, 0, 0, 99],
            run_program([1, 0, 0, 0, 99])
        )


    def test_single_sum2(self):
        self.assertEqual(
            [3, 1, 2, 0, 99],
            run_program([1, 1, 2, 0, 99])
        )

if __name__ == '__main__':
    unittest.main()
