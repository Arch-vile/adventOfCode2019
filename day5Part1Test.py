import unittest

from intcode_computer import run_program


class MyTestCase(unittest.TestCase):

    def test_parameter_mode_op_code(self):
        self.assertEqual(
            [[1001, 0, 0, 0, 99], []],
            run_program([1001, 0, 0, 0, 99])
        )

    def test_input_reading(self):
        self.assertEqual(
            [[1, 0, 99], []],
            run_program([3, 0, 99], 1)
        )

    def test_output_printing(self):
        self.assertEqual(
            [[4, 0, 99], [4]],
            run_program([4, 0, 99], 1)
        )

    def test_negative_numbers(self):
        self.assertEqual(
            [[-7, -5, -2, 0, 99], []],
            run_program([1101, -5, -2, 0, 99])
        )

    def test_jump_if_true(self):
        self.assertEqual(
            [[5, 1, 5, 1, 1, 2, 1, 2, 0, 99], []],
            run_program([1105, 1, 5, 1, 1, 2, 1, 2, 0, 99])
        )

    def test_jump_if_false(self):
        self.assertEqual(
            [[5, 0, 5, 1, 1, 1, 1, 2, 0, 99], []],
            run_program([1106, 0, 5, 1, 1, 1, 1, 2, 0, 99])
        )


if __name__ == '__main__':
    unittest.main()
