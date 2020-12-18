from utils import read_input
import math

raw = read_input.read_input_strings('day18')


def evaluate_precedence(expression):
    return math.prod([sum([int(number) for number in group.split('+')]) for group in expression.split('*')])


def evaluate_sequential(expression):
    result = 0
    pointer = 0
    operator = '+'
    numbers = []
    while pointer < len(expression):
        current = expression[pointer]
        if current == '+' or current == '*':
            if operator == '+':
                result += int(''.join(numbers))
            else:
                result *= int(''.join(numbers))
            operator = current
            numbers.clear()
        else:
            numbers.append(current)
        pointer += 1
    if len(numbers) > 0:
        if operator == '+':
            result += int(''.join(numbers))
        else:
            result *= int(''.join(numbers))
    return result


def evaluate(expression, reduce):
    formatted = expression.replace(' ', '')
    if '(' in formatted:
        result = []
        pointer = 0
        while pointer < len(formatted):
            current = formatted[pointer]
            if current == '(':
                left = 1
                start = pointer + 1
                end = pointer + 1
                while end < len(formatted):
                    if formatted[end] == '(':
                        left += 1
                    if formatted[end] == ')':
                        left -= 1
                    if left == 0:
                        break
                    end += 1
                result.append(str(evaluate(formatted[start:end], reduce)))
                pointer = end + 1
            else:
                result.append(formatted[pointer])
                pointer += 1
        return evaluate(''.join(result), reduce)
    else:
        return reduce(formatted)


def part_one():
    summary = sum([evaluate(expression, evaluate_sequential) for expression in raw])
    print(f'The summary of all expressions is {summary}.')


def part_two():
    summary = sum([evaluate(expression, evaluate_precedence) for expression in raw])
    print(f'The summary of all expressions is {summary}.')


if __name__ == '__main__':
    part_one()
    part_two()
