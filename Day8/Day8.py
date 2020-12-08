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

def run_actions_once(code, action_to_modify=None):
    global acc
    acc = 0
    if action_to_modify:
        if code[action_to_modify][0] == 'jmp':
            code[action_to_modify][0] = 'nop'
        elif code[action_to_modify][0] == 'nop':
            code[action_to_modify][0] = 'jmp'

    i = 0
    completed_actions = []
    while(True):
        if i == len(code)-1:
            evaluate_action(code[i])
            print(f"acc: {acc}")
            completed_actions.append(i)
            break
        elif i not in completed_actions:
            completed_actions.append(i)
            i += evaluate_action(code[i])
        else:
            # print(f"acc: {acc}")
            break
    return completed_actions

# Read in data
code = read_in_data('data.txt')

# PART1
completed_actions = run_actions_once(code=code)

# PART 2
for i in range(len(code)):
    code = read_in_data('data.txt')
    completed_actions = run_actions_once(code=code, action_to_modify=i)
    if (len(code)-1) in completed_actions:
        print(f"{i} {code[i]}")



