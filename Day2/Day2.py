'''Day 2'''

with open('data.txt', 'r') as f:
    puzzle_input = []
    valid_password_count = 0

    while(True):
        line = f.readline().split(' ')
        if line == ['']:
            break
        puzzle_input.append(
            {
                'min': int(line[0].split('-')[0]),
                'max': int(line[0].split('-')[1]),
                'char': line[1][:1],
                'password': line[2].replace('\n', '')
            }
        )

    for entry in puzzle_input:
        counter = 0

        # Part 1
        # for char in entry['password']:
        #     if char == entry['char']:
        #         counter += 1
        # if counter >= entry['min'] and counter <= entry['max']:
        #     valid_password_count += 1

        # Part 2
        try:
            pos1 = entry['password'][entry['min']]
        except:
            pos1 = None
        try:
            pos2 = entry['password'][entry['max']]
        except:
            pos2 = None

        if entry['char'] == pos1 and entry['char'] != pos2:
            valid_password_count += 1

        if entry['char'] == pos2 and entry['char'] != pos1:
            valid_password_count += 1

            
    print(valid_password_count)