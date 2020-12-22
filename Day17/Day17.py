'''Day 17'''

MAX = 1000000000000000000000000000
MIN = -1000000000000000000000000000

def read_in_data(file) -> list:
    with open(file, 'r') as f:
        return [line for line in f.readlines()]

class Location:

    def __init__(self, x: int=None, y: int=None, z: int=None, c: str=None):
        self.x = x
        self.y = y
        self.z = z
        self.c = c

class Dimension:

    def __init__(self):
        self.locations = []

    def add_location(self, location: Location):
        self.locations.append(location)

    def is_active(self, x: int, y: int, z: int):
        for location in self.locations:
            if location.x == x and location.y == y and location.z == z:
                return location.c == '#'
        return False

    def get_total_active(self):
        active = 0
        for location in self.locations:
            if location.c == '#':
                active += 1
        return active

    def get_x_values(self):
        min_and_max = [MAX, MIN]
        for location in self.locations:
            if location.x < min_and_max[0]:
                min_and_max[0] = location.x
            if location.x > min_and_max[1]:
                min_and_max[1] = location.x
        return min_and_max
    
    def get_y_values(self):
        min_and_max = [MAX, MIN]
        for location in self.locations:
            if location.y < min_and_max[0]:
                min_and_max[0] = location.y
            if location.y > min_and_max[1]:
                min_and_max[1] = location.y
        return min_and_max

    def get_z_values(self):
        min_and_max = [MAX, MIN]
        for location in self.locations:
            if location.z < min_and_max[0]:
                min_and_max[0] = location.z
            if location.z > min_and_max[1]:
                min_and_max[1] = location.z
        return min_and_max

def solve(input_strings):
    dimension = Dimension()
    for y in range(len(input_strings)):
        s = input_strings[y]
        for x in range(len(s)):
            dimension.add_location(Location(x=x, y=y, z=0, c=s[x]))

    for i in range(6):
        new_dimension = Dimension()
        x_range = dimension.get_x_values()
        y_range = dimension.get_y_values()
        z_range = dimension.get_z_values()
        for z in range(z_range[0] - 1, z_range[1] + 2):
            for y in range(y_range[0] - 1, y_range[1] + 2):
                for x in range(x_range[0] - 1, x_range[1] + 2):
                    active = 0
                    for z_off in range(-1, 2):
                        for y_off in range(-1, 2):
                            for x_off in range(-1, 2):
                                if z_off == 0 and y_off == 0 and x_off == 0:
                                    continue

                                if dimension.is_active(x=x+x_off, y=y+y_off, z=z+z_off):
                                    active += 1
                    if dimension.is_active(x=x, y=y, z=z):
                        if active == 2 or active == 3:
                            new_dimension.add_location(Location(x=x, y=y, z=z, c='#'))
                        else:
                            new_dimension.add_location(Location(x=x, y=y, z=z, c='.'))
                    else:
                        if active == 3:
                            new_dimension.add_location(Location(x=x, y=y, z=z, c='#'))
                        else:
                            new_dimension.add_location(Location(x=x, y=y, z=z, c='.'))    
        dimension = new_dimension
    print(f"Total Active Nodes: {new_dimension.get_total_active()}")

space = read_in_data('data.txt')
solve(space)