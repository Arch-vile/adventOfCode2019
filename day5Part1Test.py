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


if __name__ == '__main__':
    unittest.main()
