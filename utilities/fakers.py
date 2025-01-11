from random import choice, randint
from string import ascii_letters


def random_string(start: int = 9, end: int = 15) -> str:
    letters = ascii_letters
    rand_string = "".join(choice(letters) for _ in range(start, end))
    return rand_string


def random_number(start: int = 100, end: int = 1000) -> int:
    rand_int = randint(start, end)
    return rand_int
