from utils import read_input
import math

raw = read_input.read_input_numbers('day10')


def increase_one(dictionary, key):
    if dictionary.get(key) is None:
        dictionary[key] = 1
    else:
        dictionary[key] += 1


def part_one():
    chain = [0] + sorted(raw) + [max(raw) + 3]
    result = dict()
    for i in range(1, len(chain)):
        increase_one(result, chain[i] - chain[i - 1])
    print(f'The 1 times 3 result is {result[1] * result[3]}')


def calculate_continuous_steps(number):
    count = number
    result = 0
    current = 1
    pre = 0
    pre_pre = 0
    if count == 0:
        return 0
    if count == 1:
        return 1
    while count > 1:
        result = current + pre + pre_pre
        pre_pre = pre
        pre = current
        current = result
        count -= 1
    return result


def calculate_total_steps(chain):
    group = []
    current = [chain[0]]
    for i in range(1, len(chain)):
        if chain[i] - chain[i - 1] == 1:
            current.append(chain[i])
        else:
            group.append(current)
            current = [chain[i]]
    if len(current) > 0:
        group.append(current)
    steps_group = [calculate_continuous_steps(len(continuous)) for continuous in group]
    return math.prod(steps_group)


def part_two():
    chain = [0] + sorted(raw) + [max(raw) + 3]
    steps = calculate_total_steps(chain)
    print(f'The total possible steps number is {steps}.')


if __name__ == '__main__':
    part_one()
    part_two()
