import sys

OP_CODE_LENGTH = 2


def calc(instruction, memory):
    switch = {
        1: lambda inst, mem:
            mem.read_param(inst.mode1) + mem.read_param(inst.mode2),
        2: lambda inst, mem:
            mem.read_param(inst.mode1) * mem.read_param(inst.mode2),
        3: lambda inst, mem:
            mem.program_input,
        4: lambda inst, mem:
            mem.read_param(inst.mode1)
    }

    value = switch.get(instruction.op_code)(instruction, memory)

    if instruction.op_code == 4:
        memory.add_output(value)
    else:
        address = memory.read_param("IMMEDIATE")
        memory.set_value(address, value)


class Memory:
    def __init__(self, data1, program_input):
        self.data = data1
        self.pointer = 0
        self.program_input = program_input
        self.output = []

    def next_instruction(self):
        next_instruction = Instruction(self.data[self.pointer])
        self.pointer = self.pointer + 1
        return next_instruction

    def set_value(self, address, value):
        self.data[address] = value

    def read_param(self, mode):
        old_pointer = self.pointer
        self.pointer = self.pointer + 1
        if mode == "POSITION":
            return self.data[self.data[old_pointer]]
        else:
            return self.data[old_pointer]

    def add_output(self, value):
        self.output.append(value)


def run_program(program, program_input=0):
    memory = Memory(program, program_input)

    while True:

        instruction = memory.next_instruction()

        if instruction.op_code == 99:
            return [memory.data, memory.output]

        calc(instruction, memory)


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


def process_input(input_file, program_input):
    program_input = int(program_input)
    program = read_input(input_file)
    print(run_program(program, program_input)[1])


def read_input(input_file):
    f = open(input_file)
    values = f.readline().split(",")
    program = [int(x) for x in values]
    return program


if __name__ == "__main__":
    process_input(sys.argv[1], sys.argv[2])
