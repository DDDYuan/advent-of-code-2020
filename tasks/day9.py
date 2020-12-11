from utils import read_input


raw = read_input.read_input_numbers('day9')


def is_valid(array, target):
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[i] + array[j] == target:
                return True
    return False


def find_first_invalid():
    for i in range(len(raw) - 25):
        if not is_valid(raw[i:i+25], raw[i+25]):
            return raw[i+25], i+25


def part_one():
    number, index = find_first_invalid()
    print(f'Invalid number is {number} at {index}.')


def part_two():
    number, index = find_first_invalid()
    start = 0
    end = 1
    while end <= len(raw):
        summary = sum(raw[start:end])
        if summary == number:
            result = max(raw[start:end]) + min(raw[start:end])
            print(f'The final result is {result}.')
            return result
        elif summary < number:
            end += 1
        else:
            start += 1


if __name__ == '__main__':
    part_one()
    part_two()
