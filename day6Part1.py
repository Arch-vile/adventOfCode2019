# find body from dict, if not present then create and return
def get_body(dictionary, body_name):
    if body_name not in dictionary:
        dictionary[body_name] = Body(body_name)

    return dictionary[body_name]


def calculate_orbits_from_map(map):
    bodies_dict = {}
    for orbit_relation in map:
        body_names = orbit_relation.split(")")
        body1 = get_body(bodies_dict, body_names[0])
        body2 = get_body(bodies_dict, body_names[1])
        body1.orbitors.append(body2)

    return calculate_orbits(bodies_dict["COM"])


def calculate_orbits(body, distance=0):
    if not body.orbitors:
        return distance
    else:
        orbits = map(lambda b: calculate_orbits(b, distance + 1), body.orbitors)
        return sum(orbits, distance)


class Body:
    def __init__(self, name):
        self.orbitors = []
        self.name = name

    def add_orbitor(self, body):
        self.orbitors.append(body)
