import asyncio
from pytest import raises, mark
from aioresponses import aioresponses
from main.main import spiral_read, get_matrix
from conftest import create_square_matrix_string
from main.validation import reverse_spiral_populate, reverse_spiral_read
from aiohttp.client_exceptions import ClientResponseError, ClientConnectionError, InvalidURL, ContentTypeError


@mark.asyncio
async def test_correct_counter_populate_read() -> None:
    """
    Testing creation of counter-clockwise spiral matrix with `reverse_spiral_populate`,
    and reading of it with reference function `reverse_spiral_read` and my function `spiral_read`.
    """
    with raises(ValueError):
        await reverse_spiral_populate(-10)
    with raises(TypeError):
        await reverse_spiral_populate('s')
    with raises(TypeError):
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
async def test_he400_errors(mock_url) -> None:
    """
    Testing higher|equal 400 HTTPErrors.
    All of them handled with aiohttp.client_exceptions.ClientResponseError.
    With all response data in this object (headers, request_info, status, history).
    """
    with aioresponses() as mocked:
        for status_code in range(400, 521, 5):
            mocked.get(url=mock_url, status=status_code)
            with raises(ClientResponseError):
                await get_matrix(mock_url)


@mark.asyncio
async def test_client_timeout(mock_url) -> None:
    """
    Testing asyncio.Timeout error.
    Coroutine timeout, a lot of reasons to throw. So, covering basic exception.
    """
    with aioresponses() as mocked:
        mocked.get(mock_url, exception=asyncio.TimeoutError)
        with raises(TimeoutError):
            await get_matrix(mock_url)


@mark.asyncio
async def test_client_connection_error(mock_url) -> None:
    """
    Testing aiohttp.client_exceptions.ClientConnectionError.
    Unable to create connection with server.
    """
    with aioresponses() as mocked:
        mocked.get(mock_url, exception=ClientConnectionError)
        with raises(ClientConnectionError):
            await get_matrix(mock_url)


@mark.asyncio
async def test_invalid_url_call(broken_url) -> None:
    """
    Testing aiohttp.client_exceptions.InvalidURL.
    Function call with incorrect type of url.
    """
    with raises(InvalidURL):
        await get_matrix(broken_url)


@mark.asyncio
async def test_non_digit_page(mock_url) -> None:
    """
    Testing correct function call with correct get() return,
     but `request.body` contains only non-digit symbols.
    """
    with aioresponses() as mocked:
        mocked.get(mock_url, body=create_square_matrix_string(-20)[0])
        res: list[int] = await get_matrix(mock_url)
        assert not res
