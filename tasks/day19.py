from utils import read_input
from copy import deepcopy

raw = read_input.read_input_strings_groups('day19')


def parse_rule(raw_rule):
    [rule_id, targets] = raw_rule.split(': ')
    if 'a' not in targets and 'b' not in targets:
        return int(rule_id), [[int(target_id) for target_id in target.split(' ')] for target in targets.split(' | ')]
    else:
        return int(rule_id), targets[1:2]


def not_complete(rules):
    for rule in rules:
        for target in rule:
            if isinstance(target, int):
                return True
    return False


def part_one():
    rule_dict = dict()
    [rules, messages] = raw
    for rule in rules:
        rule_id, rule_target = parse_rule(rule)
        rule_dict[rule_id] = rule_target
    current = rule_dict[0]
    while not_complete(current):
        next_rules = []
        for rule in current:
            next_rule = [[]]
            for rule_id in rule:
                if isinstance(rule_id, int):
                    target = rule_dict[rule_id]
                    if len(target) == 1:
                        for r in next_rule:
                            r += target[0]
                    else:
                        next_rule += deepcopy(next_rule)
                        for r in next_rule[:len(next_rule)//2]:
                            r += target[0]
                        for r in next_rule[len(next_rule)//2:]:
                            r += target[1]
                else:
                    for r in next_rule:
                        r.append(rule_id)
            next_rules += next_rule
        current = next_rules
    valid_messages = set([''.join(rule) for rule in current])
    print(valid_messages)
    count = len([valid for valid in messages if valid in valid_messages])
    print(count)


def part_two():
    pass


if __name__ == '__main__':
    part_one()
    part_two()
