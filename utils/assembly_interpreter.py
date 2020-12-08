class Interpreter:

    def __init__(self, codes):
        self.__codes = codes
        self.__codes_length = len(codes)
        self.__acc = 0
        self.__line_number = 0
        self.__reached = set()

    def __parse_command(self, line_number):
        [operator, operand] = self.__codes[line_number].split(' ')
        return operator, int(operand)

    def __operate(self, operator, operand):
        if operator == 'acc':
            self.__acc += operand
            self.__line_number += 1
        elif operator == 'jmp':
            self.__line_number += operand
        elif operator == 'nop':
            self.__line_number += 1
        else:
            raise ValueError(f'Invalid operator {operator}')

    def reset(self):
        self.__acc = 0
        self.__line_number = 0
        self.__reached = set()

    def reinit(self, codes):
        self.__codes = codes
        self.__codes_length = len(codes)
        self.reset()

    def run_program(self):
        while self.__line_number not in self.__reached:
            if self.__line_number >= self.__codes_length:
                return True, self.__acc
            self.__reached.add(self.__line_number)
            operator, operand = self.__parse_command(self.__line_number)
            self.__operate(operator, operand)
        return False, self.__acc
