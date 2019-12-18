import sys

from day2Part1 import readInput, run_program


def gravityAssist(file):
    memory = readInput(file)
    original_memory = memory.copy()
    for noun in range(99):
        for verb in range(99):
            memory[1] = noun
            memory[2] = verb
            output = run_program(memory)[0]
            if output == 19690720:
                print(noun, verb)
                return
            else:
                memory = original_memory.copy()


if __name__ == "__main__":
    gravityAssist(sys.argv[1])
