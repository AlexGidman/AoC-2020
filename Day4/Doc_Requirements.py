"""Class objects that represent document requirements"""

import re


def get_number_from_str(string):
    """get numbers from string as single number"""

    return int(''.join(list(filter(str.isdigit, string))))


class BYR:
    def valid(self, value) -> bool:
        
        if int(value) >= 1920 and int(value) <= 2002:
            return True
        return False

    def __str__(self):
        return 'byr'


class IYR:
    def valid(self, value) -> bool:
        if int(value) >= 2010 and int(value) <= 2020:
            return True
        return False

    def __str__(self):
        return 'iyr'


class EYR:
    def valid(self, value) -> bool:
        if int(value) >= 2020 and int(value) <= 2030:
            return True
        return False

    def __str__(self):
        return 'eyr'


class HGT:
    def valid(self, value) -> bool:
        num = get_number_from_str(value)
        if value[-2:] == 'in':
            if num >= 59 and num <= 76:
                return True
        if value[-2:] == 'cm':
            if num >= 150 and num <= 193:
                return True
        return False

    def __str__(self):
        return 'hgt'


class HCL:
    def valid(self, value) -> bool:
        if re.search('^#[a-f0-9]{6,}$', value): 
            return True
        return False

    def __str__(self):
        return 'hcl'


class ECL:

    valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def valid(self, value) -> bool:
        if value in self.valid_eye_colours:
            return True
        return False

    def __str__(self):
        return 'ecl'


class PID:
    def valid(self, value) -> bool:
        if re.search('^[0-9]{9}$', value): 
            return True
        return False

    def __str__(self):
        return 'pid'
