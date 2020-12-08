'''Day 8'''

def read_in_data(file) -> list:
    '''Creates and returns a list of dicts representing instructions'''

    tmp_list = []

    with open(file, 'r') as f:
        while(True):
            line = f.readline().replace('\n', '').split(' ')
            if line == ['']: # if eof, break
                break
            
            tmp_list_item = [line[0], int(line[1])]

            tmp_list.append(tmp_list_item)

    return tmp_list

acc = 0

def evaluate_action(action: list):
    if action[0] == 'nop':
        return 1
    if action[0] == 'acc':
        global acc 
        acc += action[1]
        return 1
    if action[0] == 'jmp':
        return action[1]


code = read_in_data('data.txt')

# PART1
i = 0
completed_actions = []
while(i < len(code)):
    if i not in completed_actions:
        completed_actions.append(i)
        i += evaluate_action(code[i])
    else:
        print(acc)
        break



    