import aiohttp
import numpy


async def get_matrix(url: str) -> list[int]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                await session.close()
                text_data = await response.text()
                steps = 1  # number of turns
                x, y = -1, 0  # starting indexes x - row, y - column (start from -1 to include 0, 0)
                s_row, s_column = 1, 0  # row/column step length
                reverse_spiral = []
                matrix_data = [int(element) for element in text_data.split() if element.isdigit()]  # leaving only digs
                row_length = int(len(matrix_data) ** 0.5)  # length of square side
                matrix = numpy.asarray(matrix_data).reshape(row_length, row_length)  # square matrix
                while steps <= row_length**2:
                    if 0 <= x + s_row < row_length and 0 <= y + s_column < row_length \
                            and matrix[x + s_row][y + s_column] != -1:
                        x += s_row
                        y += s_column
                        reverse_spiral.append(matrix[x][y])
                        steps += 1
                        matrix[x][y] = -1
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
