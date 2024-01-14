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
    yield [[randint(0, val) for _ in range(size)]]


@fixture
def one_col(size, val) -> list[list[int]]:
    yield [[randint(0, val)] for _ in range(size)]


@fixture
def correct_url() -> str:
    yield 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


@fixture
def correct_answer() -> list[int]:
    yield [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]


@fixture
def mock_url() -> str:
    yield 'https://testUrl/'


@fixture
def broken_url() -> str:
    yield 'http:/|broken../'


def create_square_matrix_string(size: int) -> tuple[str, list[int]]:
    """
    Create matrix string with extra symbols to filter.
    If size <= 0: creates non-digit string (empty matrix).
    Like in given string from:
    https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt

    :param size: of desired square-matrix.
    :return: string to filter and list of numbers which was used to build square-matrix string.
    """
    used_nums: list[int] = []
    symbols: str = ascii_letters + '!@#$^*()_+-/|}{|:";'
    if 0 >= size:
        return symbols, used_nums
    square_string: str = ''
    for num in range(size):
        cur_num: int = randint(0, 10 ** 8)
        used_nums.append(cur_num)
        # random SYMBOL + NUMBER + random SYMBOL
        square_string += choice(symbols) + str(cur_num) + choice(symbols)
    return square_string, used_nums
