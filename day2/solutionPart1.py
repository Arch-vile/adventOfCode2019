import sys


def calc(left, right, op_code):
    switch = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
    }

    return switch.get(op_code)(left, right)


def run_program(program):
    for index in range(0, len(program), 4):
        op_code = program[index]
        if op_code == 99:
            return program
        term1_index = program[index + 1]
        term2_index = program[index + 2]
        store_index = program[index + 3]
        program[store_index] = calc(
            program[term1_index],
            program[term2_index],
            op_code)

    return program


def process_input(input_file):
    f = open(input_file)
    values = f.readline().split(",")
    program = [int(x) for x in values]
    program[1] = 12
    program[2] = 2
    print(run_program(program)[0])


if __name__ == "__main__":
    process_input(sys.argv[1])
