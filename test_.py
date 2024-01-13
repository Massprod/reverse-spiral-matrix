from pytest import raises, mark
from conftest import create_square_matrix_string
from spiral_read_main import spiral_read, get_matrix
from validation_for_spiral_read import reverse_spiral_populate, reverse_spiral_read


@mark.asyncio
async def test_correct_counter_populate_read() -> None:
    """
    Testing creation of counter-clockwise spiral matrix with `reverse_spiral_populate`,
    and reading of it with reference function `reverse_spiral_read` and my function `spiral_read`.
    """
    with raises(ValueError) as _:
        await reverse_spiral_populate(-10)
    with raises(TypeError) as _:
        await reverse_spiral_populate('s')
    with raises(TypeError) as _:
        await reverse_spiral_populate(10.5)
    # Function `reverse_spiral_populate` is O(size * size). So, it's not a good idea to test big sizes.
    for size in range(1, 56):
        test_matrix: list[list[int]] = await reverse_spiral_populate(size)
        assert len(test_matrix) * len(test_matrix[0]) == size ** 2
        assert await spiral_read(test_matrix) == await reverse_spiral_read(test_matrix)


@mark.asyncio
async def test_spiral_read_empty_one_sized(one_row, one_col) -> None:
    """
    Testing different ways of reading input matrix's:
     - if it's only 1 row
     - if it's only 1 column
     - if it's correct matrix
    """
    # Empty matrix, empty return.
    assert not await spiral_read([])
    # Only 1 column
    reading: list[int] = await spiral_read(one_col)
    assert len(reading) == len(one_col)
    # Standard Top->Down reading.
    correct: list[int] = [row[0] for row in one_col]
    assert reading == correct
    # Only 1 row.
    reading = await spiral_read(one_row)
    assert len(reading) == len(one_row[0])
    # Standard Right->Left reading.
    correct = one_row[0][::-1]
    assert reading == correct


@mark.asyncio
async def test_client_connection_error() -> None:
    pass
