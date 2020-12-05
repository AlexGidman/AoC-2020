'''Day 5'''

def read_input_data(file) -> list:
    """Create a list of seat_codes"""

    with open(file, 'r') as f:
        all_seats = []
        while(True):
            line = f.readline()
            if not line:
                return all_seats
            all_seats.append(line.replace('\n', ''))


all_seats = read_input_data('data.txt')

def calculate_row(seat_code) -> int:
    MIN = 0
    MAX = 127

    for i in range(6):
        if seat_code[i] =='F':
            MAX = MAX - int((MAX - MIN - 1) / 2) -1
        elif seat_code[i] =='B':
            MIN = MIN + int((MAX - MIN + 1) / 2)
    return MIN if seat_code[6] == 'F' else MAX

def calculate_column(seat_code) -> int:
    MIN = 0
    MAX = 7

    for i in range(7, 9):
        if seat_code[i] =='L':
            MAX = MAX - int((MAX - MIN - 1) / 2) -1
        elif seat_code[i] =='R':
            MIN = MIN + int((MAX - MIN + 1) / 2)
    return MIN if seat_code[9] == 'L' else MAX         

HIGHEST = 0

for seat_code in all_seats:
    try:
        seat_id = (calculate_row(seat_code) * 8) + calculate_column(seat_code)
        HIGHEST = seat_id if seat_id > HIGHEST else HIGHEST
        print(HIGHEST)
    except StopIteration:
        break
