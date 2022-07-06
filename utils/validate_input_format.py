import re


def validate_format(msg, reg_formula):
    validate = False
    while not validate:
        value = input(msg)
        check_format = re.match(reg_formula, value)
        if check_format is not None:
            validate = True
        else:
            validate = False
    return value
