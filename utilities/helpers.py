import re


def check_string_regexp(reg: str, string: str) -> bool:
    pattern = re.compile(reg)

    if pattern.match(string):
        return True
    else:
        return False


def check_exists_key(response: dict, key: str) -> bool:
    for _ in response:
        if _ == key:
            return True
    return False
