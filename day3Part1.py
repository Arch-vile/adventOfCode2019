import re
from functools import reduce
from itertools import chain


def calculate_steps(step):
    split_step = re.match('([RLUD]+)([0-9]*)', step)
    amount = int(split_step.group(2))
    direction = split_step.group(1)

    switch = {
        "R": lambda x: (1, 0),
        "U": lambda x: (0, 1),
        "L": lambda x: (-1, 0),
        "D": lambda x: (0, -1),
    }

    direction_step = switch.get(direction)
    return list(map(direction_step, range(amount)))


def calc_next_coord(coordinates, next_step):
    # do magic
    x_coord = coordinates[-1][0] + next_step[0]
    y_coord = coordinates[-1][1] + next_step[1]
    coordinates.append((x_coord, y_coord))
    return coordinates


def calculate_coordinates(path):
    steps = flatten(map(calculate_steps, path))

    # (1, 0), (1, 0), (0, 1)
    # (1, 0), (2, 0), (2, 1)

    return list(reduce(calc_next_coord, steps, [(0, 0)]))


def flatten(foo):
    return list(chain.from_iterable(foo))
