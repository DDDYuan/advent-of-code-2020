from utils import read_input
import time


raw = read_input.read_input_strings('day23')


class CupsCircle:
    def __init__(self, labels, total=None):
        self.__labels = [int(label) for label in labels]
        if total is not None:
            others = list(range(max(self.__labels) + 1, total + 1))
            self.__labels += others

    def get_result(self):
        index = 0
        while index < len(self.__labels):
            if self.__labels[index] == 1:
                break
            else:
                index += 1
        return ''.join(str(number) for number in self.__labels[index + 1:] + self.__labels[:index])

    def move(self, rounds):
        while rounds > 0:
            current = self.__labels[0]
            removed = self.__labels[1:4]
            others = self.__labels[4:]
            target = current - 1
            while target not in others:
                target -= 1
                if target < min(others):
                    target = max(others)
            index = 0
            while index < len(others):
                if others[index] == target:
                    break
                else:
                    index += 1
            self.__labels = others[:index + 1] + removed + others[index + 1:] + [current]
            rounds -= 1


def part_one():
    circle = CupsCircle(raw[0])
    circle.move(100)
    print(circle.get_result())


def part_two():
    circle = CupsCircle(raw[0], 1000000)
    circle.move(10000000)
    print(circle.get_result())


if __name__ == '__main__':
    t0 = time.time()
    part_one()
    part_two()
    print(f"Total time: {round(time.time() - t0, 2)} seconds")
