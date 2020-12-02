'''Day 1'''

with open('data.txt', 'r') as f:
    puzzle_input = []

    while(True):
        line = f.readline()
        if not line:
            break
        puzzle_input.append(int(line.strip()))

    # Part 1
    # for i in range(len(puzzle_input)):
    #     for j in range(i+1, len(puzzle_input)):
    #         if i != j:
    #             if (puzzle_input[i] + puzzle_input[j]) == 2020:
    #                 print(puzzle_input[i] * puzzle_input[j])

    # Part 2
    for i in range(len(puzzle_input)):
        for j in range(i+1, len(puzzle_input)):
            for k in range(j+1, len(puzzle_input)):
                if i != j and j != k:
                    if (puzzle_input[i] + puzzle_input[j] + puzzle_input[k]) == 2020:
                        print(puzzle_input[i] * puzzle_input[j] * puzzle_input[k])