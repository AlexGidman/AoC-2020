'''Day 12'''
from time import sleep

def read_in_data(file) -> list:
    '''Create a list of lists representing points and rows on the map'''
    tmp_list =[]
    with open(file, 'r') as f:
        tmp_list = [line.replace('\n', '') for line in f.readlines()]
    return tmp_list

def calculate_location(instruction: str):
    '''calculate x & y value based on instruction'''
    global x
    global y
    if instruction[0] == 'L' or instruction[0] == 'R':
        rotate_waypoint(instruction)
    if instruction[0] == 'F':
        move_forward(int(instruction[1:]))
    if instruction[0] == 'N':
        move_north(int(instruction[1:]))
    if instruction[0] == 'S':
        move_south(int(instruction[1:]))
    if instruction[0] == 'E':
        move_east(int(instruction[1:]))
    if instruction[0] == 'W':
        move_west(int(instruction[1:]))
    
def rotate_clockwise(degrees):
    global wp_x
    global wp_y
    while(degrees > 0):
        # rotate by +90
        tmp_wp_x = wp_x
        wp_x = wp_y
        wp_y = -tmp_wp_x
        degrees -= 90

def rotate_anticlockwise(degrees):
    global wp_x
    global wp_y
    while(degrees > 0):
        # rotate by -90
        tmp_wp_x = wp_x
        wp_x = -wp_y
        wp_y = tmp_wp_x
        degrees -= 90

def rotate_waypoint(instruction: str):
    if instruction[0] == 'L': 
        rotate_anticlockwise(int(instruction[1:]))
    if instruction[0] == 'R': 
        rotate_clockwise(int(instruction[1:]))

def move_forward(units: int):
    global wp_x
    global wp_y
    global x 
    global y

    x += wp_x * units
    y += wp_y * units

def move_north(units: int):
    global wp_y
    wp_y += units

def move_south(units: int):
    global wp_y
    wp_y -= units

def move_east(units: int):
    global wp_x
    wp_x += units

def move_west(units: int):
    global wp_x
    wp_x -= units

# PART 1
instructions = read_in_data('data.txt')

x = 0
y = 0
direction = 90

wp_x = 10
wp_y = 1

for instruction in instructions:
    calculate_location(instruction)

print(f"Manhattan Distance: {abs(x) + abs(y)}")