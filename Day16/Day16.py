'''Day 16'''

# PART 1

# import re

# def read_in_data(file) -> list:
#     with open(file, 'r') as f:
#         return [line.replace('\n', '') for line in f.readlines()]

# def valid(num: int) -> bool:
#     global rules
#     for rule in rules:
#         num_range = re.findall('\d+', rule)
#         min1 = int(num_range[0])
#         max1 = int(num_range[1])
#         min2 = int(num_range[2])
#         max2 = int(num_range[3])
#         if num >= min1 and num <= max1:
#             return True
#         if num >= min2 and num <= max2:
#             return True
#     return False

# data = read_in_data('data.txt')

# # Rules
# rules = []
# end = 0
# for i in range(len(data)):
#     if data[i] == '':
#         end = i
#         break
#     rules.append(data[i])

# end += 2

# # My Ticket
# my_ticket = data[end].split(',')

# end += 3

# # Tickets
# tickets = [data[i].split(',') for i in range(end, len(data))]

# invalid_numbers = []
# for ticket in tickets:
#     for num in ticket:
#         if not valid(int(num)):
#             invalid_numbers.append(int(num))
    
# print(sum(invalid_numbers))

# PART 2

import re

def read_in_data(file) -> list:
    with open(file, 'r') as f:
        return [line.replace('\n', '') for line in f.readlines()]

def valid(num: int) -> bool:
    global rules
    for rule in rules:
        num_range = re.findall('\d+', rule)
        min1 = int(num_range[0])
        max1 = int(num_range[1])
        min2 = int(num_range[2])
        max2 = int(num_range[3])
        if num >= min1 and num <= max1:
            return True
        if num >= min2 and num <= max2:
            return True
    return False

def valid_for_rule(rule: str, num: int) -> bool:
    '''Checks if number is valid for rule'''
    num_range = re.findall('\d+', rule)
    min1 = int(num_range[0])
    max1 = int(num_range[1])
    min2 = int(num_range[2])
    max2 = int(num_range[3])  
    if num >= min1 and num <= max1:
        return True
    elif num >= min2 and num <= max2:
        return True
    return False

        
# Read in data
data = read_in_data('data.txt')

# Rules
rules = []
end = 0
for i in range(len(data)):
    if data[i] == '':
        end = i
        break
    rules.append(data[i])

end += 2

# My Ticket
my_ticket = data[end].split(',')

end += 3

# Tickets
tickets = [data[i].split(',') for i in range(end, len(data))]

valid_tickets = []

for ticket in tickets:
    tmp_ticket = []
    for num in ticket:
        if valid(int(num)):
            tmp_ticket.append(num)
    if len(tmp_ticket) == len(ticket):
        valid_tickets.append(tmp_ticket)

# go through each rule, check all numbers in position 0 and see if the rule matches. 
# if not, move to all numbers in position 1 etc