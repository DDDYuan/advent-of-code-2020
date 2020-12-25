from utils import read_input
from copy import deepcopy

raw = read_input.read_input_strings_groups('day19')


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
    valid = ['a', 'b']
    for rule in rules:
        for rule_id in rule.split(' '):
            if rule_id not in valid:
                return True
    return False


def get_patterns(start_id):
    rule_dict = parse_rule_dict(raw)
    current = set(rule_dict[start_id])
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
                        for r in next_rule[:len(next_rule) // 2]:
                            r.append(targets[0])
                        for r in next_rule[len(next_rule) // 2:]:
                            r.append(targets[1])
            next_rule_join = [' '.join(r) for r in next_rule]
            next_rules += next_rule_join
        current = set(next_rules)
    valid_patterns = [s.replace(' ', '') for s in current]
    return valid_patterns


def is_valid_part_one(patterns1, patterns2, message):
    pattern_len = len(patterns1[0])
    message_len = len(message)
    shards = [message[i*pattern_len:(i+1)*pattern_len] for i in range(message_len // pattern_len)]
    return shards[0] in patterns1 and shards[1] in patterns1 and shards[2] in patterns2


def is_valid_part_two(patterns1, patterns2, message):
    pattern_len = len(patterns1[0])
    message_len = len(message)
    shards = [message[i*pattern_len:(i+1)*pattern_len] for i in range(message_len // pattern_len)]
    not_match_42 = False
    count_42 = 0
    count_31 = 0
    i = 0
    while i < len(shards):
        shard = shards[i]
        if not_match_42:
            if shard not in patterns2:
                return False
            else:
                count_31 += 1
                i += 1
        else:
            if shard not in patterns1:
                not_match_42 = True
            else:
                count_42 += 1
                i += 1
    return count_42 > count_31 > 0 and count_42 > 0


def part_one():
    patterns1 = get_patterns(42)
    patterns2 = get_patterns(31)
    [_, messages] = raw
    valid_messages = [message for message in messages if is_valid_part_one(patterns1, patterns2, message)]
    print(f'Valid messages count {len(valid_messages)}.')


def part_two():
    patterns1 = get_patterns(42)
    patterns2 = get_patterns(31)
    [_, messages] = raw
    valid_messages = [message for message in messages if is_valid_part_two(patterns1, patterns2, message)]
    print(f'Valid messages count {len(valid_messages)}.')


if __name__ == '__main__':
    part_one()
    part_two()
