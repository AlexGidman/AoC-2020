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

# Go through each group, each person, and each answer, create a list of all
# questions answered by group
for group in group_answers:
    questions_answered = []
    for person in group:
        for answer in person:
            if answer not in questions_answered:
                questions_answered.append(answer)
    # Go through each question, and check each persons answers. If it's missing
    # flag False and it won't increase count
    for question in questions_answered:
        shared_question = True
        for person in group:
            if question not in person:
                shared_question = False
                break
        sum_of_counts += shared_question

print(sum_of_counts)