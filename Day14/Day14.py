'''Day 14'''

import re

# PART 1
def convert_to_binary(integer: int) -> str:
    return bin(integer).replace('0b', '').replace('\n', '')

def convert_to_decimal(binary: str) -> int:
    return int(binary, 2)

def new_mask(line: str) -> bool:
    global mask
    if "mask" in line:
        mask = line[7:].replace('\n', '')
        return True
    return False

def mask_binary(mask: str, binary: str) -> str:
    tmp_binary = ((len(mask)-len(binary))*'0') + binary
    masked_binary = ''
    for i in range(len(mask)):
        masked_binary += mask[i] if mask[i] != 'X' else tmp_binary[i]
    return masked_binary

def assign_mem_value(line: str):
    global mem
    global mask
    nums = re.findall('\d+', line)
    binary_value = convert_to_binary(int(nums[1]))
    masked_binary_value = mask_binary(mask, binary_value)
    mem[int(nums[0])] = convert_to_decimal(masked_binary_value)


# initialise mem dict & mask value
mem = {}
mask = ''
total = 0

with open('data.txt', 'r') as f:
    for line in f.readlines():
        if new_mask(line):
            continue
        else:
            assign_mem_value(line)


for key in mem:
    total += mem[key]
print(total)