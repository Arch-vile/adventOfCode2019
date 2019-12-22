import re


def check_adjacent_digits(passcode):
    code_as_string = str(passcode)
    if re.match(r'.*(.)\1.*', code_as_string):
        return True
    else:
        return False


def check_increasing_digits(passcode):
    code_as_string = str(passcode)
    if re.match('^0*1*2*3*4*5*6*7*8*9*$', code_as_string):
        return True
    else:
        return False

    pass
