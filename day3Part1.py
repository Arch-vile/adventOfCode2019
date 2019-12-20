import re


def calculate_steps(step):
    split_step = re.match('([RLUD]+)([0-9]*)', step)
    amount = int(split_step.group(2))

    return list(map(lambda x: (1, 0), range(amount)))


def calculate_coordinates(path):
    map(calculate_steps, path)

    return calculate_steps()
