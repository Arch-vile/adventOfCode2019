from math import floor

f = open("input.txt")


def calculate_mass(x):
    return floor(x / 3) - 2


fuel = 0
for moduleWeight in f:
    fuel += calculate_mass(int(moduleWeight))

print(fuel)
