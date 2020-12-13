'''Day 13'''
from time import sleep

# Part 1
def get_timestamp(file) -> int:
    '''Return timestamp from bus schedule puzzle input'''
    tmp_list =[]
    with open(file, 'r') as f:
        return int(f.readline().replace('\n', ''))

def get_bus_ids(file) -> list:
    '''Create a list of lists representing points and rows on the map'''
    with open(file, 'r') as f:
        f.readline()
        values = f.readline().replace('\n', '').split(',')
        tmp_list = [int(item) for item in values if item != 'x']
        return tmp_list

timestamp = get_timestamp('data.txt')
bus_ids = get_bus_ids('data.txt')
min_leave_time = None

for bus_id in bus_ids:
    difference = timestamp % bus_id
    earliest = (timestamp + bus_id - difference)
    min_leave_time = earliest if not min_leave_time or earliest < min_leave_time else min_leave_time
    print(f'Bus: {bus_id}, Earliest: {earliest}, Time to wait: {difference}')
    print((earliest-timestamp)*bus_id)
