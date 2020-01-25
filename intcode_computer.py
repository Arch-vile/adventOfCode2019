import sys

OP_CODE_LENGTH = 2


def calc(op_code, params):
    switch = {
        1: lambda x: x[0] + x[1],
        2: lambda x: x[0] * x[1],
    }

    return switch.get(op_code)(params)


def run_program(memory):
    for instruction_pointer in range(0, len(memory), 4):
        instruction_code = memory[instruction_pointer]
        instruction = Instruction(instruction_code)

        if instruction.op_code == 99:
            return memory

        if instruction.mode1 == "POSITION":
            param1_address = memory[instruction_pointer + 1]
            param1 = memory[param1_address]
        else:
            param1 = memory[instruction_pointer + 1]

        if instruction.mode2 == "POSITION":
           param2_address = memory[instruction_pointer + 2]
           param2 = memory[param2_address]
        else:
            param2 = memory[instruction_pointer + 2]

        param3_address = memory[instruction_pointer + 3]

        memory[param3_address] = calc(
            instruction.op_code,
            [param1, param2]
        )

    return memory


def get_value_of_last_digits(instruction_code, digit_count):
    last_digits = str(instruction_code)[-digit_count:]
    return int(last_digits)


class Instruction:
    def __init__(self, instruction_code):
        self.op_code = get_value_of_last_digits(instruction_code, OP_CODE_LENGTH)

        self.mode1 = self.as_parameter_mode(instruction_code, 0)
        self.mode2 = self.as_parameter_mode(instruction_code, 1)

    @staticmethod
    def as_parameter_mode(instruction_code, index):
        code_as_string = str(instruction_code)
        if len(code_as_string)-OP_CODE_LENGTH > index:
            param = str(code_as_string[-(index+OP_CODE_LENGTH+1)])

            if param == "0":
                return "POSITION"
            else:
                return "IMMEDIATE"
        else:
            return "POSITION"


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
