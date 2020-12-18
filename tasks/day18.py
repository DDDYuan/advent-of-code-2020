from utils import read_input

raw = read_input.read_input_strings('day18')


class Expression:
    def __init__(self, operator, operand):
        self.__operator = operator
        self.__is_group = isinstance(operand[0], Expression)
        if self.__is_group:
            self.__operand = operand
        else:
            self.__operand = int(''.join(operand))

    def is_addition(self):
        return self.__operator == '+'

    def get_operand(self):
        if self.__is_group:
            return self.__operand
        else:
            return [str(self.__operand)]

    def operate(self, number):
        if self.__is_group:
            group_value = 0
            for expression in self.__operand:
                group_value = expression.operate(group_value)
            if self.is_addition():
                return number + group_value
            else:
                return number * group_value
        else:
            if self.is_addition():
                return number + self.__operand
            else:
                return number * self.__operand

    def operate_precedence(self, number):
        if self.__is_group:
            expressions = []
            group = []
            for expression in self.__operand:
                if expression.is_addition():
                    group.append(expression)
                else:
                    expressions.append(group)
                    group.clear()
                    group.append(Expression('+', expression.get_operand()))
            if len(group) > 0:
                expressions.append(group)
            if len(expressions) == 1:
                return expressions[0].operate(0)
            for i in range(len(expressions)):
                if i == 0:
                    expressions[i] = Expression('+', expressions[i])
                else:
                    expressions[i] = Expression('*', expressions[i])
            return Expression('+', expressions).operate_precedence(0)

        else:
            if self.is_addition():
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
                expression.append(Expression(current_operator, collected))
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
            expression.append(Expression(current_operator, parse_expression(formatted[start:end])))
            pointer = end + 1
    if len(collected) > 0:
        expression.append(Expression(current_operator, collected))
    return expression


def parse_expressions(raw_expressions):
    return [Expression('+', parse_expression(raw_expression)) for raw_expression in raw_expressions]


def part_one():
    summary = sum([expression.operate(0) for expression in parse_expressions(raw)])
    print(f'The summary of all expressions is {summary}.')


def part_two():
    summary = sum([expression.operate_precedence(0) for expression in parse_expressions(raw)])
    print(f'The summary of all expressions is {summary}.')


if __name__ == '__main__':
    part_one()
    part_two()
