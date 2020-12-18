from utils import read_input

raw = read_input.read_input_strings('day18')


class Element:
    def __init__(self, operator, operand):
        self.__operator = operator
        self.__is_group = isinstance(operand[0], Element)
        if self.__is_group:
            self.__operand = operand
        else:
            self.__operand = int(''.join(operand))

    def __str__(self):
        return f'{self.__operator} {self.__operand}'

    def operate(self, number):
        if self.__is_group:
            group_value = 0
            for element in self.__operand:
                group_value = element.operate(group_value)
            if self.__operator == '+':
                return number + group_value
            else:
                return number * group_value
        else:
            if self.__operator == '+':
                return number + self.__operand
            else:
                return number * self.__operand


def parse_expression(raw_expression):
    formatted = raw_expression.replace(' ', '')
    current_operator = '+'
    pointer = 0
    collected = []
    expression = []
    while pointer < len(formatted):
        if formatted[pointer] == '+' or formatted[pointer] == '*':
            if len(collected) > 0:
                expression.append(Element(current_operator, collected))
            current_operator = formatted[pointer]
            collected.clear()
            pointer += 1
        elif formatted[pointer] != '(':
            collected.append(formatted[pointer])
            pointer += 1
        else:
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
            expression.append(Element(current_operator, parse_expression(formatted[start:end])))
            pointer = end + 1
    if len(collected) > 0:
        expression.append(Element(current_operator, collected))
    return expression


def evaluate_expression(expression):
    current = 0
    for element in expression:
        current = element.operate(current)
    return current


def part_one():
    expressions = [parse_expression(raw_expression) for raw_expression in raw]
    summary = sum([evaluate_expression(expression) for expression in expressions])
    print(f'The summary of all expressions is {summary}.')


def part_two():
    pass


if __name__ == '__main__':
    part_one()
    part_two()
