import sys
from math import floor


def calculate_mass(mass):
    fuel_need = needed_fuel(mass)
    if fuel_need <= 0:
        return 0
    else:
        return fuel_need + calculate_mass(fuel_need)


def calculate_mass_old(x):
    fuel = needed_fuel(x)
    remaining_fuel = fuel

    while remaining_fuel > 0:
        new_remaining_fuel = max(needed_fuel(remaining_fuel), 0)
        fuel += new_remaining_fuel
        remaining_fuel = new_remaining_fuel

    return fuel


def needed_fuel(remaining_fuel):
    return floor(remaining_fuel / 3) - 2


def process_input(input_file):
    f = open(input_file)
    fuel = 0
    for moduleWeight in f:
        fuel += calculate_mass(int(moduleWeight))

    print(fuel)


if __name__ == "__main__":
    process_input(sys.argv[1])
