import sys


def calc(left, right, op_code):
    switch = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
    }

    return switch.get(op_code)(left, right)


def run_program(memory):
    for instruction_pointer in range(0, len(memory), 4):
        op_code = memory[instruction_pointer]
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


def process_input(input_file):
    f = open(input_file)
    values = f.readline().split(",")
    program = [int(x) for x in values]
    program[1] = 12
    program[2] = 2
    print(run_program(program)[0])


if __name__ == "__main__":
    process_input(sys.argv[1])
