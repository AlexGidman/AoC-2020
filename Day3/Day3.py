'''Day 3'''

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


def count_trees(RIGHT, DOWN):
    """Counts number of trees given movements right and down"""
    
    # Create map
    map_list = create_map()

    tree_count = 0

    # Start coordinates
    x = 0
    y = 0

    for row in range(len(map_list)):

        if map_list[y][x] == "#":
            tree_count += 1 

        if y == len(map_list)-1:
            break

        # if not reached end of row index and not reached bottom of map
        if x + RIGHT < (len(map_list[row])): 
            x += RIGHT
            y += DOWN
        else:
            x += RIGHT - len(map_list[row]) 
            y += DOWN

    return tree_count

# Input moves strategy
moves = [
    {'RIGHT': 1, 'DOWN': 1},
    {'RIGHT': 3, 'DOWN': 1},
    {'RIGHT': 5, 'DOWN': 1},
    {'RIGHT': 7, 'DOWN': 1},
    {'RIGHT': 1, 'DOWN': 2},
]

answer = 1
for move in moves:
    answer *= count_trees(RIGHT=move['RIGHT'], DOWN=move['DOWN'])

print(answer)