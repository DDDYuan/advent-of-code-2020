from utils import read_input, regex
from copy import deepcopy

raw = read_input.read_input_strings_groups('day19_sample')


def parse_rule(raw_rule):
    [rule_id, targets] = raw_rule.split(': ')
    if 'a' not in targets and 'b' not in targets:
        return int(rule_id), [target for target in targets.split(' | ')]
    else:
        return int(rule_id), [targets[1:2]]


def parse_rule_dict(raw_rules):
    rule_dict = dict()
    [rules, _] = raw_rules
    for rule in rules:
        rule_id, rule_target = parse_rule(rule)
        rule_dict[rule_id] = rule_target
    return rule_dict


def not_complete(rules):
    for rule in rules:
        for rule_id in rule.split(' '):
            if rule_id != 'a' and rule_id != 'b':
                return True
    return False


def part_one():
    rule_dict = parse_rule_dict(raw)
    [_, messages] = raw
    current = set(rule_dict[0])
    while not_complete(current):
        next_rules = []
        for rule in current:
            next_rule = [[]]
            for rule_id in rule.split(' '):
                if rule_id == 'a' or rule_id == 'b':
                    for r in next_rule:
                        r.append(rule_id)
                else:
                    targets = rule_dict[int(rule_id)]
                    if len(targets) == 1:
                        for r in next_rule:
                            r.append(targets[0])
                    else:
                        next_rule += deepcopy(next_rule)
                        for r in next_rule[:len(next_rule)//2]:
                            r.append(targets[0])
                        for r in next_rule[len(next_rule)//2:]:
                            r.append(targets[1])
            next_rule_join = [' '.join(r) for r in next_rule]
            next_rules += next_rule_join
        current = set(next_rules)
    valid_patterns = [s.replace(' ', '') for s in current]
    valid_messages = [message for message in messages if regex.match_any_regex(message, valid_patterns)]
    print(valid_messages)


def part_two():
    pass


if __name__ == '__main__':
    part_one()
    part_two()
