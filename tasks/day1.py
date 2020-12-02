from utils import read_input


expenses = read_input.read_input_numbers('day1')


def part_one():
    for i in range(len(expenses)):
        for j in range(len(expenses) - i - 1):
            if expenses[i] + expenses[j+i] == 2020:
                print(f'{expenses[i]} + {expenses[j+i]} = 2020, result is {expenses[i] * expenses[j+i]}')


def part_two():
    for i in range(len(expenses)):
        for j in range(len(expenses) - i - 1):
            for k in range(len(expenses) - i - j - 1):
                if expenses[i] + expenses[j+i] + expenses[k+j+i] == 2020:
                    print(f'{expenses[i]} + {expenses[j+i]} + {expenses[k+j+i]} = 2020,'
                          f' result is {expenses[i] * expenses[j+i] * expenses[k+j+i]}')


if __name__ == '__main__':
    part_one()
    part_two()
