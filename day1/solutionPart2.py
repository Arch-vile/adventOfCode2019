from math import floor


def calculate_mass(x):
    fuel = floor(x / 3) - 2
    remaining_fuel = fuel

    while remaining_fuel > 0:
        new_remaining_fuel = max(floor(remaining_fuel / 3) - 2, 0)
        fuel += new_remaining_fuel
        remaining_fuel = new_remaining_fuel

    return fuel
