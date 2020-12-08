from utils import read_input
from utils import assembly_interpreter

raw = read_input.read_input_strings('day8')
interpreter = assembly_interpreter.Interpreter(raw)


def part_one():
    success, acc = interpreter.run_program()
    print(f'The final acc is {acc}, Infinite loop? {not success}')


def part_two():
    indices = [i for i in range(len(raw)) if raw[i].startswith('nop') or raw[i].startswith('jmp')]
    for i in indices:
        new = raw.copy()
        if new[i].startswith('nop'):
            new[i] = new[i].replace('nop', 'jmp')
        else:
            new[i] = new[i].replace('jmp', 'nop')
        interpreter.reinit(new)
        success, acc = interpreter.run_program()
        if success:
            print(f'The result is {acc}.')


if __name__ == '__main__':
    part_one()
    part_two()
