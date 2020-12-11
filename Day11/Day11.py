'''Day 11'''

def create_map():
    '''Create a list of lists representing points and rows on the map'''

    map_list = []

    with open('data.txt', 'r') as f:
        while(True):
            line = f.readline()
            if not line:
                break
            row = []
            for point in line:
                if point != "\n":
                    row.append(point)
            map_list.append(row)

    return map_list

create_map('data.txt')
for row in create_map:
    print(row)