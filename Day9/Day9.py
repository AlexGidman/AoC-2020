'''Day 9'''

def read_in_data(file) -> list:
    '''Creates and returns a list of dicts representing instructions'''

    tmp_list = []

    with open(file, 'r') as f:
        while(True):
            line = f.readline().replace('\n', '')
            if not line: # if eof, break
                break
            tmp_list.append(int(line))

    return tmp_list


def check_for_sum(result, data) -> bool:
    '''Checks if two numbers in data sum together to make result'''
    for number1 in data:
        for number2 in data:
            if number1 + number2 == result and number1 != number2:
                return True
    return False

def check_for_no_summed_numbers(read_in, data) -> int:
    '''checks for result that doesn't have two numbers that sum together based on read_in size'''
    for i in range(read_in, len(data)):
        tmp_data = data[i-read_in:i]
        result = data[i]
        if not check_for_sum(result, tmp_data):
            return result


def check_for_contiguous(invalid_number, data) -> list:
    '''check for contiguous numbers that sum to invalid number, and return as a list'''
    for i in range(len(data)):
        sum = 0
        tmp_list = []
        for j in range(i, len(data)):
            if sum < invalid_number:
                sum += data[j]
                tmp_list.append(data[j])
            elif sum == invalid_number:
                return tmp_list
            else:
                break

def add_smallest_and_largest(data: list) -> int:
    sorted_list = sorted(data)
    return sorted_list[0] + sorted_list[-1]


data = read_in_data('data.txt')

invalid_number = check_for_no_summed_numbers(25, data)

#Part 1
print(invalid_number)

cont_list = check_for_contiguous(invalid_number, data)

#Part 2
print(add_smallest_and_largest(cont_list))
