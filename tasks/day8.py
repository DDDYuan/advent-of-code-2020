from utils import read_input


raw = read_input.read_input_strings('day8')


def run_program(lines):
    acc = 0
    current = 0
    reached = []
    while current not in reached:
        if current >= len(lines):
            return True, acc
        reached.append(current)
        [command, number] = lines[current].split(' ')
        if command == 'acc':
            acc += int(number)
            current += 1
        if command == 'jmp':
            current += int(number)
        if command == 'nop':
            current += 1
    return False, acc


def part_one():
    success, acc = run_program(raw)
    print(f'The final acc is {acc}, success? {success}')


def part_two():
    indices = [i for i in range(len(raw)) if raw[i].startswith('nop') or raw[i].startswith('jmp')]
    for i in indices:
        new = raw.copy()
        if new[i].startswith('nop'):
            new[i] = new[i].replace('nop', 'jmp')
        else:
            new[i] = new[i].replace('jmp', 'nop')
        success, acc = run_program(new)
        if success:
            print(f'The result is {acc}.')


if __name__ == '__main__':
    part_one()
    part_two()
