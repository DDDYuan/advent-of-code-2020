from utils import read_input, regex


raw_rules = read_input.read_input_strings('day7')


def parse_rule(rule):
    [in_bag, out_bags] = rule.split(' contain ')
    in_color = regex.find_first_match(in_bag, r'(.*) bags?')
    outs = []
    for out_bag in out_bags[:-1].split(', '):
        out = regex.find_all_match(out_bag, r'((\d+) (.*) bags?)')
        if len(out) > 0:
            [(_, number, color)] = out
            outs.append((int(number), color))
    return in_color, outs


rules = [parse_rule(rule) for rule in raw_rules]


def find_rules_by_out_color(out_color):
    result = []
    for rule in rules:
        in_color, outs = rule
        for (number, color) in outs:
            if out_color == color:
                result.append(rule)
    return result


def find_rule_by_in_color(color):
    for rule in rules:
        in_color, outs = rule
        if in_color == color:
            return rule


def part_one():
    colors = ['shiny gold']
    collected = set()
    while len(colors) > 0:
        current = colors.pop(0)
        collected.add(current)
        in_colors = [in_color for (in_color, _) in find_rules_by_out_color(current)]
        colors += in_colors
    print(f'In colors number is {len(collected) - 1}')


def part_two():
    colors = [(1, 'shiny gold')]
    collected = []
    while len(colors) > 0:
        current_number, current_color = colors.pop(0)
        collected.append(current_number)
        (_, outs) = find_rule_by_in_color(current_color)
        colors += [(number * current_number, color) for (number, color) in outs]
    print(f'The final bags count is {sum(collected) - 1}')


if __name__ == '__main__':
    part_one()
    part_two()
