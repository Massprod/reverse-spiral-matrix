import aiohttp
import numpy


async def get_matrix(url: str) -> list[int]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await session.close()
            try:
                # have no idea how to test other errors for now,
                # Guess I will need to learn Mock_server or similar and learn more about testing.
                # Never done testing before anyway.
                response.raise_for_status()
                text_data = await response.text()
                matrix_data = [int(element) for element in text_data.split() if element.isdigit()]  # leaving only digs
                # Матрица гарантированно содержит целые неотрицательные числа. #
                # Форматирование границ иными символами не предполагается. #
                # ^ This is why I won't be checking response text.#
                if len(matrix_data) == 0:
                    raise ValueError("There's no Digits to proceed.\n"
                                     "Text from URL should contain values of matrix separated by *spaces*")
                elif int(len(matrix_data) % len(matrix_data) ** 0.5) != 0:
                    raise ValueError("Only accepts square matrix's.\n")
                elif len(matrix_data) != 0:
                    steps = 1  # number of turns
                    x, y = -1, 0  # starting indexes x - row, y - column (start from -1 to include 0, 0)
                    s_row, s_column = 1, 0  # row/column step length
                    reverse_spiral = []
                    row_length = int(len(matrix_data) ** 0.5)  # length of square side
                    matrix = numpy.asarray(matrix_data).reshape(row_length, row_length)  # square matrix
                    used = []
                    while steps <= row_length ** 2:
                        if 0 <= x + s_row < row_length and 0 <= y + s_column < row_length \
                                and matrix[x + s_row][y + s_column] not in used:
                            x += s_row
                            y += s_column
                            reverse_spiral.append(matrix[x][y])
                            steps += 1
                            used.append(matrix[x][y])
                        else:
                            if s_column == 1:
                                s_column = 0
                                s_row = 1
                            elif s_row == 1:
                                s_row = 0
                                s_column = -1
                            elif s_column == -1:
                                s_column = 0
                                s_row = -1
                            elif s_row == -1:
                                s_row = 0
                                s_column = 1
                    return reverse_spiral
            except aiohttp.client.ClientResponseError as e:
                print(f"Error: {e.status}")
                print(f"Non existing page:\n{e.request_info.url}")
