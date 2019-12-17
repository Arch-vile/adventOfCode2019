
from math import floor


def calculate_mass(x):
    first_mass = floor(x / 3) - 2
    second_mass = max(floor(first_mass / 3) - 2, 0)
    return first_mass + second_mass
