import unittest

from intcode_computer import run_program


class MyTestCase(unittest.TestCase):

    def test_string_opcode(self):
        self.assertEqual(
            [2, 0, 0, 0, 99],
            run_program(["1", 0, 0, 0, 99])
        )

    def test_zero_padded_opcode(self):
        self.assertEqual(
            [2, 0, 0, 0, 99],
            run_program(["01", 0, 0, 0, 99])
        )


if __name__ == '__main__':
    unittest.main()
