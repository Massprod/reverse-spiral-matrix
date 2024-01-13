# GPT or some Googled function, I used before.
# It's guaranteed it works.
# So, using this as reference to check if my function `spiral_read` works correctly.
# Also, `spiral_read` is reversed version of standard clock-wise order reading from my Leetcode solution.
# https://leetcode.com/problems/spiral-matrix/solutions/4558760/standard-single-traverse-r-90-m-30/


async def reverse_spiral_populate(row_length: int) -> list[list[int]]:
    """Creating square matrix with reverse_spiral_order of values."""
    if row_length <= 0:
        raise ValueError("Row length can't be negative or 0.")
    if type(row_length) != int:
        raise TypeError('Row length can only be Integer.')
    reverse_spiral_matrix = [[0] * row_length for _ in range(row_length)]
    steps = 1  # number of turns
    x, y = -1, 0  # starting indexes x - row, y - column (start from -1 to include 0, 0)
    s_row, s_column = 1, 0  # row/column step length
    number_to_populate = 1
    while steps <= row_length ** 2:
        if 0 <= x + s_row < row_length and 0 <= y + s_column < row_length \
                and reverse_spiral_matrix[x + s_row][y + s_column] == 0:
            x += s_row
            y += s_column
            steps += 1
            reverse_spiral_matrix[x][y] = number_to_populate
            number_to_populate += 1
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
    return reverse_spiral_matrix


async def reverse_spiral_read(matrix: list[list[int]]) -> list[int]:
    """Creating list of values in reverse_spiral_order of the given square matrix."""
    row_length = int(len(matrix[0]))
    reverse_spiral = []
    steps = 1  # number of turns
    x, y = -1, 0  # starting indexes x - row, y - column (start from -1 to include 0, 0)
    s_row, s_column = 1, 0  # row/column step length
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
