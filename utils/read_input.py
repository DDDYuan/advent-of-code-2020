def read_input_strings(file_name):
    with open(f'../inputs/{file_name}') as f:
        lines = f.read().splitlines()
        return lines


def read_input_numbers(file_name):
    lines = read_input_strings(file_name)
    return [int(n) for n in lines]
