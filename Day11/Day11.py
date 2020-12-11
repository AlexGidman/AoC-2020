'''Day 11'''
from time import sleep
from typing import List, Union

def create_map(file) -> List[list]:
    '''Create a list of lists representing points and rows on the map'''

    map_list = []

    with open(file, 'r') as f:
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

def occupancy_surrounding_seat(row, column, seating) -> bool:
    '''checks for occupancy around the seat passed in'''
    occupied_seats = 0
    width = len(seating[row])-1
    height = len(seating[column])-1

    # Check 3 above ROW1, COL0, 
    if row != 0:
        if seating[row-1][column] == '#':
            occupied_seats += 1 # oc1
        if column != 0 and seating[row-1][column-1] == '#':
            occupied_seats += 1
        if column != width and seating[row-1][column+1] == '#':
            occupied_seats += 1 # oc2
    
    # Check either side
    if column != 0 and seating[row][column-1] == '#':
        occupied_seats += 1
    if column != width and seating[row][column+1] == '#':
        occupied_seats += 1

    # Check below
    if row != height:
        if seating[row+1][column] == '#':
            occupied_seats += 1
        if column != 0 and seating[row+1][column-1] == '#':
            occupied_seats += 1
        if column != width and seating[row+1][column+1] == '#':
            occupied_seats += 1


    if occupied_seats >= 4:
        return True
    else:
        return False

def lists_are_equal(list1: Union[list, List[list]], list2: Union[list, List[list]]) -> bool:
    '''checks if list values are equal'''
    if len(list1) != len(list2):
        return False
    for row in range(len(list1)):
        for column in range(len(list1[row])):
            if list1[row][column] != list2[row][column]:
                return False
            else:
                print(list1[row])
                print(list2[row])
                sleep(2)
    return True


def stabilise_map(seating_map: List[list]) -> List[list]:
    '''returns stabilised map following seating rules'''
    current_map = [row[:] for row in seating_map]
    while True:
        # TODO: Something weird with memory going on here....
        new_map = []
        for row in range(len(current_map)):
            new_row = []
            for column in range(len(current_map[row])):
                if current_map[row][column] == '.':
                    new_row.append('.')
                elif occupancy_surrounding_seat(row, column, current_map):
                    new_row.append('L')
                else:
                    new_row.append('#')
            new_map.append(new_row)

        if lists_are_equal(current_map, new_map):
            return new_map
        else:
            current_map = [line[:] for line in new_map]
            # print(current_map)
            # print('\n\n')
            # sleep(1)


def count_occupied_seats(seating_map: List[list]):
    '''counts number of occupied seats and prints value'''
    count = 0
    for row in seating_map:
        for i in range(len(row)):
            if row[i] == '#':
                count += 1
    print(count)


# PART 1
seating_map = create_map('test_data.txt')
stabilised_map1 = stabilise_map(seating_map)
# stabilised_map2 = stabilise_map(stabilised_map1)

# print(stabilised_map1[1])
# print(stabilised_map2[1])


# count_occupied_seats(stabilised_map1)
# count_occupied_seats(stabilised_map2)