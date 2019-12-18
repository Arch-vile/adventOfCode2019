
def run_program(program):

    for index in range(0,len(program),4):
        op_code = program[index]
        if op_code == 99:
            return program
        term1_index = program[index+1]
        term2_index = program[index+2]
        store_index = program[index+3]
        program[store_index] = program[term1_index] + program[term2_index]

    return program
