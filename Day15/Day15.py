'''Day 15'''

# PART 1 & 2

def read_in_data(file) -> list:
    with open(file, 'r') as f:
        return f.readline().replace('\n', '').split(',')

def return_turn(turn_to_return: int, turns: list) -> int:
    '''Returns the number said on turn_to_return'''
    for i in range(len(turns), turn_to_return):
        count = 0
        for j in range(len(turns)-2, -1, -1):
            if int(turns[i-1]) == int(turns[j]):
                count +=(i-1)-(j)
                break
        turns.append(count)
    return turns[-1]

turns = read_in_data('data.txt')

solution = return_turn(2020, turns)
print(f"Part 1 Solution: {solution}")
solution = return_turn(30000000, turns)
print(f"Part 2 Solution: {solution}")