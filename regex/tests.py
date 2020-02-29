from collections import namedtuple

import pytest

from regex.regex import check_regex_equivalent

HappyParam = namedtuple('HappyParam', ('test_string', 'regex', 'test_regex', 'regex_result'))

happy_params = (
    HappyParam(test_string='the quick brown fox jumped over the lazy dog', regex='the', test_regex='the',
               regex_result=['the', 'the']),
    HappyParam(test_string='hello', regex='.', test_regex='.', regex_result=['h', 'e', 'l', 'l', 'o']),
    HappyParam(test_string='hello', regex='l{2}', test_regex='ll', regex_result=['ll']),
)


@pytest.mark.parametrize('test_string,regex,test_regex,regex_result', happy_params)
def test_regex_is_equivalent(test_string, regex, test_regex, regex_result):
    equivalent, first_result, second_result = check_regex_equivalent(test_string, regex, test_regex)
    assert regex_result == first_result
    assert regex_result == second_result
    assert equivalent
