import sys

from day3Part1 import calculate_coordinates, determine_crosspoints


def wire_distance_sum(crosspoint, path1_coordinates, path2_coordinates):
    return path1_coordinates.index(crosspoint) + path2_coordinates.index(
        crosspoint)


def find_shortest_wire_distance(path1, path2):
    # Step1: Find coordinates for paths.
    # We have two lists of coordinates CA and CB
    ca = calculate_coordinates(path1)
    cb = calculate_coordinates(path2)

    # Step2: Find the cross points
    # We have list of coordinates
    crosspoints = determine_crosspoints(ca, cb)

    # Step3: For each cross point find the wire distances for both lines
    # It should be the index of the cross point in the coordinates CA and CB
    # We have list of ints indicating the sums for lines
    wire_distances = map(lambda point: wire_distance_sum(point, ca, cb),
                         crosspoints)

    # Step4: Return the min of the list
    return min(wire_distances)


def run_program(input_file):
    f = open(input_file)
    path1 = f.readline().split(",")
    path2 = f.readline().split(",")
    print(find_shortest_wire_distance(path1, path2))


if __name__ == "__main__":
    run_program(sys.argv[1])
