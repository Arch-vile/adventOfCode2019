
def calculate_orbits(body, distance=0):
    if not body.orbitors:
        return distance
    else:
        orbits = map(lambda b: calculate_orbits(b, distance+1), body.orbitors)
        return sum(orbits, distance)


class Body:
    def __init__(self):
        self.orbitors = []

    def add_orbitor(self, body):
        self.orbitors.append(body)

