'''Day 10'''

from functools import wraps

def read_in_data(file) -> list:
    '''Creates and returns a sorted list of numbers '''

    tmp_list = [0,] # joltage outlet of 0

    with open(file, 'r') as f:
        while(True):
            line = f.readline().replace('\n', '')
            if not line: # if eof, break
                break
            tmp_list.append(int(line))

    return sorted(tmp_list)

def count(input):
    global one_jolt
    global three_jolt
    if input == 3:
        three_jolt += 1
    else:
        one_jolt += 1

# Part 1
adapters = read_in_data('data.txt')
adapters += [adapters[-1] + 3] # accounting for the three jolt jump at the end

one_jolt = 0
three_jolt = 0 
for i in range(1, len(adapters)):
    count(adapters[i] - adapters[i-1])

print(one_jolt * three_jolt)