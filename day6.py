# find body from dict, if not present then create and return
import sys


def get_body(dictionary, body_name):
    if body_name not in dictionary:
        dictionary[body_name] = Body(body_name)

    return dictionary[body_name]


def calculate_orbits_from_map(orbit_map):
    bodies_dict = body_dictionary(orbit_map)
    return calculate_orbits(bodies_dict["COM"])


def body_dictionary(orbit_map):
    bodies_dict = {}
    for orbit_relation in orbit_map:
        body_names = orbit_relation.split(")")
        body1 = get_body(bodies_dict, body_names[0])
        body2 = get_body(bodies_dict, body_names[1])
        body1.orbitors.append(body2)
        body2.parent = body1
    return bodies_dict


def calculate_orbits(body, distance=0):
    if not body.orbitors:
        return distance
    else:
        orbits = map(lambda b: calculate_orbits(b, distance + 1), body.orbitors)
        return sum(orbits, distance)


def parents(body):
    parent_list = []
    while True:
        parent_list.append(body.parent)
        body = body.parent
        if body.name == "COM":
            return parent_list


def intersect(list_1, list_2):
    intersection = [value for value in list_1 if value in list_2]
    return intersection


def find_common_body(body1, body2):
    body1_parents = parents(body1)
    body2_parents = parents(body2)
    intersection = intersect(body1_parents, body2_parents)
    return body1_parents[-(len(intersection))]


# body1 must be deeper in orbit map
# return distance in tree
def distance(body1, body2):
    distance_between = 0
    while body1 is not None and body1.name != body2.name:
        distance_between += 1
        body1 = body1.parent
    return distance_between


def distance_to_santa(orbit_map):
    bodies = body_dictionary(orbit_map)
    santa = bodies["SAN"]
    you = bodies["YOU"]
    common_body = find_common_body(santa, you)
    orbit_distance_you = distance(you, common_body) - 1
    orbit_distance_santa = distance(santa, common_body) - 1
    return orbit_distance_you + orbit_distance_santa


class Body:
    def __init__(self, name):
        self.orbitors = []
        self.name = name
        self.parent = None

    def add_orbitor(self, body):
        self.orbitors.append(body)


def process_input(input_file):
    orbit_map = read_input(input_file)
    # print(calculate_orbits_from_map(orbit_map))
    print(distance_to_santa(orbit_map))

def read_input(input_file):
    return [line.rstrip('\n') for line in open(input_file)]


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    process_input(sys.argv[1])
