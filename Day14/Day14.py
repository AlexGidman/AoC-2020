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

print(f"Part 1 Solution: {total}")


######

# PART 2

# Apply mask to memory address
# Generate all possible binaries for memory addresses
# convert to decimal, and store the value in every memory address
# sum all values stored in mem

def mask_binary_v2(mask: str, binary: str) -> str:
    tmp_binary = ((len(mask)-len(binary))*'0') + binary
    masked_binary = ''
    for i in range(len(mask)):
        if mask[i] != '0':
            masked_binary += mask[i] 
        else:
            masked_binary += tmp_binary[i]
    return masked_binary

def generate_all_variants(binary: str) -> list:
    '''return list of mem addresses as ints'''
    floating_bits = binary.count("X")
    addresses = []
    variants = []

    for i in range(2**floating_bits):
        variants.append( list(bin(i)[2:].zfill(floating_bits)))

    for variant in variants:
        i = 0
        address = ""
        for char in binary:
            if char == "X":
                address += str(variant[i])
                i += 1
            else:
                address += str(char)
        addresses.append(convert_to_decimal(address))
    return addresses

def assign_mem_values_v2(addresses: list, value: int):
    global mem2
    for ad in addresses:
        mem2[ad] = value
    


mem2 = {}
mask = ''
total = 0

with open('data.txt', 'r') as f:
    for line in f.readlines():
        if new_mask(line):
            continue
        else:
            nums = re.findall('\d+', line)
            value = int(nums[1])
            binary = convert_to_binary(int(nums[0]))
            masked_binary = mask_binary_v2(mask, binary)
            addresses = generate_all_variants(masked_binary)
            assign_mem_values_v2(addresses, value)

for key in mem2:
    total += mem2[key]

print(f"Part 2 Solution: {total}")