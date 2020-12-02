from utils import read_input

raw_inputs = read_input.read_input_strings('day2')


def parse_password(raw):
    [rule, password] = raw.split(': ')
    [policy, char] = rule.split(' ')
    [low, high] = policy.split('-')
    return int(low), int(high), char, password


def is_password_valid(policy):
    low, high, char, password = policy
    count = len([c for c in password if c == char])
    return low <= count <= high


def is_password_valid_new(policy):
    pos1, pos2, char, password = policy
    return (password[pos1 - 1] == char and password[pos2 - 1] != char) or\
           (password[pos1 - 1] != char and password[pos2 - 1] == char)


def part_one():
    result = len([p for p in raw_inputs if is_password_valid(parse_password(p))])
    print(f'{result} passwords are valid.')


def part_two():
    result = len([p for p in raw_inputs if is_password_valid_new(parse_password(p))])
    print(f'{result} passwords are valid.')


if __name__ == '__main__':
    part_one()
    part_two()
