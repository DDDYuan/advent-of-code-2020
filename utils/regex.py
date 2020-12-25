import re


def match_regex(string, regex):
    r = re.compile(regex)
    match = r.match(string)
    return match and match.group() == string


def match_any_regex(string, regex_list):
    for regex in regex_list:
        if match_regex(string, regex):
            return True
    return False


def find_all_match(string, regex):
    pattern = re.compile(regex)
    return pattern.findall(string)


def find_first_match(string, regex):
    return find_all_match(string, regex)[0]
