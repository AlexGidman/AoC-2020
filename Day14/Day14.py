'''Day 14'''

# Part 1
def convert_to_binary(integer):
    return bin(integer).replace('0b', '').replace('\n', '')

def convert_to_decimal(binary):
    return int(binary, 2)

def mask_binary(mask, binary):
    tmp_binary = ((len(mask)-len(binary))*'0') + binary
    masked_binary = ''
    for i in range(len(mask)):
        masked_binary += mask[i] if mask[i] != 'X' else tmp_binary[i]
    return masked_binary

# initialise mem dict
mem = {}
# read in mask value
mask = ""
# read in mem value, run through: convert_to_decimal(mask_binary(convert_to_binary(mem_value)))


