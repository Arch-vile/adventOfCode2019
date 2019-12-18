
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
