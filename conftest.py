from pytest import fixture
from random import randint
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

    :return: Tuple with string to filter and correct Numbers which was used to build it
    """
    nums: int = size
    used_nums: list[int] = []
    symbols: str = ascii_letters + '!@#$^*()_+-/|}{|:";'
    square_string: str = ''
    for _ in range(nums):
        cur_num: int = randint(-10 ** 16, 10 ** 16)
        used_nums.append(cur_num)
        slice_ind: int = randint(1, len(symbols) - 1)
        square_string += symbols[:slice_ind] + str(cur_num) + symbols[slice_ind:]
    return square_string, used_nums
