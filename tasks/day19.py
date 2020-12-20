from utils import read_input

raw = read_input.read_input_strings_groups('day19_sample')


def parse_rule(raw_rule):
    [rule_id, targets] = raw_rule.split(': ')
    if 'a' not in targets and 'b' not in targets:
        return int(rule_id), [[int(target_id) for target_id in target.split(' ')] for target in targets.split(' | ')]
    else:
        return int(rule_id), targets[1:2]


def unresolved(rule):
    for target in rule:
        for rule_id in target:
            if isinstance(rule_id, int):
                return True
    return False


def part_one():
    rule_dict = dict()
    [rules, messages] = raw
    for rule in rules:
        rule_id, rule_target = parse_rule(rule)
        rule_dict[rule_id] = rule_target
    current = rule_dict[0]
    while unresolved(current):
        next_rule = []
        for target in current:
            for rule_id in target:
                target_target = rule_dict[rule_id]
                



def part_two():
    pass


if __name__ == '__main__':
    part_one()
    part_two()
