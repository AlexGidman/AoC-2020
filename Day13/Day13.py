'''Day 13'''
from time import sleep

# Part 1
# def get_timestamp(file) -> int:
#     '''Return timestamp from bus schedule puzzle input'''
#     tmp_list =[]
#     with open(file, 'r') as f:
#         return int(f.readline().replace('\n', ''))

# def get_bus_ids(file) -> list:
#     '''Create a list of lists representing points and rows on the map'''
#     with open(file, 'r') as f:
#         f.readline()
#         values = f.readline().replace('\n', '').split(',')
#         tmp_list = [int(item) for item in values if item != 'x']
#         return tmp_list

# timestamp = get_timestamp('data.txt')
# bus_ids = get_bus_ids('data.txt')
# min_leave_time = None

# for bus_id in bus_ids:
#     difference = timestamp % bus_id
#     earliest = (timestamp + bus_id - difference)
#     min_leave_time = earliest if not min_leave_time or earliest < min_leave_time else min_leave_time
#     print(f'Bus: {bus_id}, Earliest: {earliest}, Time to wait: {difference}')
#     print((earliest-timestamp)*bus_id)

# Part 2
# This takes a while to calculate and needs optimising

def get_bus_ids(file) -> list:
    '''Create a list of lists representing points and rows on the map'''
    with open(file, 'r') as f:
        f.readline()
        return f.readline().replace('\n', '').split(',')

def is_start_of_sequence(i, bus_ids, offsets):
    # Check each offset results in modulo zero
    for j in range(1, len(bus_ids)):
        if (i + offsets[j]) % bus_ids[j] != 0:
            return False
    return True

input_data = get_bus_ids('data.txt')
bus_ids = [int(bus_id) for bus_id in input_data if bus_id != 'x']
offsets = [input_data.index(str(bus_id)) for bus_id in bus_ids]

i = 100000000000000
while(True):
    if is_start_of_sequence(i, bus_ids, offsets):
        print(i)
        break
    i += bus_ids[0]