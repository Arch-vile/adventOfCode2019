import re


def check_adjacent_digits(passcode):
    code_as_string = str(passcode)
    if re.match(r'.*(.)\1.*', code_as_string):
        return True
    else:
        return False
