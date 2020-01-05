import re

from day4Part1 import check_adjacent_digits, check_increasing_digits


def check_adjacent_digits_even(passcode):
    code_as_string = str(passcode)
    regexp = r'((.)\2+)'
    matches = re.findall(regexp, code_as_string)
    for match in matches:
        if len(match[0]) % 2 != 0:
            return False
    return True


def test_password(passcode):
    matchfirst = check_adjacent_digits(passcode) \
                  & check_increasing_digits(passcode)
    matchsecond = check_adjacent_digits(passcode) \
           & check_increasing_digits(passcode) \
           & check_adjacent_digits_even(passcode)

    if (matchfirst is True) & (matchsecond is False):
        # print(str(passcode))
        return matchsecond

    if matchfirst is not matchsecond:
        print('fail')

    return matchsecond


def find_solution():
    count = 0
    for x in range(359282, 820401):
        if test_password(x):
            count += 1
    print(count)
