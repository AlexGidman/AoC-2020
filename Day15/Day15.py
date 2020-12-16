'''Day 15'''

# PART 1

def read_in_data(file) -> list:
    with open(file, 'r') as f:
        return f.readline().replace('\n', '').split(',')

turns = read_in_data('data.txt')

for i in range(len(turns), 2020):
    count = 0
    for j in range(len(turns)-2, -1, -1):
        if int(turns[i-1]) == int(turns[j]):
            count +=(i-1)-(j)
            break
    turns.append(count)

print(turns[-1])
