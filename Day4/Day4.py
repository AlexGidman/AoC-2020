'''Day 4'''

from pprint import pprint

from Doc_Requirements import BYR, IYR, EYR, HGT, HCL, ECL, PID

def read_in_data(file) -> list:
    '''Creates and returns a list of dicts representing passports'''

    tmp_list = []

    with open(file, 'r') as f:
        document = {}
        while(True):
            line = f.readline().split(' ')
            if line == ['\n'] or line == ['']: # if blank line or eof, append dict and reset value
                tmp_list.append(document)
                document = {}
            else: # else add all elements to the dict
                for item in line:
                    tmp_item = item.split(':')
                    document[tmp_item[0]] = tmp_item[1].replace('\n', '')
            if line == ['']: # if eof, break
                break

    return tmp_list

def count_valid_docs(data: list, criteria: tuple) -> int:
    """Checks each doc against criteria, returns number of valid docs"""

    number_of_valid_docs = 0
    
    for doc in data:
        valid_doc = True
        for option in criteria:
            if option.__str__() not in doc:
                valid_doc = False
                break
            if not option.valid(doc[option.__str__()]):
                valid_doc = False
                break

        number_of_valid_docs += int(valid_doc)
    
    return number_of_valid_docs


byr = BYR()
iyr = IYR()
eyr = EYR()
hgt = HGT()
hcl = HCL()
ecl = ECL()
pid = PID()

CRITERIA = (byr, iyr, eyr, hgt, hcl, ecl, pid)

data = read_in_data('data.txt')

# print(len(data))
print(count_valid_docs(data, CRITERIA))
