'''Day 1'''

with open('data.txt', 'r') as f:
    puzzle_input = []

    while(True):
        line = f.readline()
        if not line:
            break
        puzzle_input.append(int(line.strip()))

    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input)):
            if i != j:
                if (puzzle_input[i] + puzzle_input[j]) == 2020:
                    print(puzzle_input[i] * puzzle_input[j])
