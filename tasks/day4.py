from utils import read_input, regex


raw = read_input.read_input_strings_groups('day4')


def parse_passport(lines):
    passport = {}
    for line in lines:
        items = line.split(' ')
        for item in items:
            [key, value] = item.split(':')
            passport[key] = value
    return passport


def get_passports():
    return [parse_passport(item) for item in raw]


def passport_valid(passport):
    fields = set([field for field in passport])
    return fields >= {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def is_valid_height(height):
    if 'cm' in height:
        numbers = height.split('cm')
        return 150 <= int(numbers[0]) <= 193
    if 'in' in height:
        numbers = height.split('in')
        return 59 <= int(numbers[0]) <= 76
    return False


def passport_present_valid(passport):
    if passport_valid(passport):
        return 1920 <= int(passport['byr']) <= 2002 and \
               2010 <= int(passport['iyr']) <= 2020 <= int(passport['eyr']) <= 2030 and \
               is_valid_height(passport['hgt']) and \
               regex.match_regex(passport['hcl'], r'#[0-9a-f]{6}') and \
               regex.match_regex(passport['ecl'], r'(amb|blu|brn|gry|grn|hzl|oth)') and \
               regex.match_regex(passport['pid'], r'[0-9]{9}')


def part_one():
    valid = len([passport for passport in get_passports() if passport_valid(passport)])
    print(f'Valid passport number is {valid}')


def part_two():
    valid = len([passport for passport in get_passports() if passport_present_valid(passport)])
    print(f'Valid passport number is {valid}')


if __name__ == '__main__':
    part_one()
    part_two()
