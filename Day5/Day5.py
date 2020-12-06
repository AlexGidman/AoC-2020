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
    """Calculate row based on first 7 characters in seat_code input data"""

    MIN = 0
    MAX = 127

    for i in range(6):
        if seat_code[i] =='F':
            MAX = MAX - int((MAX - MIN - 1) / 2) -1
        elif seat_code[i] =='B':
            MIN = MIN + int((MAX - MIN + 1) / 2)
    return MIN if seat_code[6] == 'F' else MAX

def calculate_column(seat_code) -> int:
    """Calculate column based on last 3 characters in seat_code input data"""

    MIN = 0
    MAX = 7

    for i in range(7, 9):
        if seat_code[i] =='L':
            MAX = MAX - int((MAX - MIN - 1) / 2) -1
        elif seat_code[i] =='R':
            MIN = MIN + int((MAX - MIN + 1) / 2)
    return MIN if seat_code[9] == 'L' else MAX         

# HIGHEST = 0

# Generate all boarding pass seat_ids
all_boarding_cards = []
for seat_code in all_seats:
    try:
        seat_id = (calculate_row(seat_code) * 8) + calculate_column(seat_code)
        # HIGHEST = seat_id if seat_id > HIGHEST else HIGHEST
        # print(HIGHEST)
        all_boarding_cards.append(seat_id)
    except StopIteration:
        break

# Generate all possible seat ids excluding front and back rows,
# if a seat_id is not in the boarding card list, append to missing seats list
missing_seats = []
for row in range(1, 127):
    for column in range(8):
        seat_id = row * 8 + column
        # print(f"{row} : {column} >> {seat_id}")
        if seat_id not in all_boarding_cards:
            missing_seats.append(seat_id)

# if a seat_id in missing seats has got two known 'taken' seats it is printed (ie my seat!)
for seat_id in missing_seats:
    if seat_id - 1 not in missing_seats and seat_id + 1 not in missing_seats:
        print(seat_id)