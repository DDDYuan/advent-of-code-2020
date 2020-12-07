import os


def read_input_strings(file_name):
    with open(f'{os.getcwd()}/inputs/{file_name}') as f:
        lines = f.read().splitlines()
        return lines


def read_input_numbers(file_name):
    lines = read_input_strings(file_name)
    return [int(n) for n in lines]


def read_input_strings_groups(file_name):
    lines = read_input_strings(file_name)
    result = []
    current = []
    for line in lines:
        if line == '':
            if len(current) > 0:
                result.append(current)
                current = []
        else:
            current.append(line)
    if len(current) > 0:
        result.append(current)
    return result
