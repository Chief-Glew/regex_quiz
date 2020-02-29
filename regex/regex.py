import re


def check_regex_equivalent(test_string, regex, test_regex):
    expected = re.findall(regex, test_string)
    actual = re.findall(test_regex, test_string)
    return expected == actual, expected, actual
