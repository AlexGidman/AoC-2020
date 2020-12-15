'''Day 15'''

# PART 1
def read_in_data(file) -> list:
    with open(file, 'r') as f:
        return f.readline().replace('\n', '').split(',')

def next_number():
    pass

turns = read_in_data('data.txt')

for i in range(len(turns), 2020):
    pass
print(turns)
# {number: turn}