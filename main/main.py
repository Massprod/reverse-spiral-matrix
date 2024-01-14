from aiohttp import ClientSession, ClientTimeout
from aiohttp.client_exceptions import (
    InvalidURL, ClientConnectionError, ServerTimeoutError, ClientResponseError, ContentTypeError
)


async def spiral_read(matrix: list[list[int | str]]) -> list[int | str]:
    """
    Reads the matrix in counter-clockwise spiral order.
    Starting from NW corner == matrix[0][0].

    :param matrix: of any size.
    :return: all matrix values in counter-clockwise spiral order.
    """
    if len(matrix) == 0:
        return []
    max_x: int = len(matrix[0]) - 1
    spiral: list[int | str] = []
    # Only one column.
    if max_x == 0:
        for _ in matrix:
            spiral.append(_[0])
        return spiral
    max_y = len(matrix) - 1
    # Only one row.
    if max_y == 0:
        # We need counter-clock, row should be reversed.
        for x in range(len(matrix[0]) - 1, -1, -1):
            spiral.append(matrix[0][x])
        return spiral
    all_steps: int = len(matrix[0]) * len(matrix)
    x: int = 0
    dx: int = 0
    y: int = 0
    dy: int = 1
    steps: int = 1
    turn: int = 0
    min_x: int = 0
    min_y: int = 0
    spiral = [matrix[y][x]]
    while steps < all_steps:
        if turn == 3:
            min_x += 1
            max_x -= 1
            turn += 1
        elif turn == 5:
            min_y += 1
            max_y -= 1
            turn = 0
        x += dx
        y += dy
        spiral.append(matrix[y][x])
        if x == max_x and dy == 0 and dx == 1:
            dy, dx = -1, 0
            turn += 1
        elif y == max_y and dx == 0 and dy == 1:
            dy, dx = 0, 1
            turn += 1
        elif x == min_x and dy == 0 and dx == -1:
            dy, dx = 1, 0
            turn += 1
        elif y == min_y and dx == 0 and dy == -1:
            dy, dx = 0, -1
            turn += 1
        steps += 1
    return spiral


async def get_matrix(url: str) -> list[int]:
    """
    Makes GET request for input URL.
    Takes all possible digits from response payload, separated by non-digit symbols.
    Creates matrix from these values and if it's a Square matrix reads it in counter-clockwise spiral order.

    :param url: any URL string to work with.
    :return: correct counter-clockwise reading of given square-matrix.
    """
    # Default 5m, but it's too much in our case.
    timelimit: int = 35
    async with ClientSession(timeout=ClientTimeout(total=timelimit)) as connect:
        try:
            async with connect.get(url) as response:
                if not response.ok:
                    # If `response.ok` is False, then it's already >=400.
                    raise ClientResponseError(
                        headers=response.headers,
                        request_info=response.request_info,
                        status=response.status,
                        history=response.history,
                    )
                orig_matrix: str = await response.text()
                all_values: list[int] = []
                cur_value: str = ''
                for sym in orig_matrix:
                    if sym.isdigit():
                        cur_value += sym
                    elif cur_value:
                        all_values.append(int(cur_value))
                        cur_value = ''
                # If last symbol is digit, it will be added in `cur_value`,
                #  but never added into `all_values`. Extra check.
                if cur_value:
                    all_values.append(int(cur_value))
                # No digits at this page, at all.
                if not all_values:
                    return all_values
                row_length = col_length = int(len(all_values) ** 0.5)
                # Not a square matrix.
                if len(all_values) != (row_length * col_length):
                    raise ContentTypeError(
                        request_info=response.request_info,
                        status=204,
                        message=f"Numbers from provided url generates non-square matrix."
                                f" Only square matrix's allowed.",
                        history=response.history,
                    )
                # We're always reading matrix from URL left-top -> right-bot.
                # So, we already have `all_values` in correct order.
                # We just need to take them by row size == `row_length`.
                # index = 0 -> row_length => row_length -> row_length + row_length etc.
                correct_matrix: list[list[int]] = [
                    all_values[x * row_length: row_length + (row_length * x)] for x in range(row_length)
                ]
                return await spiral_read(correct_matrix)

        except TimeoutError as error:
            raise ServerTimeoutError(
                f'\nTimeout, service is unreachable.'
                f'\nError type: {type(error)}`'
                f'\nTimelimit: {timelimit}sec'
                f'\nProvided url: {url}'
            )
        except ClientConnectionError as error:
            raise ClientConnectionError(
                f'\nConnection error: `{error}`'
                f'\nError type: {type(error)}'
                f'\nProvided url: {url}',
            )
        except InvalidURL:
            raise InvalidURL(
                url=url,
            )
