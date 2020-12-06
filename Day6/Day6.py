'''Day 6'''

def read_in_data(file) -> list:
    '''Creates and returns a list of lists representing groups and there answers'''

    tmp_list = []
    group = []

    with open(file, 'r') as f:
        while(True):
            line = f.readline()
            if line == '\n':
                tmp_list.append(group)
                group = []
            elif not line: # if eof, break
                tmp_list.append(group)
                break
            else:
                group.append(line.replace('\n', ''))

    return tmp_list


group_answers = read_in_data('data.txt')

sum_of_counts = 0

# Go through each group, each person, and each answer, and count for each group 
# how many of the questions were answered yes, and sum together.
for group in group_answers:
    questions_answered = []
    for person in group:
        for answer in person:
            if answer not in questions_answered:
                questions_answered.append(answer)
                sum_of_counts += 1

print(sum_of_counts)
