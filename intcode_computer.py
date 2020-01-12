import sys


def calc(left, right, op_code):
    switch = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
    }

    return switch.get(op_code)(left, right)


def run_program(memory):
    memory = list(map(int, memory))
    for instruction_pointer in range(0, len(memory), 4):
        instruction_code = memory[instruction_pointer]
        instruction = Instruction(instruction_code)

        op_code = instruction.op_code
        # parameter_mode1 = instruction.get_parameter_mode(0)
        # parameter_mode2 = instruction_code_parts.get_parameter_mode(1)
        # parameter_mode3 = instruction_code_parts.get_parameter_mode(2)

        if op_code == 99:
            return memory
        param1_address = memory[instruction_pointer + 1]
        param2_address = memory[instruction_pointer + 2]
        param3_address = memory[instruction_pointer + 3]
        memory[param3_address] = calc(
            memory[param1_address],
            memory[param2_address],
            op_code)

    return memory


def get_value_of_last_two_digits(instruction_code):
    last_two_digits = str(instruction_code)[-2:]
    return int(last_two_digits)


class Instruction:
    def __init__(self, instruction_code):
        self.op_code = get_value_of_last_two_digits(instruction_code)


def process_input(input_file):
    program = readInput(input_file)
    program[1] = 12
    program[2] = 2
    print(run_program(program)[0])


def readInput(input_file):
    f = open(input_file)
    values = f.readline().split(",")
    program = [int(x) for x in values]
    return program


if __name__ == "__main__":
    process_input(sys.argv[1])
