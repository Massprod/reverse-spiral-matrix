from pytest import fixture
from random import randint, choice
from string import ascii_letters


@fixture
def size() -> int:
    yield randint(1, 33)


@fixture
def val() -> int:
    yield randint(1, 1000)


@fixture
def one_row(size, val) -> list[list[int]]:
    yield [[randint(-val, val) for _ in range(size)]]


@fixture
def one_col(size, val) -> list[list[int]]:
    yield [[randint(-val, val)] for _ in range(size)]


def create_square_matrix_string(size: int) -> tuple[str, list[int]]:
    """
    Create matrix string with extra symbols to filter.
    Like in given string from:
    https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt
    We need to test filtering of non-digits out and use only square-matrix's.

    :return: Tuple with string to filter and correct Numbers which was used to build square-matrix.
    """
    used_nums: list[int] = []
    symbols: str = ascii_letters + '!@#$^*()_+-/|}{|:";'
    if not size:
        return symbols, used_nums
    square_string: str = ''
    for num in range(size):
        cur_num: int = randint(-10 ** 8, 10 ** 8)
        used_nums.append(cur_num)
        # random SYMBOL + NUMBER + random SYMBOL
        square_string += choice(symbols) + str(cur_num) + choice(symbols)
    return square_string, used_nums
