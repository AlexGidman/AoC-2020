'''Day 7'''

import time


def read_in_data(file) -> list:
    '''Creates and returns a list of dicts representing bags'''

    tmp_list = []

    with open(file, 'r') as f:
        while(True):
            line = f.readline().replace(',', '').replace('.', '').replace('\n', '').split(' ')
            if line == ['']: # if eof, break
                break

            # tmp_dict = {}
            # tmp_dict['outer'] = f"{line[0]}{line[1]}"

            # if len(line) > 7: # Has inner bags
            #     inner_dict = {}
            #     for i in range(4, len(line), 4):
            #         inner_dict[f"{line[i+1]}{line[i+2]}"] = int(line[i])
            #     tmp_dict['inner'] = inner_dict

            if len(line) > 7:
                tmp_dict = {}
                tmp_dict['outer'] = f"{line[0]}{line[1]}"
                # Using dict comprehension instead of above code
                tmp_dict['inner'] = {f"{line[i+1]}{line[i+2]}":int(line[i]) for i in range(4, len(line), 4)}
 
            tmp_list.append(tmp_dict)

    return tmp_list


def check_bag_in_inner(bag, rules):
    tmp_list = []
    for rule in rules:
        if bag in rule['inner']:
            tmp_list.append(rule['outer'])
    return tmp_list


rules = read_in_data('data.txt')
bags = ["shinygold",]
count = 0
all_bags = []

while(True):
    tmp_bags = []

    for bag in bags:
        result = check_bag_in_inner(bag, rules)
        for item in result:
            if item not in tmp_bags and item not in all_bags:
                tmp_bags += result   
    if len(tmp_bags) > 0:
        all_bags += tmp_bags
        bags = tmp_bags
    else:
        break

test = []
for bag in all_bags:
    if bag not in test:        
        test.append(bag)

print(len(test))