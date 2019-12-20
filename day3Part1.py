import re


def calculate_steps(step):
    split_step = re.match('([RLUD]+)([0-9]*)', step)
    amount = int(split_step.group(2))
    direction = split_step.group(1)

    switch = {
        "R": lambda x: (1, 0),
        "U": lambda x: (0, 1),
    }

    direction_step = switch.get(direction)
    return list(map(direction_step, range(amount)))


def calculate_coordinates(path):
    map(calculate_steps, path)

    return calculate_steps()
