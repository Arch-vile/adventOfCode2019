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


def determine_crosspoints(path1_coordinates, path2_coordinates):
    crosspoints = set(path1_coordinates).intersection(path2_coordinates)
    crosspoints.discard((0, 0))
    return crosspoints


def find_smallest_distance(coordinates):
    # map(f, iterable)
    return min(list(map(lambda c: abs(c[0]) + abs(c[1]), coordinates)))


def find_closest_crosspoint(path1, path2):
    path1_coords = calculate_coordinates(path1)
    path2_coords = calculate_coordinates(path2)
    return find_smallest_distance(
        determine_crosspoints(path1_coords, path2_coords))


def run_program(input_file):
    f = open(input_file)
    path1 = f.readline().split(",")
    path2 = f.readline().split(",")
    print(find_closest_crosspoint(path1, path2))


if __name__ == "__main__":
    run_program(sys.argv[1])
