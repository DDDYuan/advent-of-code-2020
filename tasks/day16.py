from utils import read_input
import math

raw = read_input.read_input_strings_groups('day16')


def parse_rules(raw_rules):
    result = []
    for raw_rule in raw_rules:
        values = raw_rule.split(': ')[1].split(' or ')
        ranges = []
        for value in values:
            [min_value, max_value] = value.split('-')
            ranges.append((int(min_value), int(max_value)))
        result.append(ranges)
    return result


def parse_tickets(raw_tickets):
    return [[int(number) for number in raw_ticket.split(',')] for raw_ticket in raw_tickets]


def is_number_valid(number, rule):
    for (down, up) in rule:
        if down <= number <= up:
            return True
    return False


def find_invalid_numbers(ticket, rules):
    result = []
    for i in range(len(ticket)):
        number = ticket[i]
        is_valid = False
        for rule in rules:
            if is_number_valid(number, rule):
                is_valid = True
                break
        if not is_valid:
            result.append(number)
    return result


def part_one():
    rules = parse_rules(raw[0])
    tickets = parse_tickets(raw[2][1:])
    invalid_numbers = []
    for ticket in tickets:
        invalid_numbers += find_invalid_numbers(ticket, rules)
    print(f'The sum of invalid numbers is {sum(invalid_numbers)}.')


def part_two():
    rules = parse_rules(raw[0])
    my_ticket = parse_tickets(raw[1][1:])[0]
    tickets = parse_tickets(raw[2][1:])
    valid_tickets = [ticket for ticket in tickets if len(find_invalid_numbers(ticket, rules)) == 0]
    # Find all valid columns to each rule
    rule_valid_columns = dict()
    for r_i in range(len(rules)):
        rule = rules[r_i]
        for i in range(len(valid_tickets[0])):
            numbers = [ticket[i] for ticket in valid_tickets]
            all_valid = True
            for number in numbers:
                if not is_number_valid(number, rule):
                    all_valid = False
                    break
            if all_valid:
                if r_i in rule_valid_columns:
                    rule_valid_columns[r_i].add(i)
                else:
                    rule_valid_columns[r_i] = {i}
    # Reduce valid columns to a one-one mapping
    confirmed_rules = set()
    while len(rules) != len(confirmed_rules):
        for key in rule_valid_columns:
            if len(rule_valid_columns[key]) == 1 and key not in confirmed_rules:
                current_key = key
                removal_column = rule_valid_columns[key].copy().pop()
                confirmed_rules.add(key)
        for key in rule_valid_columns:
            if key != current_key and removal_column in rule_valid_columns[key]:
                rule_valid_columns[key].remove(removal_column)

    departures = [my_ticket[rule_valid_columns[rule].pop()] for rule in range(6)]
    print(f'The six departures multiplies to be {math.prod(departures)}.')


if __name__ == '__main__':
    part_one()
    part_two()
