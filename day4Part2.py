import re


def check_adjacent_digits_even(passcode):
    code_as_string = str(passcode)
    regexp = r'((.)\2+)'
    matches = re.findall(regexp, code_as_string)
    for match in matches:
        if len(match[0]) % 2 != 0:
            return False
    return True
